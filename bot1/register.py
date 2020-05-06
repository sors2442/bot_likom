import pymysql.cursors


def register(y):
    connect = pymysql.connect(host='31.31.196.97',  # подключение к бд
                              user='u0536724_root',
                              password='poiuyt098765',
                              db='u0536724_bot',
                              )
    try:
        with connect.cursor() as cursor:
            tee1 = ("SELECT id FROM `register` WHERE id=%(u)s")
            tee2 = {'u': y}
            cursor.execute(tee1, tee2)
            res = cursor.fetchone()
            if res == None:
                tee3 = ("INSERT INTO `register`(id, status) VALUES (%(u)s, 'free')")
                tee4 = {"u": y}
                cursor.execute(tee3, tee4)
                connect.commit()
            else:
                return res
    finally:
        connect.close()