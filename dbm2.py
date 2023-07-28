import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="adduser",port=3306)

def insert(t):

    con=connect()
    cur=con.cursor()
    sql="insert into users(name,email,password) values(%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()

def select():

    con=connect()
    cur=con.cursor()
    sql="select email,password from users"
    cur.execute(sql)
    data=cur.fetchall()
    print(data)
    con.commit()
    con.close()
    return data

def update(t):

    con=connect()
    cur=con.cursor()
    sql="update users set name=%s,email=%s, password=%s where id=%s"
    cur.execute(sql,t)
    con.commit()
    con.close()


def delete(id):

    con=connect()
    cur=con.cursor()
    sql="delete from users where id=%s"
    cur.execute(sql,id)
    con.commit()
    con.close()


def select1():

    con=connect()
    cur=con.cursor()
    sql="select * from users"
    cur.execute(sql)
    data=cur.fetchall()
    print(data)
    con.commit()
    con.close()
    return data    







