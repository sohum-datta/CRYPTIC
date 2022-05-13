import mysql.connector
import pickle
password=input("enter the password to your mysql database")
mydb=mysql.connector.connect(host="localhost",user="root",passwd=password)
print (mydb.is_connected())
c=mydb.cursor()
c.execute("DROP DATABASE IF EXISTS cryptic")
c.execute("CREATE DATABASE cryptic;")
c.execute("USE cryptic;")
c.execute("DROP TABLE IF EXISTS users")
c.execute("CREATE TABLE users(username varchar(128),encrypted_password varchar(128),today varchar(128),now varchar(128));")
mydb.commit()

file="mysqlpass.dat"
def write(file,password):
    with open(file,'wb') as f:
        pickle.dump(password,f)
        f.close()
    print("success")
write(file,password)
exit()
