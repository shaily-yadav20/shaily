from tkinter import *
from tkinter import messagebox


root=Tk()
root.geometry("600x600")
root.title("CALCULTOR")
root.configure(bg="beige")

label=Label(root,text="CALCULATOR",font=("Arial Bold",30))
label.config(bg="yellow",fg="black")
label.pack()                                           


myframe=LabelFrame(root,text="",font=("arial",20,"bold"))
mydisplay=Entry(root,width=35,borderwidth=5)
mydisplay.pack()

#button functions
def one():
    n=1
    mydisplay.insert(10,'1')
    return n
def two():
    n=2
    mydisplay.insert(10,'2')
    return n
SNIdef three():
    n=3
    mydisplay.insert(10,'3')
    return n
def four():
    n=4
    mydisplay.insert(10,'4')
    return n
def five():
    n=5
    mydisplay.insert(10,'5')
    return n
def six():
    n=6
    mydisplay.insert(10,'6')
    return n
def seven():
    n=7
    mydisplay.insert(10,'7')
    return n
def eight():
    n=8
    mydisplay.insert(10,'8')
    return n
def nine():
    n=9
    mydisplay.insert(10,'9')
    return n
def zero():
    n=0
    mydisplay.insert(10,'0')
    return n
def plus():
    mydisplay.insert(10,"+")
    return "+"
def minus():
    mydisplay.insert(10,"-")
    return "-"
def mult():
    mydisplay.insert(10,"*")
    return "*"
def divide():
    mydisplay.insert(10,"/")
    return "/"
def clear():
    mydisplay.delete(0,END)
def result():
    r=eval(mydisplay.get())
    mydisplay.delete(0,END)
    mydisplay.insert(10,r)
    
mybutton1=Button(myframe,text="9",width=6,height=3,command=nine,bg="seashell3")
mybutton1.grid(row=1,column=1)
mybutton2=Button(myframe,text="8",width=6,height=3,command=eight,bg="PeachPuff2")
mybutton2.grid(row=1,column=2)
mybutton3=Button(myframe,text="7",width=6,height=3,command=seven,bg="seashell3")
mybutton3.grid(row=1,column=3)
mybutton4=Button(myframe,text="6",width=6,height=3,command=six,bg="PeachPuff2")
mybutton4.grid(row=2,column=1)
mybutton5=Button(myframe,text="5",width=6,height=3,command=five,bg="seashell3")
mybutton5.grid(row=2,column=2)
mybutton6=Button(myframe,text="4",width=6,height=3,command=four,bg="PeachPuff2")
mybutton6.grid(row=2,column=3)
mybutton7=Button(myframe,text="3",width=6,height=3,command=three,bg="seashell3")
mybutton7.grid(row=3,column=1)
mybutton8=Button(myframe,text="2",width=6,height=3,command=two,bg="PeachPuff2")
mybutton8.grid(row=3,column=2)
mybutton9=Button(myframe,text="1",width=6,height=3,command=one,bg="seashell3")
mybutton9.grid(row=3,column=3)
mybutton10=Button(myframe,text="0",width=6,height=3,command=zero,bg="PeachPuff2")
mybutton10.grid(row=4,column=1)
mybutton11=Button(myframe,text="CL",width=6,height=3,command=clear,bg="seashell3")
mybutton11.grid(row=4,column=2)
mybutton12=Button(myframe,text="=",width=6,height=3,command=result,bg="PeachPuff2")
mybutton12.grid(row=4,column=3)

mybutton13=Button(myframe,text="/",width=6,height=3,command=divide,bg="seashell3")
mybutton13.grid(row=4,column=4)
mybutton14=Button(myframe,text="+",width=6,height=3,command=plus,bg="PeachPuff2")
mybutton14.grid(row=3,column=4)
mybutton15=Button(myframe,text="-",width=6,height=3,command=minus,bg="seashell3")
mybutton15.grid(row=2,column=4)
mybutton16=Button(myframe,text="*",width=6,height=3,command=mult,bg="PeachPuff2")
mybutton16.grid(row=1,column=4)


myframe.pack()
root.mainloop()
