def passcode(username,pass_word):
    import mysql.connector
    import pickle
    f=open("mysqlpass.dat","rb")
    code=pickle.load(f)
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=code,database="cryptic")
    c=mydb.cursor()
    c.execute("select * from users;")
    record = c.fetchall()
    for row in record:
        if str(row[0])==str(username):
            enc=row[1]
            today=row[2]
            now=row[3]
            new_enc=today+pass_word+now
            if new_enc==enc:
                return True
    else:
        return False
