from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import messagebox
import cv2
import os


def openFile():
    global filepathh
    fp = filedialog.askopenfilename(initialdir="D:\\SEM 5 NHCE\\Python-Project",
                                          title="Select an Image",
                                          filetypes= (("JPG files","*.jpg"),
                                          ("all files","*.*")))
    
    #filepathh=fp
    #print(filepathh)
    #filepathh= os.path.abspath(fp)
    filepathh= fp
    #print(type(fp))
    #return fp
    #file = open(filepath,'r')
    #my_label=label(Sketcher, text=Sketcher.filepath).pack()
   # my_image=ImageTk.PhotoImage(Image.open(Sketcher.filepath))
   # my_image_label=label(image=my_image).pack()
    #filepathh=text(filepath)
    
    
    
def Draw():
    image = cv2.imread(filepathh)
    grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert,(21,21),0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)
    cv2.imwrite("sketch.png",sketch)
    cv2.imshow("oldimage",image)
    cv2.waitKey(0)
    cv2.imshow("sketch.png",sketch)


Sketcher=Tk()
Sketcher.geometry("890x600")
Sketcher.config(background='#c3eb34')
Sketcher.title("Sketchy")
bg=ImageTk.PhotoImage(file=r"D:\\KARTHIK\Wallpapers and rocky and me\Wallpapers\\richard-horvath-_nWaeTF6qo0-unsplash.jpg")
lbl_bg=Label(Sketcher,image=bg)
lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
label=Label(Sketcher,text="Sketchy",font=('times new roman','45','bold'),fg='blue')
label.pack()
button1=Button(Sketcher,text="Select",font=('times new roman',20),fg='green',command=openFile)
button1.place(x=350,y=300,relwidth=0.20,relheight=0.1)
button2=Button(Sketcher,text="Convert",font=('times new roman',20),fg='green',command=Draw) 
button2.place(x=350,y=450,relwidth=0.20,relheight=0.1)
Sketcher.mainloop()