from flask import Blueprint, render_template, request, redirect, url_for
from .forms import ContactForm

bp = Blueprint('main', __name__)


# Will add more links to all pages and need to add neccessary code to each route
@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home')

@bp.route('/create')
def create():
    return render_template('create.html', title='Create')

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
