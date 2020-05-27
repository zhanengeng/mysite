import pymysql


class MysqlHelper:
    """传参（字符串）：(db, user, pw [,host, port, charset])。
    返回对象，具有insert(增)，delete，update(改)，get_all(查)方法 """
    def __init__(self, db, user, password, host="localhost", port=3306, charset="utf8"):
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.user = user
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, db=self.db, user=self.user,
 password=self.password, port=self.port, charset=self.charset)

        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def __cud(self, sql, params=[]):
        """增，改，删"""
        try:
            self.connect()
            self.cur.execute(sql, params)
            self.conn.commit()
            self.close()
            print("ok")

        except Exception as e:
            print(e)
            self.conn.rollback()

    def get_all(self, sql, params=[]):
        """search method, return as tuple"""
        try:
            self.connect()
            self.cur.execute(sql, params)
            result = self.cur.fetchall()
            self.close()

            return result

        except Exception as e:
            print(e)
            self.conn.rollback()

    def update(self, sql, params=[]):
        """改"""
        return self.__cud(sql, params)

    def insert(self, sql, params=[]):
        """增"""
        return self.__cud(sql, params)

    def delete(self, sql, params=[]):
        """删"""
        return self.__cud(sql, params)
