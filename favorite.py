import sqlite3

class Favorite:
    @staticmethod
    def add(train, user_id):
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "insert into favorite (train, user_id) values(?, ?)"
        values = [train, user_id]
        cursor.execute(sql, values)
        conn.commit()
        sql = "select account, email from user "
        result = conn.execute("select * from favorite")
        conn.commit()
        return result

    @staticmethod
    def delete(train, user_id):
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        print(train)
        print(user_id)
        sql = "delete from favorite WHERE train = ? AND user_id = ?"
        values = [train, user_id]
        result = cursor.execute(sql, values)
        conn.commit()
        print("??????:? " , result)
        return result

    @staticmethod
    def get(user_id):
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        # sql = "SELECT bus.busNumber, bus.busName from favorite left join bus on favorite.bus_number = bus.busNumber WHERE favorite.user_id = ?"
        sql = "SELECT train.trainid, train.trainstation from train Left join favorite on train.trainid = favorite.train where favorite.user_id = ?"
        values = [user_id]
        cursor.execute(sql, values)
        result = cursor.fetchall()
        conn.commit()
        return result
    
    @staticmethod
    def check(trainid):        
        conn = sqlite3.connect('user.sqlite')
        cursor = conn.cursor()
        sql = "SELECT EXISTS(SELECT 1 FROM train WHERE trainid = ?)"
        values = [trainid]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        conn.commit()
        return result
