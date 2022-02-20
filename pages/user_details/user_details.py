from flask import Blueprint, render_template, request, session
from utilities.db.db_user_details import dbUserDetails

user_details = Blueprint('user_details',__name__,static_folder='static',static_url_path='/user_details',template_folder='templates')

@user_details.route('/user_details')
def index():
    return render_template('user_details.html')

@user_details.route('/update_pass', methods=['post'])
def update_d():
    if session:
        user_email = session['Email']
        new_password = request.form['Password']
        dbUserDetails.update_details(user_email, new_password)
        session['Password'] = new_password
        return render_template('user_details.html', message='הסיסמה עודכנה בהצלחה!')

