def fetch(username):
    import mysql.connector
    import pickle
    f=open("mysqlpass.dat","rb")
    code=pickle.load(f)
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=code,database="cryptic")
    txt="select * from {};".format(username)
    c=mydb.cursor()
    c.execute(txt)
    record=c.fetchall()
    return record
