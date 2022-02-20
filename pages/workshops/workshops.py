from flask import Blueprint, render_template, request, session
from utilities.db.db_workshops import dbWorkshops

workshops = Blueprint('workshops', __name__, static_folder='static', static_url_path='/workshops', template_folder='templates')


# Routes
@workshops.route('/workshops')
def workshopsIndex():
    workshops_list= dbWorkshops.get_workshops()
    return render_template('workshops.html', workshops=workshops_list)


@workshops.route('/workshop-details')
def workshop_details():
    if 'id' in request.args:
        w_id=request.args['id']
        workshop_d= dbWorkshops.get_details(w_id)
        return render_template('workshop_details.html', workshopDetails=workshop_d)

@workshops.route('/registration', methods=['post'])
def workshop_registration():
    if session:
        user_email = session['Email']
        workshop = request.form['workshop']
        workshopDT = request.form['workshopDT']
        workshopDTnew= workshopDT + ' 13:30:00'
        card = request.form['card']
        ED = request.form['expiryDate']
        cvv = request.form['cvv']
        num = int(request.form['workshopNum'])
        check = dbWorkshops.check_exist_reg(user_email, workshop, workshopDTnew)
        if check == []:
            dbWorkshops.add_reg(user_email, workshop, workshopDTnew, card, ED, cvv)
            dbWorkshops.update_num(workshop, num)
            workshop_d= dbWorkshops.get_details(workshop)
            return render_template('workshop_details.html', workshopDetails=workshop_d, message1="ההרשמה בוצעה בהצלחה!")
        else:
            workshop_d= dbWorkshops.get_details(workshop)
            return render_template('workshop_details.html', workshopDetails=workshop_d, message2="קיימת הרשמה קודמת לסדנה")
    return render_template('sign_in.html')






