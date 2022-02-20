from flask import Blueprint, render_template, request, session, redirect
import datetime
from utilities.db.db_workshops import dbWorkshops

# wish_list blueprint definition
my_workshops = Blueprint('my_workshops',
                  __name__,
                  static_folder='static',
                  static_url_path='/my_workshops',
                  template_folder='templates')

# Routes
@my_workshops.route('/my_workshops')
def index():
    if session:
        user_email = session['Email']
        future_workshops= dbWorkshops.future_w(user_email)
        previous_workshops= dbWorkshops.old_w(user_email)
        return render_template('my_workshops.html', Fworkshops=future_workshops, Pworkshops=previous_workshops )
    else:
        return render_template('sign_in.html')



@my_workshops.route('/Delete_Workshop', methods=['post'])
def Delete_Workshop():
    if session:
        user_email = session['Email']
        workshop = request.form['workshop']
        dbWorkshops.delete_reg(user_email, workshop)
        return redirect('/my_workshops')


