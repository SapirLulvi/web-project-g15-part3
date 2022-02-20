from utilities.db.db_manager import dbManager

class DBhomepage:
    def get_hotP(self):
        hot_p_query = "select h.product_id, p.product_name, p.img_url  from (select product_id, sum(quantity) as q from group15.products_in_order group by product_id order by q desc limit 6) as h inner JOIN group15.products as p on h.product_id=p.product_ID;"
        res = dbManager.fetch(query=hot_p_query)
        return res

dbHomepage = DBhomepage()

