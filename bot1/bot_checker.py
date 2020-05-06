from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import pymysql.cursors

def check(x):
    connection = pymysql.connect(
        host='31.31.196.97',
        user='u0536724_root',
        password='poiuyt098765',
        db='u0536724_free',
    )
    print("Соединение с БД "+str(connection)+" установлено")
# первая база
    with connection.cursor() as cursor:
        checker1 = ("SELECT user FROM `DemMix` WHERE user=%(u)s")
        checker2 = {'u': x}
        cursor.execute(checker1, checker2)
        results = cursor.fetchone()
        if results != None:
            for i in results: print(i)
            checker1 = ("SELECT password FROM `DemMix` WHERE user=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            results1 = cursor.fetchone()
            for ii in results1: print(ii)
            global a
            a='\n\n' + "Ник: "+ str(i) +"\nПароль: "+ str(ii) + "\nБаза: DemMix"
            print(str(a))
        else:
            print('ELSE')
            a=""
# вторая база
        checker3 = ("SELECT username FROM `Craftboard` WHERE username=%(u)s")
        checker4 = {'u': x}
        cursor.execute(checker3, checker4)
        results2 = cursor.fetchone()
        if results2 != None:
            for kk in results2: print(kk)
            checker3 = ("SELECT password FROM `Craftboard` WHERE username=%(u)s")
            checker4 = {'u': x}
            cursor.execute(checker3, checker4)
            results3 = cursor.fetchone()
            for mm in results3: print(mm)
            global b
            b='\n\n' + "Ник: "+ str(kk) +"\nПароль: "+ str(mm) + "\nБаза: Craftboard"
            print(str(b))
        else:
            print('ELSE2')
            b=""
# третья база
        checker5 = ("SELECT username FROM `Awyshion` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `Awyshion` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global c
            c='\n\n' + "Ник: "+ str(n) +"\nПароль: "+ str(h) + "\nБаза: Awyshion"
            print(str(c))
        else:
            print('ELSE3')
            c=""
# четвертая база
        checker5 = ("SELECT username FROM `EnixWorld` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `EnixWorld` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global d
            d = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: EnixWorld"
            print(str(d))
        else:
            print('ELSE4')
            d = ""
# пятая база
        checker5 = ("SELECT username FROM `EnixWorld2` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `EnixWorld2` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global e
            e = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: EnixWorld2"
            print(str(e))
        else:
            print('ELSE5')
            e = ""
# шестая база
        checker5 = ("SELECT username FROM `EnixWorld3` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `EnixWorld3` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global f
            f = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: EnixWorld3"
            print(str(f))
        else:
            print('ELSE6')
            f = ""
# седьмая база
        checker5 = ("SELECT username FROM `fireMC` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `fireMC` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global g
            g = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: fireMC"
            print(str(g))
        else:
            print('ELSE7')
            g = ""
# восьмая база
        checker5 = ("SELECT username FROM `MCNova` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `MCNova` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global j
            j = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: MCNova"
            print(str(j))
        else:
            print('ELSE8')
            j = ""
# девятая база
        checker5 = ("SELECT username FROM `Enot_io` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `Enot_io` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global k
            k = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: Enot_io"
            print(str(k))
        else:
            print('ELSE9')
            k = ""
# десятая база
        checker5 = ("SELECT name FROM `Maricraft` WHERE name=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `Maricraft` WHERE name=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global l
            l = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: Maricraft"
            print(str(l))
        else:
            print('ELSE10')
            l = ""
# 11 база
        checker5 = ("SELECT username FROM `BorkLand` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `BorkLand` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global m
            m = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: BorkLand"
            print(str(m))
        else:
            print('ELSE11')
            m = ""
# 12 база
        checker5 = ("SELECT username FROM `OpMine` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `OpMine` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global o
            o = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: OpMine"
            print(str(o))
        else:
            print('ELSE12')
            o = ""
# 13 база
        checker5 = ("SELECT username FROM `MCSurvi` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `MCSurvi` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global p
            p = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: MCSurvi"
            print(str(p))
        else:
            print('ELSE12')
            p = ""
# 14 база
        checker5 = ("SELECT username FROM `MineSerwer` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `MineSerwer` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global r
            r = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: MineSerwer"
            print(str(r))
        else:
            print('ELSE12')
            r = ""
# 15 база
        checker5 = ("SELECT username FROM `OzoneMC` WHERE username=%(u)s")
        checker6 = {'u': x}
        cursor.execute(checker5, checker6)
        results4 = cursor.fetchone()
        if results4 != None:
            for n in results4: print(n)
            checker5 = ("SELECT password FROM `OzoneMC` WHERE username=%(u)s")
            checker6 = {'u': x}
            cursor.execute(checker5, checker6)
            results5 = cursor.fetchone()
            for h in results5: print(h)
            global s
            s = '\n\n' + "Ник: " + str(n) + "\nПароль: " + str(h) + "\nБаза: OzoneMC"
            print(str(s))
        else:
            print('ELSE12')
            s = ""
    connection.close()

def statcheck(x): # проверка статуса
    connect = pymysql.connect(host='31.31.196.97',  # подключение к бд
                              user='u0536724_root',
                              password='poiuyt098765',
                              db='u0536724_free',
                              )
    try:
        with connect.cursor() as cursor:
            checker1 = ("SELECT status FROM `register` WHERE id=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            result = cursor.fetchone()
            global stat
            for stat in result: print(stat)
    except: print('ErrorCHECK')
    connect.close()

def statusupdatevip(x): # замена статуса vip
    connect = pymysql.connect(host='31.31.196.97',  # подключение к бд
                              user='u0536724_root',
                              password='poiuyt098765',
                              db='u0536724_free',
                              )
    try:
        with connect.cursor() as cursor:
            checker1 = ("UPDATE `register` SET status='vip'  WHERE id=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            connect.commit()
        with connect.cursor() as cursor:
            checker1 = ("SELECT status FROM `register` WHERE id=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            result = cursor.fetchone()
            for o in result: print(o)
    finally: connect.close()

def statusupdatefree(x): # замена статуса free
    connect = pymysql.connect(host='31.31.196.97',  # подключение к бд
                              user='u0536724_root',
                              password='poiuyt098765',
                              db='u0536724_free',
                              )
    try:
        with connect.cursor() as cursor:
            checker1 = ("UPDATE `register` SET status='free'  WHERE id=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            connect.commit()
        with connect.cursor() as cursor:
            checker1 = ("SELECT status FROM `register` WHERE id=%(u)s")
            checker2 = {'u': x}
            cursor.execute(checker1, checker2)
            result = cursor.fetchone()
            for o in result: print(o)
    finally: connect.close()

def register(y): # регистрация пользователя
    connect = pymysql.connect(host='31.31.196.97',  # подключение к бд
                              user='u0536724_root',
                              password='poiuyt098765',
                              db='u0536724_free',
                              )
    try:
        with connect.cursor() as cursor:
            checker1 = ("SELECT id FROM `register` WHERE id=%(u)s")
            checker2 = {'u': y}
            cursor.execute(checker1, checker2)
            res = cursor.fetchone()
            global name
            if res == None:
                user_get = vk.users.get(user_ids=(y))
                user_get = user_get[0]
                name = user_get['first_name']
                tee3 = ("INSERT INTO `register`(id, status, name) VALUES (%(u)s, 'free', %(y)s)")
                tee4 = {'u': y, 'y': name}
                cursor.execute(tee3, tee4)
                connect.commit()
            else: pass
            tee5 = ("SELECT status FROM `register` WHERE id=%(u)s")
            tee6 = {'u': y}
            cursor.execute(tee5, tee6)
            global status
            stratus = cursor.fetchone()
            for status in stratus: pass
            tee5 = ("SELECT name FROM `register` WHERE id=%(u)s")
            tee6 = {'u': y}
            cursor.execute(tee5, tee6)
            global first_name
            name1 = cursor.fetchone()
            for first_name in name1: pass

    finally:
        connect.close()

# подключение к боту
token='7b70fa96dc6db8ac22e8dcd202adf7c9343b0c601097d546f37701ac9afef23e0fab938e43097fcc6819b'
vk_session = vk_api.VkApi(token=token)
vk=vk_session.get_api()
longpoll=VkLongPoll(vk_session)

# начало работы
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Текст сообщения: ' + str(event.text))
            print('Сообщение пришло в: '+ str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print(event.user_id)
            print('------------------------')
            response = event.text.lower()
            if event.from_chat or event.from_user:
                try:
                    register(event.peer_id)
                    if response.split(' ')[0] == 'чек':
                        try:
                            if status == 'free': # бесплатные базы
                                check(response.split(' ')[1])
                                print('Excellent')
                                if a=="" and b=="" and c=="" and d=="" and e=="" and f=="" and g=="" and j==""\
                                        and k=="" and l=="" and m=="" and o=="" and p=="" and r=="" and s=="":
                                    vk.messages.send(  # отправка сообщения
                                        peer_id=event.peer_id,
                                        random_id=random.randint(-2147483648, +2147483648),
                                        message='Увы... Ничего не найдено.'
                                    )
                                else:
                                    vk.messages.send(  # отправка сообщения
                                        peer_id=event.peer_id,
                                        random_id=random.randint(-2147483648, +2147483648),
                                        message='\n' + str(first_name) + ", твой статус: " + str(status) +"\n\n" + 'Результаты Free чекера:' +  '\n' + str(a)
                                                + '\n' + str(b) +'\n' + str(c) + '\n' + str(d) + '\n' + str(e) + '\n' + str(f)
                                                + '\n' + str(g) + '\n' + str(j) + '\n' + str(k) + '\n' + str(l) + '\n' + str(m) + '\n' + str(o)
                                                + '\n' + str(p) + '\n' + str(r) + '\n' + str(s)
                                    )
                            elif status == 'vip' or status == 'VIP': # вип базы
                                check(response.split(' ')[1])
                                print('Excellent')
                                if a=="" and b=="" and c=="" and d=="" and e=="" and f=="" and g=="" and j==""\
                                        and k=="" and l=="" and m=="" and o=="" and p=="" and r=="" and s=="":
                                    vk.messages.send(  # отправка сообщения
                                        peer_id=event.peer_id,
                                        random_id=random.randint(-2147483648, +2147483648),
                                        message='Увы... Ничего не найдено.'
                                    )
                                else:
                                    vk.messages.send(  # отправка сообщения
                                        peer_id=event.peer_id,
                                        random_id=random.randint(-2147483648, +2147483648),
                                        message='\n' + str(first_name) + ", твой статус: " + str(
                                            status) + "\n\n" + 'Результаты Free чекера:' + '\n' + str(a)
                                                + '\n' + str(b) + '\n' + str(c) + '\n' + str(d) + '\n' + str(e) + '\n' + str(f)
                                                + '\n' + str(g) + '\n' + str(j) + '\n' + str(k) + '\n' + str(l) + '\n' + str(m) + '\n' + str(o)
                                                + '\n' + str(p) + '\n' + str(r) + '\n' + str(s)
                                    )
                        except:
                            vk.messages.send(  # отправка сообщения
                                peer_id=event.peer_id,
                                random_id=random.randint(-2147483648, +2147483648),
                                message='Неверная команда'
                            )
                            print('EXCEPT')
                    elif response.split(' ')[0] == 'дек':
                        vk.messages.send(  # отправка сообщения
                            peer_id=event.peer_id,
                            random_id=random.randint(-2147483648, +2147483648),
                            message="Дешифратор в разработке..."
                        )
                    elif response.split(' ')[0] == '/status':
                            statuscheck=response.split(' ')[1]
                            statcheck(statuscheck)
                            print('123123123123123')
                            vk.messages.send(  # отправка сообщения
                                peer_id=event.peer_id,
                                random_id=random.randint(-2147483648, +2147483648),
                                message='\n' + str(first_name) + ", твой статус: " + stat
                            )
                    elif response.split(' ')[0] == '/set_vip':
                        updatename = response.split(' ')[1]
                        statusupdatevip(updatename)
                        print('BRAVO!')
                        vk.messages.send(  # отправка сообщения
                            peer_id=event.peer_id,
                            random_id=random.randint(-2147483648, +2147483648),
                            message='Успешно! ' + first_name + ', твой статус' + ': vip'
                        )
                    elif response.split(' ')[0] == '/set_free':
                        updatename1 = response.split(' ')[1]
                        statusupdatefree(updatename1)
                        print('BRAVO!')
                        vk.messages.send(  # отправка сообщения
                            peer_id=event.peer_id,
                            random_id=random.randint(-2147483648, +2147483648),
                            message='Успешно! ' + first_name + ', твой статус' + ': free'
                        )
                except:
                    vk.messages.send(  # отправка сообщения
                        peer_id=event.peer_id,
                        random_id=random.randint(-2147483648, +2147483648),
                        message='Error'
                    )
                    print('Error')