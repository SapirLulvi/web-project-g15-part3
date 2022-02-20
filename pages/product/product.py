from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.db_product import dbProduct

# product blueprint definition
product = Blueprint('product', __name__, static_folder='static', static_url_path='/product', template_folder='templates')

# Routes
@product.route('/product')
def index():
    if 'id' in request.args:
        product_ID = request.args['id']
        product_details = dbProduct.get_product(product_ID)
        return render_template('product.html', product = product_details)

@product.route('/product_page/<int:p_id>')
def return_page(p_id):
    product_details = dbProduct.get_product(p_id)
    return render_template('product.html', product=product_details, msg="המוצר נוסף לסל בהצלחה!")

@product.route('/add_product_sc', methods = ['post'])
def add_p():
    if session:
        if 'p_id' in request.form:
            product_id = request.form['p_id']
            product_price = request.form['p_price']
            user_email = session['Email']
            product = dbProduct.check_exist(product_id,user_email)
            if product:
                quantity = product[0].Quantity
                dbProduct.update_shopping_c(user_email, product_id, quantity)
            else:
                dbProduct.add_product(user_email,product_id)
        return redirect(url_for('product.return_page', p_id=product_id))
    else:
        return render_template('sign_in.html')

