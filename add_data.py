def add(username,website,newname,password):
    import mysql.connector
    import pickle
    f=open("mysqlpass.dat","rb")
    code=pickle.load(f)
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=code,database="cryptic")
    c=mydb.cursor()
    txt="insert into {} values('{}','{}','{}');".format(username,website,newname,password)
    c.execute(txt)
    mydb.commit()
    
