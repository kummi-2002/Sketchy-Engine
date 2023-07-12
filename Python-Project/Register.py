from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from subprocess import call

def rg():
    if fname.get()=="" or lname.get()=="" or uname.get()=="" or age.get()=="" or pno.get()=="" or secans.get()=="" or pas.get()=="" or conpas.get()=="" or secsel.get()=="select" : 
            messagebox.showerror("Error","all fields are required")
    elif pas.get()!=conpas.get():
            messagebox.showerror("Error", "Password does not match")
    else:
        Firstname=fname.get()
        Lastname=lname.get()
        Username=uname.get()
        age_=age.get()
        Phone_number=pno.get()
        Security_Question=secsel.get()
        Security_Answer=secans.get()
        password=pas.get()
        Confirm_password=conpas.get()
        conn= mysql.connector.connect(host="localhost",user="root",port="3306",password="",database="sketch_users")
        my_cursor=conn.cursor()
        query=("select * from users where Username=%s")
        value=(uname.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()
        if row!=None:
            messagebox.showerror("Error","User already exist!")
        else:
            q1="insert into users(Firstname,Lastname,Username,Age,Phone_number,Security_Question,Security_Answer,Password,Confirm_Password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            v1=(Firstname,Lastname,Username,age_,Phone_number,Security_Question,Security_Answer,password,Confirm_password) 
            my_cursor.execute(q1,v1)                       
        conn.commit()
        conn.close()
        messagebox.showinfo("Success!","Sucessfully Registered")


        


def log_return():
    call(["python","main.py"])

       

register=Tk()
register.geometry("990x700")
register.title("Register")
bg=ImageTk.PhotoImage(file=r"D:\KARTHIK\Wallpapers and rocky and me\Wallpapers\richard-horvath-_nWaeTF6qo0-unsplash.jpg")
lbl_bg=Label(register,image=bg)
lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(register,text="Register",font=('times new roman',45,'bold'),fg='green')
label.pack()
label1=Label(register,text="Firstname:",font=('times new roman','20'),fg='blue')
label1.place(x=240,y=150)
label2=Label(register,text="Lastname:",font=('times new roman','20'),fg='blue')
label2.place(x=240,y=200)
label3=Label(register,text="Username:",font=('times new roman','20'),fg='blue')
label3.place(x=240,y=250)
label4=Label(register,text="Age:",font=('times new roman','20'),fg='blue')
label4.place(x=240,y=300)
label5=Label(register,text="Phone no:",font=('times new roman','20'),fg='blue')
label5.place(x=240,y=350)
label6=Label(register,text="Security Question:",font=('times new roman','20'),fg='blue')
label6.place(x=40,y=400)
label7=Label(register,text="Security Answer:",font=('times new roman','20'),fg='blue')
label7.place(x=510,y=400)
label8=Label(register,text="Password:",font=('times new roman','20'),fg='blue')
label8.place(x=40,y=450)
label9=Label(register,text="Confirm Password:",font=('times new roman','20'),fg='blue')
label9.place(x=480,y=450)
fname=Entry(register,font=('times new roman',18) )
fname.place(x=370,y=150)
lname=Entry(register,font=('times new roman',18) )
lname.place(x=370,y=200)
uname=Entry(register,font=('times new roman',18) )
uname.place(x=370,y=250)
age=Entry(register,font=('times new roman',18) )
age.place(x=370,y=300)
pno=Entry(register,font=('times new roman',18))
pno.place(x=370,y=350)
secans=Entry(register,font=('times new roman',18) )
secans.place(x=710,y=400)
pas=Entry(register,font=('times new roman',18) )
pas.place(x=180,y=450)
conpas=Entry(register,font=('times new roman',18), show="*" )
conpas.place(x=710,y=450)
regbtn=Button(register,text="Register",font=('times new roman',30,'bold'),fg='green',command=rg)
regbtn.place(x=400,y=520,relwidth=0.20,relheight=0.1)
logbtn=Button(register,text="Login",font=('times new roman',30,'bold'),fg='green',command=log_return)
logbtn.place(x=670,y=520,relwidth=0.20,relheight=0.1)
secsel=ttk.Combobox(register,font=('times new roman',18),state="readonly")
secsel["values"]=("select","Your birth place?","Your first school?","Your favorite food?")
secsel.place(x=250,y=402,height=32,width=260)
secsel.current(0)

register.mainloop()