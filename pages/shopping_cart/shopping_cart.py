import datetime, os
from flask import Blueprint, render_template, request, session, redirect
from utilities.db.db_shopping_cart import dbCart


shopping_cart = Blueprint('shopping_cart', __name__, static_folder='static', static_url_path='/shopping_cart', template_folder='templates')

# Routes
@shopping_cart.route('/shopping_cart')
def index():
    if session:
        user_email = session['Email']
        query_results= dbCart.get_user_cart(user_email)
        totalPrice= dbCart.calc_total_price(user_email)
        if query_results:
            return render_template('shopping_cart.html', products=query_results, totalP=totalPrice)
        else:
            return render_template('shopping_cart.html')
    return render_template('sign_in.html')


@shopping_cart.route('/update_quantity', methods=['get','post'])
def update_q():
     if session:
        user_email = session['Email']
        product = request.form['product']
        Quantity = request.form['quantity']
        dbCart.update_q(user_email,product,Quantity)
        return redirect('/shopping_cart')
     else:
        return render_template('shopping_cart.html')

@shopping_cart.route('/Delete_Item', methods=['post'])
def Delete_Item():
    if session:
        user_email = session['Email']
        product = request.form['product']
        dbCart.delete_product(user_email, product)
        return redirect('/shopping_cart')
    return render_template('sign_in.html')


@shopping_cart.route('/send_order', methods=['post'])
def send_order():
    if session:
        user_email = session['Email']
        DT = datetime.datetime.now().replace(microsecond=0)
        arrival = request.form['orderDate']
        phone = int(request.form['telNo'])
        address = request.form['address']
        card = request.form['card']
        ED = request.form['expiryDate']
        cvv = request.form['cvv']
        comment = request.form['comment']
        totalP = request.form['totalP']
        dbCart.add_to_orders(user_email, DT, arrival, phone, address, card, ED, cvv, comment, totalP)
        products = dbCart.get_products_order(user_email)
        for p in products:
            dbCart.add_products(user_email, DT, p[0], p[1], p[2])
        dbCart.delete_cart(user_email)
        return render_template('shopping_cart.html', message="הטופס נשלח לחנות בהצלחה!")
    else:
        return render_template('sign_in.html')
