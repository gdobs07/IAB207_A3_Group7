from flask_login import UserMixin
import sqlite3
from . import db
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment', backref='user')
    bookings = db.relationship('Booking', backref='user', lazy=True)

    
    
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    artist = db.Column(db.String(80)) 
    status = db.Column(db.String(10))
    genre = db.Column(db.String(20))
    description = db.Column(db.String(200))
    image = db.Column(db.String(80), nullable=False, default='default.jpg')
    venue = db.Column(db.String(60))
    cost = db.Column(db.String(5)) 
    comments = db.relationship('Comment', backref='event')
    bookings = db.relationship('Booking', backref='event')
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)
    
class Booking(db.Model):
    __tablename__ = 'bookings'
    booking_id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    price = db.Column(db.Integer)
    ticket_quantity = db.Column(db.Integer)
    image = db.Column(db.String(80), nullable=False, default='default.jpg')
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    def __repr__(self):
        return "<Booking: {}>".format(self.booking_id)

   
