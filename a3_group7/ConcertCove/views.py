from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import user_logged_in, login_required, current_user #login_required and current_user will work with a database with user information
# a user will only be able to access a certain page if logged in
from .forms import ContactForm, EventForm

bp = Blueprint('main', __name__)


# Will add more links to all pages and need to add neccessary code to each route
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')


@bp.route('/create')
def create():
    return render_template('create.html', title='Create')

@bp.route('/booking')
def booking():
    return render_template('booking.html', title='Booking')

@bp.route('/event_details')
def event_details():
    return render_template('event_details.html', title='Event Details')

@bp.route('/show')
def show():
    return render_template('show.html', title='Show')

@bp.route('/404error')
def error_404():
    return render_template('404error.html', title='404error')

@bp.route('/500error')
def error_500():
    return render_template('500error.html', title='500error')

@bp.route('/contact', methods=['GET','POST']) # both get and post methods
def create_contact():
     print('In contact view function')
     form = ContactForm()
     if form.validate_on_submit():
          print("Contact Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))

@bp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    if request.method == 'POST':
        pass  
    else:
        events = EventForm.query.all()  
        return render_template('create_event.html', events=events, name=current_user.name)
    

@bp.route('/booking_history')
@login_required
def booking_history():
    bookings = booking.query.filter_by(user_id=user_logged_in.id).all()  
    return render_template('booking_history.html', bookings=bookings, name=current_user.name)
