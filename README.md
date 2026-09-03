# FakerX Automation

A Flask-based web application that combines **user authentication, database management, and Selenium web automation** into a single project.

This project was created as a practical learning project to understand how Flask can be integrated with automation and a database while building a complete web application.

## 🚀 Features

* User registration
* Registration validation
* Password hashing
* User login and logout
* Session-based authentication
* SQLite database with SQLAlchemy
* Protected dashboard
* Selenium web automation
* Automated product search
* Product information extraction
* Add-to-cart and checkout automation on a demo store
* BeautifulSoup HTML inspection
* Requests-based HTTP operations
* Automation result reporting
* Modern responsive frontend

## 🛠️ Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* SQLAlchemy
* SQLite
* Selenium
* BeautifulSoup
* Requests
* HTML
* CSS
* Jinja2
* Gunicorn

## 📁 Project Structure

```text
FakerX-Automation/
│
├── app.py
├── automation.py
├── requirements.txt
├── .gitignore
│
├── fakerx/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   └── routes.py
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
└── static/
```

## ⚙️ How It Works

The application provides a web interface where users can register and log in.

After authentication, the user can access the dashboard and start the Selenium automation.

The automation performs a test workflow on the Sauce Demo Shopify website:

```text
Open Website
      ↓
Search for "jacket"
      ↓
Find Grey Jacket
      ↓
Read Product Information
      ↓
Add to Cart
      ↓
Open Cart
      ↓
Checkout
      ↓
Fill Test Information
      ↓
Complete Demo Checkout Flow
```

The automation is intended for **testing and learning purposes** and does not perform real payment authorization.

## 🔐 Authentication

The project uses Flask sessions for authentication and securely hashes user passwords before storing them in the database.

The application includes:

* Registration
* Login
* Logout
* Session management
* Database-backed users

## 🗄️ Database

The application uses **SQLite** with **Flask-SQLAlchemy**.

The database stores registered users and their hashed passwords.

The database is created automatically when the Flask application starts.

## 🤖 Selenium Automation

Selenium is integrated directly into the Flask application.

When the user starts the automation from the dashboard, Flask calls the Selenium automation function and displays the result on the dashboard.

The automation is designed around a demo/test e-commerce website and is not intended for real-world payment processing.

## 📦 Installation

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Enter the project directory:

```bash
cd FakerX-Automation
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run Locally

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🎯 Project Purpose

The main purpose of this project is to practice building a complete Flask application while integrating Python web automation.

It demonstrates practical knowledge of:

* Flask application structure
* Routing
* Templates
* Forms
* Sessions
* Authentication
* Password hashing
* SQLAlchemy
* SQLite
* Selenium
* BeautifulSoup
* Requests
* Git and GitHub
* Production deployment preparation

## 📌 Project Status

**Completed as a Flask learning and portfolio project.**

The project is currently prepared for deployment and further testing in a hosted environment.

## 👨‍💻 Author

**Mr Haseeb khan**

Built as part of my journey into **Python Automation, Web Development, and Cyber Security**.

