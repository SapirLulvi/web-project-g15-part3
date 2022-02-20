from utilities.db.db_manager import dbManager

class DBcategory:
    def get_categories(self):
        categories = "SELECT * FROM group15.categories;"
        res = dbManager.fetch(query=categories)
        return res

    def get_category(self, id):
        category_products = "SELECT p.product_ID, p.category_ID, p.product_name, p.price, p.img_url, c.category_name FROM group15.products as p inner JOIN group15.categories as c on p.category_ID = c.category_ID WHERE p.category_ID = '%s';" % id
        res = dbManager.fetch(query=category_products)
        return res



# Creates an instance for the DBproducts class for export.
dbCategory = DBcategory()