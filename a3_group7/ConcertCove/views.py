from flask import Blueprint, render_template

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