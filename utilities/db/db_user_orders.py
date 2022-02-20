from utilities.db.db_manager import dbManager

class DBuser_orders:
    def get_orders(self, email):
        query = "SELECT * FROM group15.orders where email='%s'" %email
        res = dbManager.fetch(query=query)
        return res

    def get_products(self, email, DT):
        query = "SELECT o.product_ID, o.quantity, o.TotalPrice, p.img_url, p.product_name FROM group15.products_in_order as o inner Join group15.products as p on o.product_ID =  p.product_ID where email='%s' and order_creation_dt='%s'" %(email, DT)
        res = dbManager.fetch(query=query)
        return res


# Creates an instance for the DBproducts class for export.
dbUserOrders = DBuser_orders()