from flask import Flask
import os

def create_app():

    app = Flask(__name__ , template_folder="../templates")

#CONFIGURATION

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fakerx.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = "your-secret-key"


    from fakerx.extension import db

    db.init_app(app)

    from fakerx.routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app