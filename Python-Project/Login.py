from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from subprocess import call

def reg():
    call(["python","Register.py"])

def fp():
    call(["python","for.py"])

def Login():
    if uname.get()=="" or pswd.get()=="":
        messagebox.showerror("Error","all fields are required")
    
    else:
        conn=mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="sketch_users")
        cur=conn.cursor()
        cur.execute("select * from users where Username=%s and Password=%s ",(
                                                                                        uname.get(),
                                                                                        pswd.get()
                                                                                    ))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error!","Incorrect Username or Password")
        else:
            messagebox.showinfo("Success!","Loggedin sucessfully")
            call(["python","Menu.py"])
        conn.commit()
        conn.close()
 
login=Tk()
login.geometry("890x600")
login.config(background='#c3eb34')
login.title("Login")
bg=ImageTk.PhotoImage(file=r"D:\KARTHIK\Wallpapers and rocky and me\Wallpapers\richard-horvath-_nWaeTF6qo0-unsplash.jpg")
lbl_bg=Label(login,image=bg)
lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(login,text="Login",font=('times new roman','45','bold'),fg='blue')
label.pack()
label1=Label(login,text="Username:",font=('times new roman','20'),fg='blue')
label1.place(x=240,y=150)
label2=Label(login,text="Password:",font=('times new roman','20'),fg='blue')
label2.place(x=240,y=200)
uname=Entry(login,font=('times new roman',18) )
uname.place(x=370,y=150)
pswd=Entry(login,font=('times new roman',18), show="*" )
pswd.place(x=370,y=200)
button1=Button(login,text="Login",font=('times new roman',20),fg='green',command=Login)
button1.place(x=250,y=300,relwidth=0.20,relheight=0.1)
label1=Label(login,text="OR",font=('times new roman',12),bg='#c3eb34',fg='blue')
label1.place(x=300,y=370)
label2=Label(login,text="If you don't have an account ",font=('times new roman',16),fg='blue')
label2.place(x=190,y=400)
button2=Button(login,text="Register",font=('times new roman',20),fg='green',command=reg)
button2.place(x=250,y=450,relwidth=0.20,relheight=0.1)
forgotpass=Button(login,text="Forgot Password",font=('times new roman',20),fg='green',command=fp)
forgotpass.place(x=550,y=300,relwidth=0.30,relheight=0.1)



login.mainloop()




