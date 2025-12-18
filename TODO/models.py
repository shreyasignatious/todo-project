from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)
    task = db.relationship('Task',back_populates='owner')

class Task(db.Model):
    task_id = db.Column(db.Integer,primary_key=True,unique=True,nullable=False)
    task_name = db.Column(db.String(150),nullable=False)
    task_desc = db.Column(db.String(1500))
    comp_date = db.Column(db.DateTime,nullable=False)
    priority = db.Column(db.String(100),default='No Priority')
    cato = db.Column(db.String(100),default='No Category')
    rel_user = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    owner = db.relationship('User',back_populates='task')