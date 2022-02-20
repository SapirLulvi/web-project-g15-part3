from utilities.db.db_manager import dbManager

class DBsignUp:
    def checkEmail(self, email):
        check = "SELECT * FROM group15.customers WHERE Email= '%s';" %email
        res = dbManager.fetch(query=check)
        return res

    def insert_user(self, email, password, fname, lname):
        insert = "INSERT INTO group15.customers(Email, Password, First_name, Last_name) VALUES('%s','%s','%s','%s');" %(email, password, fname, lname)
        res = dbManager.commit(query=insert)
        return res


dbSign_up = DBsignUp()