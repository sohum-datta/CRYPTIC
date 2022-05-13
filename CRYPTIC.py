import encryptinput
import decryptinput
import time
import datafetch
import add_data
import os

def enterbutton():
        global passwordentry
        global confirmpasswordentry
        global usernameentry
        global newtk
        global entrytk
        if passwordentry.get()==confirmpasswordentry.get():
            try:    
                    


                    encryptinput.passcode(usernameentry.get(),passwordentry.get())
                    
                    message=Label(newtk,text='Account Created!').place(x=500,y=600)
                    newtk.destroy()
                    main()
##                    entrytk=Tk()
##                    entrytk.title('Workspace')
##                    entrytk.minsize(1280,720)
##                    username=Label(entrytk,text='Enter Username').place(x=500,y=350)
##                    Password=Label(entrytk,text='Enter Password').place(x=500,y=380)
##                    ConfirmPassword=Label(entrytk,text='Confirm Password').place(x=500,y=410)
##                    usernameentry=Entry(entrytk)
##                    usernameentry.place(x=590,y=350)
##                    passwordentry=Entry(entrytk)
##                    passwordentry.place(x=590,y=380)
##                    confirmpasswordentry=Entry(entrytk)
##                    confirmpasswordentry.place(x=610,y=410)
                    
            except:
                    message=Label(newtk,text='Username has an issue , make sure it is following all rules!').place(x=500,y=550)
        else:
            message=Label(newtk,text='Passwords do not match!').place(x=500,y=440)

def Signin():#Function for Signin
    global passwordentry
    global confirmpasswordentry
    global usernameentry
    global newtk
    tk.destroy()
    newtk=Tk()
    newtk.title('Signin')
    newtk.minsize(1280,720)
    username=Label(newtk,text='Enter Username').place(x=500,y=350)
    Password=Label(newtk,text='Enter Password').place(x=500,y=380)
    ConfirmPassword=Label(newtk,text='Confirm Password').place(x=500,y=410)
    usernameentry=Entry(newtk)
    usernameentry.place(x=590,y=350)
    passwordentry=Entry(newtk)
    passwordentry.place(x=590,y=380)
    confirmpasswordentry=Entry(newtk)
    confirmpasswordentry.place(x=610,y=410)
    enter=Button(newtk,text="ENTER",bg="white",width=40,fg="black",font= "none 10",command=enterbutton).place(x=500,y=500)        
    rules=Label(newtk,text='RULES :\n1.No spaces in username \n2.Username should have alphabets\n3.If username satisfies both the conditions above then it already exists',font='none 12').place(x=400,y=200)                


                
        
                    
def Login():
        global loginusernameentry,loginpasswordentry
        global logintk
        global mpassword
        global name
        tk.destroy()
        logintk=Tk()
        logintk.title('Login')
        logintk.minsize(1280,720)
        username=Label(logintk,text='Enter Username').place(x=500,y=350)
        Password=Label(logintk,text='Enter Password').place(x=500,y=380)
        loginusernameentry=Entry(logintk)
        loginusernameentry.place(x=590,y=350)
        loginpasswordentry=Entry(logintk)
        loginpasswordentry.place(x=590,y=380)
        #message=Label(logintk,text='Click CHECK then click ENTER').place(x=500,y=400)
        enter=Button(logintk,text="ENTER",bg="white",width=40,fg="black",font= "none 10",command=Workspace).place(x=500,y=500)
        #check=Button(logintk,text="CHECK",bg="white",width=40,fg="black",font= "none 10",command=Checkin).place(x=500,y=450)

def Checkin():
        global actualname,actualpassword
        
        name=loginusernameentry.get()
        mpassword=loginpasswordentry.get()
        actualname=str(name)
        actualpassword=str(mpassword)
        f1=open('name.txt','w')
        f1.write(name)
        f2=open('password.txt','w')
        f2.write(mpassword)
        f1.close()
        f2.close()
##        message=Label(logintk,text='Checked!').place(x=500,y=200)
        
def Workspace():
        global loginusernameentry,loginpasswordentry
        global table
        global workspaceusernameentry,workspacepasswordentry
        global websiteserviceentry
        global workspacetk
        global actualname,actualpassword
        try:
                Checkin()
                f1=open('name.txt','r')
                actualname=f1.read()
                f2=open('password.txt','r')
                actualpassword=f2.read()
                f1.close()
                f2.close()
        except:
                pass
        if decryptinput.passcode(actualname,actualpassword)==True:
                try:
                        logintk.destroy()
                        workspacetk=Tk()
                        workspacetk.title(actualname)
                        workspacetk.minsize(1280,720)
                        websiteservice=Label(workspacetk,text='Enter Website').place(x=500,y=320)
                        workspaceusername=Label(workspacetk,text='Enter Username').place(x=500,y=350)
                        workspacepassword=Label(workspacetk,text='Enter Password').place(x=500,y=380)
                        workspaceusernameentry=Entry(workspacetk)
                        websiteserviceentry=Entry(workspacetk)
                        websiteserviceentry.place(x=590,y=320)
                        workspaceusernameentry.place(x=590,y=350)
                        workspacepasswordentry=Entry(workspacetk)
                        workspacepasswordentry.place(x=590,y=380)
                        adata=Button(workspacetk,text="ADD DATA",bg="white",width=40,fg="black",font= "none 10",command=addata).place(x=500,y=450)
                        exitbutton=Button(workspacetk,text="EXIT",bg="white",width=40,fg="black",font= "none 10",command=exits).place(x=500,y=500)
                        table=Tk()
                        table.title('Your accounts!')
                        lst=datafetch.fetch(actualname)
                        
                        
                        try:
                                total_rows=len(lst)
                                total_columns=len(lst[0])
                                header1=Label(table,text='\tWebsite')
                                header1.grid(row=0,column=0)
                                header2=Label(table,text='Username     ')
                                header2.grid(row=0,column=1)
                                header3=Label(table,text='Password\t')
                                header3.grid(row=0,column=2)
                                for i in range(total_rows):
                                        for j in range(total_columns):
                                                label=Label(table,text=lst[i][j])
                                                label.grid(row=i+1,column=j)
                        except:
                                pass

                except:
                        workspacetk=Tk()
                        workspacetk.title(actualname)
                        workspacetk.minsize(1280,720)
                        websiteservice=Label(workspacetk,text='Enter Website/service').place(x=500,y=320)
                        workspaceusername=Label(workspacetk,text='Enter Username').place(x=500,y=350)
                        workspacepassword=Label(workspacetk,text='Enter Password').place(x=500,y=380)
                        workspaceusernameentry=Entry(workspacetk)
                        websiteserviceentry=Entry(workspacetk)
                        websiteserviceentry.place(x=590,y=320)
                        workspaceusernameentry.place(x=590,y=350)
                        workspacepasswordentry=Entry(workspacetk)
                        workspacepasswordentry.place(x=590,y=380)
                        adata=Button(workspacetk,text="ADD DATA",bg="white",width=40,fg="black",font= "none 10",command=addata).place(x=500,y=450)
                        exitbutton=Button(workspacetk,text="EXIT",bg="white",width=40,fg="black",font= "none 10",command=exits).place(x=500,y=500)
                        table=Tk()
                        table.title('Your accounts!')
                        lst=datafetch.fetch(actualname)
                        
                        try:
                                total_rows=len(lst)
                                total_columns=len(lst[0])
                                header1=Label(table,text='\tWebsite Service     ')
                                header1.grid(row=0,column=0)
                                header2=Label(table,text='Username     ')
                                header2.grid(row=0,column=1)
                                header3=Label(table,text='Password\t')
                                header3.grid(row=0,column=2)
                                
                                for i in range(total_rows):
                                        for j in range(total_columns):
                                                label=Label(table,text=lst[i][j])
                                                label.grid(row=i+1,column=j)
                        except:
                                pass
        else:
                message=Label(logintk,text='Username and Password do not match!').place(x=500,y=440)
        

def exits():
        os.remove('name.txt')
        os.remove('password.txt')
        exit()
def addata():
        global websiteserviceentry
        global table
        global loginusernameentry,loginpasswordentry
        global workspaceusernameentry,workspacepasswordentry
        global workspacetk
        global actualname,actualpassword
        f1=open('name.txt','r')
        actualname=f1.read()
        f1.close()
        website=websiteserviceentry.get()
        username=workspaceusernameentry.get()
        password=workspacepasswordentry.get()
        try:
                table.destroy()
        except:
                pass
        add_data.add(actualname,website,username,password)
        workspacetk.destroy()
        Workspace()
        
from tkinter import *
#Main Tkinter
def main():
        global tk
        tk=Tk()
        tk.title('CRYPTIC')
        tk.minsize(1280,720)
        signin=Button(tk,text="SIGN IN",bg="white",width=40,fg="black",font= "none 10",command=Signin).place(x=500,y=350)
        login=Button(tk,text="LOG IN",bg="white",width=40,fg="black",font= "none 10",command=Login).place(x=500,y=300)
main()
