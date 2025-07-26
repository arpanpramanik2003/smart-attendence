# Attendance Management System

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

A web-based attendance management system built with Flask that allows teachers to track student attendance, manage student records, and generate reports.

## Features

- **User Authentication**
  - Secure login system
  - Default credentials: username=`a`, password=`a`

- **Student Management**
  - Register new students with unique UID
  - Remove students from the system
  - View all registered students

- **Attendance Tracking**
  - Mark daily attendance (Present/Absent)
  - View attendance records by date
  - Edit existing attendance records

- **Reporting**
  - Export attendance data to Excel
  - Generate PDF reports
  - View attendance history for any date

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (Development), PostgreSQL (Production)
- **ORM**: SQLAlchemy
- **Migrations**: Flask-Migrate (Alembic)
- **Templating**: Jinja2
- **Reporting**: Pandas (Excel), WeasyPrint (PDF)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/arpanpramanik2003/smart-attendance.git
   cd smart-attendance

## Installation & Setup

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   # Linux/Mac:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Configure environment variables:
   ```bash
   # Linux/Mac:
    export FLASK_APP=app.py
    export FLASK_DEBUG=1
    export SECRET_KEY=your-secret-key-here
    
    # Windows:
    set FLASK_APP=app.py
    set FLASK_DEBUG=1
    set SECRET_KEY=your-secret-key-here
## Login Credentials

Default admin credentials:
- **Username:** `a`
- **Password:** `a`

## Deployment (Render)

1. **Set up PostgreSQL database** on Render
2. **Configure environment variables**:
   - `DATABASE_URL`: postgresql://attendence_db_lstr_user:FNlCnojEWCnNE7hb94rLaPJzvBbbFUZf@dpg-d22fv6qdbo4c73f6p0pg-a/attendence_db_lstr
   - `SECRET_KEY`: Hidden
   - `FLASK_DEBUG`: Set to `0` in production
  
## File Structure
attendance-app/
├── migrations/          # Database migration files
├── templates/          # HTML templates
├── .gitignore
├── app.py              # Main application file
├── models.py           # Database models
├── requirements.txt    # Dependencies
└── README.md

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

We welcome contributions! Please follow these steps:  
1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add some feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request  

For major changes, please open an issue first to discuss your proposed changes.

## Acknowledgements

Special thanks to:  
- [Flask](https://flask.palletsprojects.com/) for the web framework  
- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM support  
- [Render](https://render.com/) for deployment platform  

---
