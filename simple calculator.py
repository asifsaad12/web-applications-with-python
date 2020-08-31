from tkinter import*
from tkinter import font as TkFont
import math


root=Tk()


root.title("my first app")
root.config(bg="#9EFB45")
e=Entry(root)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=25,ipadx=30,ipady=30)
helv36 = TkFont.Font(family='Arial', size=20, weight=TkFont.BOLD)



def click(number):
    value=e.get()
    e.delete(0,END)
    e.insert(0,str(value)+str(number))

    
def click_clear():
    e.delete(0,END)


def click_equal():

    value1=e.get()
    e.delete(0,END)
    if sign=='+':
        e.insert(0,float(num)+float(value1))
    elif sign=='-':
            e.insert(0,float(num)-float(value1))
    elif sign=='*':
        e.insert(0,float(num)*float(value1))
    elif sign=='/':
        e.insert(0,float(num)/float(value1))
    elif sign=='%':
        e.insert(0,float(num)%float(value1))







def click_add():
    value1=e.get()
    e.delete(0,END)
    global num
    num = str(value1)

    global sign
    sign='+'


def click_minus():
    value1=e.get()
    e.delete(0,END)
    global num
    num = str(value1)

    global sign
    sign='-'


def click_multiplication():
    value1=e.get()
    e.delete(0,END)
    global num
    num = str(value1)

    global sign
    sign='*'

def click_division():
    value1=e.get()
    e.delete(0,END)
    global num
    num = str(value1)

    global sign
    sign='/'


def click_remainder():
    value1=e.get()
    e.delete(0,END)
    global num
    num = str(value1)

    global sign
    sign='%'


def click_sqrt():
    value1=e.get()
    e.delete(0,END)
    e.insert(0,math.sqrt(float(value1)))
    

def click_inverse():
    value1=e.get()
    e.delete(0,END)
    e.insert(0,1/(float(value1)))



b1=Button(root,text='1', font=helv36,bg="#ACDDF4",padx=50,pady=20,command=lambda : click(1))
b2=Button(root,text='2', font=helv36,padx=50,bg="#ACDDF4",pady=20,command=lambda : click(2))
b3=Button(root,text='3',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(3))


b4=Button(root,text='4',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(4))
b5=Button(root,text='5',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(5))
b6=Button(root,text='6',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(6))



b7=Button(root,text='7',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(7))
b8=Button(root,text='8',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(8))
b9=Button(root,text='9',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(9))




b_clear=Button(root,text="Clear",font=helv36,padx=100,pady=20,bg="#ACDDF4",command=click_clear)
b_equal=Button(root,text='=',font=helv36,padx=47,pady=20,bg="#ACDDF4",command=click_equal)
b_add=Button(root,text='+',font=helv36,padx=47,pady=20,bg="#ACDDF4",command=click_add)


b_minus=Button(root,text='-',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=click_minus)
b_multiplication=Button(root,text='*',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=click_multiplication)
b_division=Button(root,text='/',font=helv36,padx=55,pady=20,bg="#ACDDF4",command=click_division)


b_remainder=Button(root,text='%',font=helv36,padx=47,pady=20,bg="#ACDDF4",command=click_remainder)
b0=Button(root,text='0',font=helv36,padx=50,pady=20,bg="#ACDDF4",command=lambda : click(0))



b_sqrt=Button(root,padx=30,pady=20,font=helv36,bg="#ACDDF4",text='root',command=click_sqrt)
b_point=Button(root,padx=53,pady=20,font=helv36,bg="#ACDDF4",text='.',command=lambda : click('.'))
b_inverse=Button(root,padx=35,pady=20,font=helv36,bg="#ACDDF4",text='1/x',command=click_inverse)




b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)


b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)


b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)


b_clear.grid(row=4,column=0,columnspan=2)
b0.grid(row=4,column=2)



b_minus.grid(row=6,column=0)
b_division.grid(row=6,column=1)
b_multiplication.grid(row=6,column=2)


b_remainder.grid(row=5,column=1)
b_add.grid(row=5,column=0)
b_equal.grid(row=5,column=2)


b_sqrt.grid(row=7,column=0)
b_point.grid(row=7,column=1)
b_inverse.grid(row=7,column=2)

root.mainloop()