from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.category.category import category
app.register_blueprint(category)

## Product
from pages.product.product import product
app.register_blueprint(product)

## Workshops
from pages.workshops.workshops import workshops
app.register_blueprint(workshops)

## Sign_in
from pages.sign_in.sign_in import sign_in
app.register_blueprint(sign_in)

## Sign_up
from pages.sign_up.sign_up import sign_up
app.register_blueprint(sign_up)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## log_out
from pages.log_out.log_out import log_out
app.register_blueprint(log_out)

## log_out
from pages.shopping_cart.shopping_cart import shopping_cart
app.register_blueprint(shopping_cart)

## user_details
from pages.user_details.user_details import user_details
app.register_blueprint(user_details)


## my_workshops
from pages.my_workshops.my_workshops import my_workshops
app.register_blueprint(my_workshops)

## my_orders
from pages.my_orders.my_orders import my_orders
app.register_blueprint(my_orders)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

##header
from components.header.header import header
app.register_blueprint(header)

## footer
from components.footer.footer import footer
app.register_blueprint(footer)


