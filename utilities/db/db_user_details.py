from utilities.db.db_manager import dbManager

class DBuser_details:

    def update_details(self, email, password):
        query = "update group15.customers set Password='%s' where Email='%s';" %(password,email)
        dbManager.commit(query=query)
        return



dbUserDetails = DBuser_details()