from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Length, Email, EqualTo


#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    contact_number = IntegerField("Primary Contact Number")
    address = StringField("Home Address") # user needs to provide contact number and address based on assessment proj requirements to register
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class CommentForm(FlaskForm):  #User comment form
     text = TextAreaField('Comment here', [InputRequired()])
     submit = SubmitField('Send Comment')
    

class EventForm(FlaskForm): #creating create an event form
    name=StringField('Event Name')
    artist=StringField('Event Artist')
    start_datetime = DateTimeField('Event Start DateTime')
    end_datetime = DateTimeField('Event End DateTime') 
    venue = StringField('Event Venue')
    available_tickets = IntegerField('Available Tickets')
    image = StringField('Image File Name')
    description=TextAreaField('Event Description')
    submit = SubmitField("Create Event")
    
class ContactForm(FlaskForm): # create contact form to contact an interested user. the form does not ask for the password
    user_name = StringField('Name' )    
    email = StringField('Email Address')
    submit = SubmitField("Submit")
    
    

    
    
    
