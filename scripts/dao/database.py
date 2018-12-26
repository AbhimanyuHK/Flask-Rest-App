import pymysql


class Database(object):

    """
    GET, INSERT, UPDATE, DELETE
    """

    def __init__(self):
        self.host = 'sql12.freemysqlhosting.net'
        self.user = 'sql12271532'
        self.password = 'HF6R2dbWuv'
        self.db = 'sql12271532'
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def get_by_id(self, id):
        try:
            self.cur.execute("select * from MyGuests where id = " + str(id))
            result = self.cur.fetchall()
            return result
        finally:
            self.cur.close()

    def get_all(self):
        try:
            self.cur.execute("select * from MyGuests")
            result = self.cur.fetchall()
            return result
        finally:
            self.cur.close()

    def insert(self, json):
        try:
            val = (json.get('firstname'), json.get('lastname'), json.get('email'))
            sql = "insert into MyGuests (firstname, lastname, email) values (%s, %s, %s)"
            self.cur.execute(sql, val)
            return self.cur.rownumber
        finally:
            self.con.commit()
            self.cur.close()

    def delete_by_id(self, id):
        try:
            sql_delete = "Delete from MyGuests where id = %s"
            count = self.cur.execute(sql_delete, id)
            return count
        finally:
            self.con.commit()
            self.cur.close()

    def update(self, id, json):
        try:
            sql = "update MyGuests set firstname = %s , lastname = %s , email = %s where id = %s"
            val = (json.get('firstname'), json.get('lastname'), json.get('email'), str(id))
            count = self.cur.execute(sql, val)
            return count
        finally:
            self.con.commit()
            self.cur.close()
