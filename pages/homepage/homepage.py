from flask import Blueprint, render_template, redirect, url_for
from utilities.db.db_homepage import dbHomepage

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/')
def index():
    hot_products = dbHomepage.get_hotP()
    return render_template('homepage.html', hot_p=hot_products)


@homepage.route('/homepage')
@homepage.route('/home')
@homepage.route('/')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
