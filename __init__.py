import flask
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from os import path

db=SQLAlchemy()
DB_name="database.db"

def create_app():
    app=flask.Flask(__name__)
    app.config['SECRET_KEY']='asdfghjkl'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///{DB_name}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    return app

def create_data(app):
    if not path.exists('website/'+DB_name):
       db.create_app(app=app)
       print('created database!')
