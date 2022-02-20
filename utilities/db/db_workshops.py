from utilities.db.db_manager import dbManager

class DBworkshops:
    def get_workshops(self):
        workshops = "SELECT * FROM group15.workshops where workshop_dt >= NOW(); "
        res = dbManager.fetch(query=workshops)
        return res

    def check_exist_reg(self, email, ws_ID, ws_DT):
        query_check = "SELECT * FROM group15.Registrations_workshops where email = '%s' and ws_ID = '%s' and ws_DT = '%s';" % (email, ws_ID, ws_DT)
        res = dbManager.fetch(query=query_check)
        return res

    def get_details(self, id):
        details = "SELECT * FROM group15.workshops where workshop_ID = '%s';" % id
        res = dbManager.fetch(query=details)
        return res

    def add_reg(self, email, ws_ID, ws_DT, card, ed, cvv):
        ed1= ed + '-00'
        query_add="insert into group15.Registrations_workshops (email, ws_ID, ws_DT, card, ExpiryDate, cvv) VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % (email, ws_ID, ws_DT, card, ed1, cvv)
        res = dbManager.commit(query=query_add)
        return res

    def update_num(self, ws_ID, num):
        num1=num-1
        query = "update group15.workshops set num_of_people='%s' where workshop_ID='%s';" %(num1,ws_ID)
        dbManager.commit(query=query)
        return

    def future_w(self, email):
        workshops = "SELECT r.email, r.ws_ID, r.ws_DT, w.workshop_name, w.img_url, w.price FROM group15.Registrations_workshops as r inner JOIN group15.workshops as w on r.ws_ID = w.workshop_ID where workshop_dt >= NOW() and r.email = '%s';" %email
        res = dbManager.fetch(query=workshops)
        return res

    def old_w(self, email):
        workshops = "SELECT r.email, r.ws_ID, r.ws_DT, w.workshop_name, w.img_url, w.price FROM group15.Registrations_workshops as r inner JOIN group15.workshops as w on r.ws_ID = w.workshop_ID where workshop_dt < NOW() and r.email = '%s';" %email
        res = dbManager.fetch(query=workshops)
        return res

    def delete_reg(self, email,  ws_ID):
        num_query = "select num_of_people from group15.workshops where workshop_ID = '%s';" % ws_ID
        num = dbManager.fetch(query=num_query)
        num1= num[0].num_of_people + 1
        update_num = "update group15.workshops set num_of_people='%s' where workshop_ID='%s';" %(num1,ws_ID)
        dbManager.commit(query=update_num)
        delete_query = "delete from group15.Registrations_workshops where email='%s' and ws_ID='%s';" %(email, ws_ID)
        dbManager.commit(query=delete_query)
        return



dbWorkshops = DBworkshops()