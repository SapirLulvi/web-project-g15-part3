from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.db_sign_in import dbSign_in


sign_in = Blueprint('sign_in', __name__, static_folder='static', static_url_path='/sign_in', template_folder='templates')


# Routes

@sign_in.route('/sign_in')
def index():
    return render_template('sign_in.html')

@sign_in.route('/sign_in_req', methods=['post'])
def sign_req():
    useremail = request.form.get('Email')
    userpassword = request.form.get('Password')
    customer = dbSign_in.check_user(useremail,userpassword)
    if customer and len(customer):
        session['logged_in'] = True
        session['Email'] = customer[0].Email
        session['FirstName'] = customer[0].First_name
        session['LastName'] = customer[0].Last_name
        session['Password'] = customer[0].Password
        return redirect(url_for('homepage.index'))
    else:
        return render_template('sign_in.html', message="האימייל או הסיסמה שהזנת שגויים ! נא לנסות שוב")


