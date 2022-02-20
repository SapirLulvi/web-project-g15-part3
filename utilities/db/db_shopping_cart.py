from utilities.db.db_manager import dbManager

class DBcart:

    def get_user_cart(self, email):
        user_cart = "SELECT s.product_ID, s.Quantity, p.product_name, p.img_url, p.price*s.Quantity as totalPrice FROM group15.shopping_carts as s inner JOIN group15.products as p on s.product_ID = p.product_ID where s.email ='%s' group by s.product_ID;" % email
        res = dbManager.fetch(query=user_cart)
        return res

    def delete_product(self,email, p_id):
        delete = "DELETE FROM group15.shopping_carts WHERE email='%s' and product_ID= '%s'; " % (email, p_id)
        dbManager.commit(query=delete)
        return

    def add_to_orders(self,email, dt, arrival, phone, address, card, ed, cvv, comment, totalP):
        ed1= ed + '-00'
        query = "insert into group15.orders (email, order_creation_dt, arrival_dt, phone_number, address, card, ExpiryDate, cvv, comment, TotalPrice) values ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (email, dt, arrival, phone, address, card, ed1, cvv, comment, totalP)
        dbManager.commit(query=query)
        return

    def get_products_order(self, email):
        user_order = "SELECT s.product_ID, s.Quantity, p.price*s.Quantity as totalPrice FROM group15.shopping_carts as s inner JOIN group15.products as p on s.product_ID = p.product_ID where s.email ='%s' group by s.product_ID;" % email
        res = dbManager.fetch(query=user_order)
        return res

    def add_products(self, email, dt, p_id, quantity, totalP):
        query = "insert into group15.Products_in_order (email, order_creation_dt, product_id, quantity, TotalPrice ) values ('%s','%s', '%s', '%s', '%s');" % (email, dt, p_id, quantity, totalP )
        dbManager.commit(query=query)
        return

    def delete_cart(self, email):
        query = "delete from group15.shopping_carts where email='%s';" % email
        dbManager.commit(query=query)
        return

    def calc_total_price(self, email):
        totalP ="select sum(new.totalPrice) as totalPriceCart from (SELECT s.product_ID, s.Quantity, p.price*s.Quantity as totalPrice FROM group15.shopping_carts as s inner JOIN group15.products as p on s.product_ID = p.product_ID where s.email ='%s' group by s.product_ID) as new;" % email
        res = dbManager.fetch(query=totalP)
        return res


    def update_q(self,email,p_id,q):
        updateQ = "update group15.shopping_carts set Quantity='%s' where email='%s' and product_ID = '%s';" % (int(q), email, p_id)
        dbManager.commit(query=updateQ)
        return


dbCart = DBcart()