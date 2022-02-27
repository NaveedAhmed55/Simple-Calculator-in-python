from _tkinter import*
from tkinter import END, Button, Tk
from tkinter.ttk import Entry


Calculator=Tk()
Calculator.title("Simple Calculator in Python")
index=0
index2=0
value1=0
value12=0
optr=""
#value method get each and keep track of them
def value(number):
    global index
    global value1
    index=index+1
    Entry1.insert(index,number)
    value1=Entry1.get()
#Addition Method
def addition():
    global value1
    global value12
    global optr
    value12=value1
    optr="+"
    value1=0
    Entry1.delete(0,END)
#Subraction Method   
def subtraction():
    global value1
    global value12
    global optr
    value12=value1
    optr="-"
    value1=0
    Entry1.delete(0,END)
#Multiplication Method    
def multiplication():
    global value1
    global value12
    value12=value1
    global optr
    optr="*"
    value1=0
    Entry1.delete(0,END)
#Division Method
def division():
    global value1
    global value12
    global optr
    value12=value1
    optr="/"
    value1=0
    Entry1.delete(0,END)

#Equal method gives result                   
def Equal():
    if(optr=="+"):
        value3=int(value1)+int(value12)
        Entry1.delete(0,END)
        Entry1.insert(0,value3)
    elif(optr=="-"):
        value3=int(value1)-int(value12)
        Entry1.delete(0,END)
        Entry1.insert(0,value3)
    elif(optr=="/"):
        value3=int(value1)/int(value12)
        Entry1.delete(0,END)
        Entry1.insert(0,value3)
    elif(optr=="*"):
        value3=int(value1)*int(value12)
        Entry1.delete(0,END)
        Entry1.insert(0,value3)
    else:
        "INVALID Operations" 
#Clear button erases all information in 
def Clear():
    global value1
    value1=0
    Entry1.delete(0,END)

Entry1=Entry(Calculator,width=60)
Entry1.grid(row=0,column=0,columnspan=4)

#All Buttons
button9=Button(Calculator,text="9",padx=35,pady=35,command=lambda:value(9))
button8=Button(Calculator,text="8",padx=35,pady=35,command=lambda:value(8))
button7=Button(Calculator,text="7",padx=35,pady=35,command=lambda:value(7))
button6=Button(Calculator,text="6",padx=35,pady=35,command=lambda:value(6))
button5=Button(Calculator,text="5",padx=35,pady=35,command=lambda:value(5))
button4=Button(Calculator,text="4",padx=35,pady=35,command=lambda:value(4))
button3=Button(Calculator,text="3",padx=35,pady=35,command=lambda:value(3))
button2=Button(Calculator,text="2",padx=35,pady=35,command=lambda:value(2))
button1=Button(Calculator,text="1",padx=35,pady=35,command=lambda:value(1))
button0=Button(Calculator,text="0",padx=35,pady=35,command=lambda:value(0))
buttonAddition=Button(Calculator,text="+",padx=35,pady=35,command=addition)
buttonSubtract=Button(Calculator,text="-",padx=35,pady=35,command=subtraction)
buttonMultiply=Button(Calculator,text="*",padx=35,pady=35,command=multiplication)
buttonDivision=Button(Calculator,text="/",padx=35,pady=35,command=division)
buttonEqual=Button(Calculator,text="=",padx=35,pady=35,command=Equal)
buttonClear=Button(Calculator,text="Clear",padx=26,pady=35,command=Clear)

#Position of each button using grid geometery
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
buttonMultiply.grid(row=1,column=3)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
buttonSubtract.grid(row=2,column=3)

button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
buttonAddition.grid(row=3,column=3)

button0.grid(row=4,column=0)
buttonDivision.grid(row=4,column=1)
buttonEqual.grid(row=4,column=2)
buttonClear.grid(row=4,column=3)

#Size of frame and mininum and maximum.
Calculator.geometry("370x400")
Calculator.minsize(370,400)
Calculator.maxsize(370,400)
Calculator.mainloop()
