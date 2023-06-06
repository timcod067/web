import sqlite3

class Data:
    @staticmethod
    def register(account, password, email):
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "insert into user (account, password, email) values(?, ?, ?)"
        values = [account, password, email]
        cursor.execute(sql, values)
        conn.commit()
        sql = "select account, email from user "
        result = cursor.execute(sql)
        conn.commit()
        return result

    @staticmethod
    def get():
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "select account, email from user "
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        return result
    
    @staticmethod
    def getUserData(account):
        print(account)
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "select * from user where (account = ?)"
        values = [account]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        print("??????:? " , result)
        conn.commit()
        return result
    
    @staticmethod
    def check(account):        
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "select password from user where (account = ?)"
        values = [account]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        # print(result.fetchall())
        conn.commit()
        return result
    
    @staticmethod
    def check_username_exit(account):
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "select exists (select account from user where account = ?)"
        values = [account]
        conn.execute (sql,values)
        result=cursor.fetchone()[0]
        conn.commit
        return bool (result)