from tkinter import *
window=Tk()
window.title("widget")
window.geometry("400x400")
l1=Label(text="Getting started with widgets",fg="white",bg="blue",height=1,width=400)

# from PIL import Image, ImageTk
# lab_img=Image.open("images.jpg")
# img1=ImageTk.PhotoImage(lab_img)
# label=Label(window, image=img1,height=200,width=300)


l2=Label(text="Enter number 1",fg="black",bg="light green")
e1=Entry()
l3=Label(text="Enter number 2",fg="black",bg="light green")
f1=Entry()

def display():
    name=int(e1.get())
    nam=int(f1.get())
    global msg
    multi=name*nam
    msg="Product"+"="+str(multi)
    tb.insert(END,msg)

tb=Text(height=100)
tbb=Text(height=100)
b=Button(text="click",command=display,height=1)
c=Button(text="click",command=display,height=1)

l1.pack()
l2.pack()
e1.pack()
l3.pack()
c.pack()
f1.pack()
tb.pack()
tbb.pack()

window.mainloop()