from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import db
import os
from alembic.command import upgrade
from alembic.config import Config

app = Flask(__name__)

if os.environ.get("FLASK_ENV") != "production":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
else:
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_dev_secret_key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    if os.environ.get("FLASK_ENV") == "production":
        alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "migrations", "alembic.ini"))
        upgrade(alembic_cfg, "head")

# Dummy credentials
USERNAME = "a"
PASSWORD = "a"

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname == USERNAME and pwd == PASSWORD:
            session['user'] = uname
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid Username or Password", "danger")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')


from models import Student

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name'].strip()
        uid = request.form['uid'].strip()

        if not name or not uid:
            flash("Please fill in all fields.", "danger")
            return redirect(url_for('register'))

        # Check if UID already exists
        existing_student = Student.query.filter_by(uid=uid).first()
        if existing_student:
            flash("UID already exists. Try a different one.", "danger")
        else:
            new_student = Student(name=name, uid=uid)
            db.session.add(new_student)
            db.session.commit()
            flash("Student registered successfully!", "success")
            return redirect(url_for('register'))

    return render_template('register.html')


from flask import flash, render_template, redirect, request, session, url_for
from datetime import datetime
from models import Attendance, Student

@app.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if 'user' not in session:
        return redirect(url_for('login'))

    students = Student.query.order_by(Student.name).all()
    today = datetime.now().strftime("%Y-%m-%d")

    if request.method == 'POST':
        for student in students:
            status = request.form.get(f'attend_{student.id}')
            if status in ['P', 'A']:
                # Check if already marked
                existing = Attendance.query.filter_by(student_id=student.id, date=today).first()
                if existing:
                    existing.status = status 
                else:
                    new_attendance = Attendance(
                        student_id=student.id,
                        date=today,
                        status=status
                    )
                    db.session.add(new_attendance)
        db.session.commit()
        flash("✅ Attendance saved successfully!", "success")

    return render_template('attendance.html', students=students, today=today)



@app.route('/remove', methods=['GET'])
def remove():
    if 'user' not in session:
        return redirect(url_for('login'))

    students = Student.query.order_by(Student.name).all()
    return render_template('remove.html', students=students)

@app.route('/remove/<int:student_id>', methods=['POST'])
def remove_student(student_id):
    if 'user' not in session:
        return redirect(url_for('login'))

    student = Student.query.get_or_404(student_id)

    Attendance.query.filter_by(student_id=student.id).delete()

    db.session.delete(student)
    db.session.commit()
    flash(f"Student '{student.name}' removed successfully.", "success")
    return redirect(url_for('remove'))



from datetime import date as dt_date
from flask import request, flash

@app.route('/records', methods=['GET', 'POST'])
def records():
    if 'user' not in session:
        return redirect(url_for('login'))

    selected_date = request.args.get('date')
    if selected_date:
        try:
            selected_date = dt_date.fromisoformat(selected_date)
        except ValueError:
            flash("Invalid date format.", "error")
            selected_date = dt_date.today()
    else:
        selected_date = dt_date.today()

    students = Student.query.order_by(Student.name).all()
    attendance_data = []

    for student in students:
        att = Attendance.query.filter_by(student_id=student.id, date=selected_date).first()
        row = {
            'uid': student.uid,
            'name': student.name,
            'status': att.status if att else '-'
        }
        attendance_data.append(row)

    data_exists = any(row['status'] != '-' for row in attendance_data)

    return render_template('records.html',
                           students=attendance_data,
                           selected_date=selected_date,
                           data_exists=data_exists)



import pandas as pd
from flask import send_file
from io import BytesIO
from xhtml2pdf import pisa
from flask import make_response

@app.route('/export/excel')
def export_excel():
    students = Student.query.all()
    dates = sorted({a.date for a in Attendance.query.all()})

    data = []
    for student in students:
        row = {'Name': student.name, 'UID': student.uid}
        for date in dates:
            att = Attendance.query.filter_by(student_id=student.id, date=date).first()
            row[date] = att.status if att else "-"
        data.append(row)

    df = pd.DataFrame(data)
    output = BytesIO()
    df.to_excel(output, index=False, engine='openpyxl')
    output.seek(0)

    return send_file(output, download_name="attendance.xlsx", as_attachment=True)

@app.route('/export/pdf')
def export_pdf():
    students = Student.query.all()
    dates = sorted({a.date for a in Attendance.query.all()})

    html = render_template('records.html', students=[
        {
            **{'name': s.name, 'uid': s.uid},
            **{d: (Attendance.query.filter_by(student_id=s.id, date=d).first() or type('', (), {'status': '-'})()).status for d in dates}
        }
        for s in students
    ], dates=dates)

    result = BytesIO()
    pisa.CreatePDF(BytesIO(html.encode("utf-8")), dest=result)
    result.seek(0)

    return send_file(result, download_name="attendance.pdf", as_attachment=True)


@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", "success")
    return redirect(url_for('login'))

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# Create admin instance
admin = Admin(app, name='Attendance Admin', template_mode='bootstrap4')

# Add your models
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Attendance, db.session))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
