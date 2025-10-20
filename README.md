# 🎯 Smart Attendance Management System

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://smart-attendence.onrender.com)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## 📋 Project Summary

A comprehensive web-based attendance management system built with Flask that enables educational institutions to efficiently track student attendance, manage student records, and generate detailed reports. The system provides a user-friendly interface for teachers and administrators to streamline the attendance tracking process with secure authentication and robust data management capabilities.

**🚀 Key Highlights:**
- Modern web interface with responsive design
- Secure user authentication system
- Real-time attendance tracking and management
- Comprehensive reporting with multiple export formats
- Cloud deployment ready (Render/Heroku compatible)

## ✨ Features

### 🔐 **Secure Authentication**
- Role-based access control
- Secure session management
- Password protection with encryption
- Default admin credentials: `username: a, password: a`

### 👥 **Student Management**
- ➕ Register new students with unique identifiers (UID)
- 🗑️ Remove students from the system
- 📊 View comprehensive student directories
- 🔍 Search and filter student records
- 📝 Edit student information

### 📅 **Daily Attendance Tracking**
- ✅ Mark attendance status (Present/Absent/Late)
- 📆 Date-wise attendance management
- ⏰ Timestamp tracking for attendance records
- 🔄 Edit and update existing attendance records
- 📈 Real-time attendance statistics

### 📊 **Advanced Reporting & Analytics**
- 📁 Export attendance data to Excel (.xlsx)
- 📄 Generate professional PDF reports
- 📋 View detailed attendance history by date range
- 📈 Attendance percentage calculations
- 📊 Visual attendance analytics and insights

### 💾 **Data Export Capabilities**
- Multiple export formats (Excel, PDF, CSV)
- Customizable date range selection
- Filtered export options
- Professional report formatting

## 🛠️ Technology Stack

### **Backend**
- **Framework**: Python Flask 2.x
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **ORM**: SQLAlchemy with Flask-SQLAlchemy
- **Migrations**: Flask-Migrate (Alembic)
- **Authentication**: Flask-Login

### **Frontend**
- **Templating**: Jinja2
- **Styling**: CSS3 with Bootstrap components
- **JavaScript**: Vanilla JS for interactivity
- **Responsive Design**: Mobile-first approach

### **Data Processing & Reporting**
- **Excel Export**: Pandas + openpyxl
- **PDF Generation**: WeasyPrint
- **Data Analysis**: NumPy, Pandas

### **Deployment & DevOps**
- **Cloud Platform**: Render (Primary), Heroku (Alternative)
- **Database**: PostgreSQL (Production)
- **Environment Management**: python-dotenv

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+ installed on your system
- Git for version control
- Virtual environment (recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/arpanpramanik2003/smart-attendence.git
cd smart-attendence
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv attendance_env

# Activate virtual environment
# On Windows:
attendance_env\Scripts\activate

# On macOS/Linux:
source attendance_env/bin/activate
```

### 3. Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# If requirements.txt doesn't exist, install manually:
pip install flask flask-sqlalchemy flask-migrate pandas openpyxl weasyprint
```

### 4. Environment Configuration
```bash
# Create .env file
touch .env

# Add the following variables to .env:
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///attendance.db
```

### 5. Database Setup
```bash
# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Run the Application
```bash
# Start the development server
flask run

# Or alternatively:
python app.py
```

The application will be available at `http://localhost:5000`

## 🚀 Deployment

### Render Deployment (Recommended)

1. **Prepare for Deployment:**
   ```bash
   # Ensure you have these files:
   # - requirements.txt
   # - Procfile (web: gunicorn app:app)
   # - runtime.txt (python-3.9.x)
   ```

2. **Database Configuration:**
   - Set `DATABASE_URL` environment variable to PostgreSQL URL
   - Update database configurations for production

3. **Deploy on Render:**
   - Connect your GitHub repository
   - Configure build and start commands
   - Set environment variables
   - Deploy automatically from main branch

### Alternative Cloud Platforms
- **Heroku**: Use Heroku Postgres add-on
- **Railway**: Direct GitHub integration
- **PythonAnywhere**: Manual file upload option

## 📖 Usage Instructions

### 🔑 **Admin Dashboard Access**
1. Navigate to the application URL
2. Login with admin credentials:
   - Username: `a`
   - Password: `a`
3. Access the main dashboard

### 👨‍🎓 **Student Management**
1. **Add New Student:**
   - Click "Add Student" button
   - Enter student name and unique UID
   - Submit the form

2. **View Students:**
   - Navigate to "Students" section
   - Browse through student directory
   - Use search functionality if needed

3. **Remove Student:**
   - Find student in the directory
   - Click "Remove" button
   - Confirm the action

### ✅ **Attendance Marking**
1. **Daily Attendance:**
   - Select the current date
   - Choose students from the list
   - Mark Present/Absent status
   - Save attendance records

2. **Edit Attendance:**
   - Navigate to specific date
   - Modify existing attendance records
   - Update and save changes

### 📊 **Report Generation & Export**
1. **Generate Reports:**
   - Select date range
   - Choose report format (Excel/PDF)
   - Click "Generate Report" button
   - Download the generated file

2. **View Attendance History:**
   - Navigate to "Reports" section
   - Filter by date, student, or class
   - View detailed attendance statistics

## 📁 File Structure

```
smart-attendence/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── Procfile               # Deployment configuration
├── runtime.txt            # Python runtime version
├── .env                   # Environment variables
├── migrations/            # Database migration files
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── students.html
│   ├── attendance.html
│   └── reports.html
├── models/                # Database models
│   ├── __init__.py
│   ├── student.py
│   └── attendance.py
├── routes/                # Application routes
│   ├── __init__.py
│   ├── auth.py
│   ├── students.py
│   └── attendance.py
└── utils/                 # Utility functions
    ├── __init__.py
    ├── export.py
    └── helpers.py
```

## 🤝 Contributing

We welcome contributions to improve the Smart Attendance Management System! Here's how you can contribute:

### Getting Started
1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Make your changes** with proper documentation
4. **Add tests** for new functionality
5. **Commit changes:** `git commit -m 'Add amazing feature'`
6. **Push to branch:** `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Contribution Guidelines
- 📝 Write clear commit messages
- 📋 Update documentation for new features
- 🧪 Add tests for new functionality
- 🎨 Follow Python PEP 8 style guidelines
- 📱 Ensure responsive design compatibility
- 🔍 Test thoroughly before submitting PR

### Areas for Contribution
- 🌟 UI/UX improvements
- 🔧 Performance optimizations
- 🛡️ Security enhancements
- 📊 Additional reporting features
- 🌐 Internationalization support
- 📱 Mobile app development

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Arpan Pramanik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 📞 Contact Information

👨‍💻 **Developer:** Arpan Pramanik

📧 **Email:** [arpanpramanik2003@gmail.com](mailto:arpanpramanik2003@gmail.com)

💼 **LinkedIn:** [Connect with Arpan Pramanik](https://linkedin.com/in/arpanpramanik2003)

🐱 **GitHub:** [@arpanpramanik2003](https://github.com/arpanpramanik2003)

📱 **Portfolio:** [Visit Portfolio](https://arpanpramanik.dev)

---

## 🙏 Acknowledgments

- **Flask Community** - For the excellent web framework and documentation
- **SQLAlchemy Team** - For the powerful ORM capabilities
- **Bootstrap** - For responsive design components
- **Open Source Community** - For inspiration and code examples
- **Educational Institutions** - For feedback and feature suggestions
- **Contributors** - Thank you to all who have contributed to this project

### Special Thanks
- 🎓 **Educational Technology Community** for valuable insights
- 🔧 **Flask Extension Developers** for amazing tools
- 📚 **Documentation Writers** for clear guides and tutorials
- 🧪 **Beta Testers** for thorough testing and feedback

---

## 📈 Project Stats

[![GitHub stars](https://img.shields.io/github/stars/arpanpramanik2003/smart-attendence)](https://github.com/arpanpramanik2003/smart-attendence/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/arpanpramanik2003/smart-attendence)](https://github.com/arpanpramanik2003/smart-attendence/network)
[![GitHub issues](https://img.shields.io/github/issues/arpanpramanik2003/smart-attendence)](https://github.com/arpanpramanik2003/smart-attendence/issues)
[![GitHub license](https://img.shields.io/github/license/arpanpramanik2003/smart-attendence)](https://github.com/arpanpramanik2003/smart-attendence/blob/master/LICENSE)

---

<div align="center">
  <h3>🌟 If you found this project helpful, please consider giving it a star! 🌟</h3>
  <p><strong>Made with ❤️ by <a href="https://github.com/arpanpramanik2003">Arpan Pramanik</a></strong></p>
</div>
