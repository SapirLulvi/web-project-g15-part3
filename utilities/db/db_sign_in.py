from utilities.db.db_manager import dbManager

class DBsignIn:
    def check_user(self, email, password):
        user = "SELECT * FROM group15.customers WHERE Email='%s' AND Password='%s';" % (email, password)
        res = dbManager.fetch(query=user)
        return res




dbSign_in = DBsignIn()