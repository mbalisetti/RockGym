# Rock's Gym - Django Web Application

A comprehensive gym management web application built with Django that provides gym members with equipment information, schedules, trainer details, and user authentication features.

## 🏋️‍♂️ Project Overview

Rock's Gym is a Django-based web application designed to help gym members access information about equipment, view schedules, learn about trainers, and manage their accounts. The application features a responsive design with Bootstrap styling and includes user authentication functionality.

## 🚀 Features

- **User Authentication System**
    - User registration and login
    - Secure password handling
    - Session management
    - Protected routes for authenticated users

- **Equipment Showcase**
    - Detailed equipment catalog with descriptions
    - Interactive equipment browser with tabs
    - Professional tips and muscle group information
    - High-quality equipment images

- **Gym Information**
    - Trainer profiles and qualifications
    - Gym schedules and timings
    - Address and contact information
    - Fee structure information

- **Responsive Design**
    - Bootstrap 4 integration
    - Mobile-friendly interface
    - Modern UI/UX design

## 🛠️ Technology Stack

- **Backend**: Django 3.0.5
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Database**: SQLite (default)
- **Authentication**: Django Auth System
- **JavaScript**: jQuery, Bootstrap JS

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.6 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd rockgym
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
   python -m venv gym_env

# Activate virtual environment
# On Windows:
gym_env\Scripts\activate
# On macOS/Linux:
source gym_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📱 Application Structure

```
rockgym/
├── manage.py
├── requirements.txt
├── rockgym/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── testapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── migrations/
└── templates/
    ├── registration/
    │   └── login.html
    └── testapp/
        ├── base.html
        ├── home.html
        ├── signup.html
        ├── equipments.html
        ├── trainer.html
        ├── fee.html
        ├── sched.html
        └── add.html
```

## 🌐 API Endpoints & URLs

| URL Pattern | View Function | Description | Authentication Required |
|-------------|---------------|-------------|------------------------|
| `/` | `home_view` | Homepage with gym overview | No |
| `/signup/` | `signup_view` | User registration | No |
| `/accounts/login/` | Django Auth | User login | No |
| `/accounts/logout/` | Django Auth | User logout | Yes |
| `/equip/` | `equp_view` | Equipment catalog | Yes |
| `/trainer/` | `trainer_view` | Trainer information | Yes |
| `/fee/` | `fee_view` | Fee structure | Yes |
| `/schedule/` | `sched_view` | Gym schedules | Yes |
| `/add/` | `add_view` | Gym address | No |
| `/admin/` | Django Admin | Admin panel | Admin Only |

## 🔐 Authentication Features

- **Registration**: New users can create accounts with username, email, and password
- **Login/Logout**: Secure session-based authentication
- **Protected Routes**: Equipment, trainer, fee, and schedule pages require authentication
- **Password Security**: Passwords are properly hashed using Django's built-in system

## 📊 Equipment Catalog

The application features a comprehensive equipment catalog including:

- **Strength Training**: Bench Press, Incline Bench, Dumbbells, Barbells
- **Cardio Equipment**: Treadmill, Indoor Cycling Bike, Elliptical Machine
- **Specialized Equipment**: Cable Machines, Pullup Bars, Leg Extension/Curl Machines
- **Functional Training**: Battle Ropes, Jump Ropes, Bumper Plates