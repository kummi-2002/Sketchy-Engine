from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
from subprocess import call

menu=Tk()
menu.geometry("890x600")
menu.config(background='#c3eb34')
menu.title("Menu")
bg=ImageTk.PhotoImage(file=r"D:\KARTHIK\Wallpapers and rocky and me\Wallpapers\richard-horvath-_nWaeTF6qo0-unsplash.jpg")
lbl_bg=Label(menu,image=bg)
lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(menu,text="Menu",font=('times new roman','45','bold'),fg='blue')
label.pack()
def aircanvas():
    call(["python","Air-canvas.py"])
def Sketchy():
    call(["python","Sketch.py"])
button1=Button(menu,text="Air canvas",font=('times new roman',20),fg='green',command=aircanvas)
button1.place(x=350,y=300,relwidth=0.20,relheight=0.1)
label1=Label(menu,text="OR",font=('times new roman',12),bg='#c3eb34',fg='blue')
label1.place(x=425,y=370)
label2=Label(menu,text="If you want to convert an image to a pencil sketch ",font=('times new roman',16),fg='blue')
label2.place(x=225,y=400)
button2=Button(menu,text="Sketchy",font=('times new roman',20),fg='green',command=Sketchy)
button2.place(x=350,y=450,relwidth=0.20,relheight=0.1)


menu.mainloop()
