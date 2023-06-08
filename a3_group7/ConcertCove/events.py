from flask import Blueprint, render_template, request, redirect, url_for
from .models import Event, Comment
from .forms import EventForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename

destbp = Blueprint('event', __name__, url_prefix='/events')

@destbp.route('/<id>')
def show(id):
    event = db.session.scalar(db.select(event).where(event.id==id))
    cform = CommentForm()    
    return render_template('events/show.html', event=event, form=cform)

@destbp.route('/create', methods=['GET', 'POST'])
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():
    db_file_path = check_upload_file(form)
    event = Event(name=form.name.data, description=form.description.data, 
    image=form.image.data, start_datetime = form.start_datetime.data, end_datetime = form.end_datetime.data, venue = form.venue.data
                 available_tickets = form.available.tickets.data) 
    # currency was changed to status from the in class example
    db.session.add(event)
    db.session.commit()
    print('Successfully created new travel event', 'success')
    return redirect(url_for('event.create'))
  return render_template('event/create.html', form=form) # creat.html not made yet

def check_upload_file(form): 
  fp = form.image.data
  filename = fp.filename 
  BASE_PATH = os.path.dirname(__file__)
  upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
  db_upload_path = '/static/image/' + secure_filename(filename)
  fp.save(upload_path)
  return db_upload_path

@destbp.route('/<destination>/comment', methods=['GET', 'POST'])  
def comment(event):  
    form = CommentForm()  
    event = db.session.scalar(db.select(Event).where(Event.id==event))  
    if form.validate_on_submit():  
      comment = Comment(text=form.text.data, event=event) 
      db.session.add(comment) 
      db.session.commit() 
      print('Your comment has been added', 'success') 
    return redirect(url_for('event.show', id=event)) #does the orginal have a section for commects check for timedate thing in class
