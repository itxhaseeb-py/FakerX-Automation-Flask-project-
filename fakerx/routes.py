from flask import Blueprint, render_template, request, redirect, url_for, flash , session
from werkzeug.security import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
import re
from automation import run_automation

from fakerx.extension import db
from fakerx.model import User


main = Blueprint("main", __name__)


# -------------------------
# HOME / REGISTRATION PAGE
# -------------------------

@main.route("/")
def home():
    return render_template("index.html")


# -------------------------
# REGISTRATION
# -------------------------

@main.route("/register", methods=["POST"])
def register():

    # Get form data
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")


    # -------------------------
    # NAME VALIDATION
    # -------------------------

    if not name:
        flash("Name is required.")
        return render_template("index.html")

    if len(name) < 2:
        flash("Name must contain at least 2 characters.")
        return render_template("index.html")

    if len(name) > 50:
        flash("Name must not exceed 50 characters.")
        return render_template("index.html")

    if not all(part.isalpha() for part in name.split()):
        flash("Name must contain only letters and spaces.")
        return render_template("index.html")


    # -------------------------
    # EMAIL VALIDATION
    # -------------------------

    if not email:
        flash("Email is required.")
        return render_template("index.html")

    email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(email_pattern, email):
        flash("Please enter a valid email address.")
        return render_template("index.html")


    # -------------------------
    # PASSWORD VALIDATION
    # -------------------------

    if not password:
        flash("Password is required.")
        return render_template("index.html")

    if len(password) < 8:
        flash("Password must be at least 8 characters long.")
        return render_template("index.html")

    if len(password) > 128:
        flash("Password must not exceed 128 characters.")
        return render_template("index.html")

    if not re.search(r"[A-Z]", password):
        flash("Password must contain at least one uppercase letter.")
        return render_template("index.html")

    if not re.search(r"[a-z]", password):
        flash("Password must contain at least one lowercase letter.")
        return render_template("index.html")

    if not re.search(r"\d", password):
        flash("Password must contain at least one number.")
        return render_template("index.html")


    # -------------------------
    # CHECK EXISTING EMAIL
    # -------------------------

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        flash("This email is already registered.")
        return render_template("index.html")


    # -------------------------
    # CREATE USER
    # -------------------------

    password_hash = generate_password_hash(password)

    user = User(
        name=name,
        email=email,
        password=password_hash
    )

    db.session.add(user)
    db.session.commit()


    # -------------------------
    # SUCCESS → INFORMATION PAGE
    # -------------------------

    return render_template("register.html")









@main.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    if not email:
        flash("Email is required.")
        return render_template("login.html")

    if not password:
        flash("Password is required.")
        return render_template("login.html")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("Invalid email or password.")
        return render_template("login.html")

    if not check_password_hash(user.password, password):
        flash("Invalid email or password.")
        return render_template("login.html")

    # Login successful
    return redirect(url_for("main.dashboard"))






@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")






@main.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("main.login"))






@main.route("/run-automation", methods=["POST"])
def run_selenium():

    result = run_automation()

    return render_template(
        "dashboard.html",
        result=result
    )
# -------------------------
# PROJECT INFORMATION PAGE
# -------------------------

# @main.route("/about")
# def about():
#     return render_template("register.html")