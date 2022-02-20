from utilities.db.db_manager import dbManager

class DBproduct:

    def get_product(self, id):
        product = "SELECT * FROM group15.products where product_id = '%s';" % id
        res = dbManager.fetch(query=product)
        return res

    def check_exist(self, id, email):
        check_q = "SELECT * FROM group15.shopping_carts where email = '%s' and product_ID = '%s';" % (email, id)
        res = dbManager.fetch(query=check_q)
        return res

    def update_shopping_c(self, email, p_id, quantity):
        add_q = quantity+1
        update_q = "update group15.shopping_carts set Quantity='%s' where email='%s' and product_ID = '%s';" %(add_q,email,p_id)
        dbManager.commit(query=update_q)
        return

    def add_product(self, email, p_id):
        add_query = "insert into group15.shopping_carts (email, product_ID, Quantity ) values ('%s','%s', '%s');" % (email, p_id, 1 )
        dbManager.commit(query=add_query)
        return

# Creates an instance for the DBproducts class for export.
dbProduct = DBproduct()