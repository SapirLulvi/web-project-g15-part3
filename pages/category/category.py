from flask import Blueprint, render_template, request
from utilities.db.db_category import dbCategory


# catalog blueprint definition
category = Blueprint('category', __name__, static_folder='static', static_url_path='/category', template_folder='templates')


# Routes
@category.route('/categories')
def categoriesIndex():
    categories= dbCategory.get_categories()
    return render_template('categories.html', categories_list=categories)

# Routes
@category.route('/category')
def index():
    if 'id' in request.args:
        category_ID = request.args['id']
        category_products = dbCategory.get_category(category_ID)
        return render_template('category.html', products = category_products)

