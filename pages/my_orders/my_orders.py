from flask import Blueprint, render_template ,request, session,redirect,url_for
from utilities.db.db_user_orders import dbUserOrders
my_orders = Blueprint('my_orders', __name__, static_folder='static', static_url_path='/my_orders', template_folder='templates')

# Routes
@my_orders.route('/my_orders')
def index():
    user_email = session['Email']
    orders = dbUserOrders.get_orders(user_email)

    if orders: #אם השאילתה הצליחה
        return render_template('my_orders.html',userOrders=orders)
    return render_template('my_orders.html')

@my_orders.route('/order_details')
def order_details():
    email = request.args['id']
    dateTime = request.args['date']
    products_list = dbUserOrders.get_products(email, dateTime)
    if products_list:
        return render_template('order_details.html', products=products_list)
    return render_template('order_details.html')



