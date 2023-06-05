from flask_login import UserMixin
import sqlite3
from . import db
from datetime import datetime

sqliteConnection = sqlite3.connect('Model.db') #this should create the overall database if the main runs i.e. we would add to the database through the website. If thiss causees issues when testing please delet.

class User(UserMixin, db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('comment', backref='user')
    
    
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    #artist = db.Column(db.String(80)) to be added if you guys want? -MS
    status = db.Column(db.String(10))
    genre = db.Column(db.String(20))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    #cost = db.Column(db.String(5)) to be added if you guys want? -MS
    comments = db.relationship('comment', backref='event')
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)
