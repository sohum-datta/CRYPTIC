#encryption algo
##def satisfying(password):
##    cu=0
##    cl=0
##    cn=0
##    cp=0
##    if len(password)>=8:
##        for i in password:
##            if i.isupper():
##                cu+=1
##            elif i.islower():
##                cl+=1
##            elif i in "0123456789":
##                cn+=1
##            else:
##                cp+=1
##        if cu>=2 and cl>=2 and cn>=2 and cp>=2:
##            return password
##        else:
##            op=input("password is not strong enough, do you want to continue,yes/no")
##            if op=="yes":
##                return password
##            else:
##                return False
##    else:
##        print("password is less than 8 characters, reenter")
##








import datetime
def userid():
    username=input("Enter a suitable username:")
    return username
def passcode(username,password):
    
    
    today=datetime.date.today()
    now=datetime.datetime.now()
    ##key=satisfying(password)
    
    encryptedpassword=str(today)+password+str(now)
    import pickle
    f=open("mysqlpass.dat","rb")
    code=pickle.load(f)  
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd=code)
    c=mydb.cursor()
    mtoday=str(today)
    mnow=str(now)
    print(type(mtoday),type(mnow))
    lst=(username,encryptedpassword,mtoday,mnow)
    stmt1='insert into users values(%s,%s,%s,%s)'
    c.execute("USE cryptic;")
    c.execute(stmt1,lst)
    stmt2="CREATE TABLE "+username+" (website_or_service varchar(128),username varchar(64),password varchar(64))"
    c.execute(stmt2)
    #c.execute("CREATE TABLE {}(website_or_service varchar(128),username varchar(64),password varchar(64));".format(username))
    mydb.commit()
    print (True)
    return True    









##    else:
##        op=input("password is not strong enough, do you want to continue,yes/no")
##        if op=="yes":
##                
##            encryptedpassword=str(today)+password+str(now)
##            return encryptedpassword,today,now
            
##            recheck=input("enter password again")
##            cond=False
##            while cond==False:
##                if recheck==password:
##                    print("password has been set")
##                    cond=True
##                    return encryptedpassword
##                    
##                else:
##                    passcode(password)    
##                    
    
##cond=False
##while cond==False:
##    
##    username=""
##    password=""
##    username=userid(username)
##    password=passcode(password)
##    recheck=input("enter password again")
##    
##    if recheck==password:
##        print("password has been set")
##        #print (password)
##        cond=True
##    else:
##        passcode(password)


##password=input("Enter new password(min. 8 char):")
##username=input("Enter a suitable username:")
#
