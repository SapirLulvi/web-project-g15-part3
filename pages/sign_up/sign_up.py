from flask import Blueprint, render_template, request
from utilities.db.db_sign_up import dbSign_up


sign_up = Blueprint('sign_up', __name__, static_folder='static', static_url_path='/sign_up', template_folder='templates')

@sign_up.route('/sign_up')
def index():
    return render_template('sign_up.html')

@sign_up.route('/sign_up_reg', methods=['post'])
def insert_user():
    email = request.form.get('Email')
    password = request.form.get('Password')
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email_exists = dbSign_up.checkEmail(email)
    if email_exists:
        return render_template('sign_up.html', message1="האימייל כבר קיים במערכת")
    else:
        new_customer = dbSign_up.insert_user(email, password, first_name, last_name)
        if new_customer:
            return render_template('sign_in.html', message="נרשמת בהצלחה ! בצע התחברות")

