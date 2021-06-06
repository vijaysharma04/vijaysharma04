
import abc
from tkinter import *

root = Tk()
root.title('my calculator')
root.geometry("250x400")

def click(event):
    text = event.widget.cget('text')
    print(text)
    if text == '=':
        if btntxt.get().isdigit():
            value = int(btntxt.get())
        else:
            value = eval(btntxt.get())
        
        btntxt.set(value)
        screen.update()
    
    elif text == 'C':
        btntxt.set('')
        screen.update()
    
    else:
        btntxt.set(btntxt.get() + text)
        screen.update()
    
    
    
    



btntxt = StringVar()
btntxt.set('')

screen = Entry(root,font=('verdana',22),textvariable=btntxt).pack(expand=True,fill=BOTH)

l1 = Label(root)
l1.pack(fill='both',expand=True)

bt1 = Button(l1,
text='1',
relief=GROOVE,
border='0',
font=('VERDANA',22))
bt1.pack(side=LEFT,expand=True,fill='both')
bt1.bind('<Button-1>',click)

bt2n= Button(l1,
text='2',
relief=GROOVE,
border='0',
font=('VERDANA',22))
bt2n.pack(side=LEFT,expand=True,fill='both')
bt2n.bind("<Button-1>",click)

btn3 = Button(l1,
text='3',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn3.pack(side=LEFT,expand=True,fill='both')
btn3.bind('<Button-1>',click)

btn4 = Button(l1,
text='+',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn4.pack(side=LEFT,expand=True,fill='both')
btn4.bind('<Button-1>',click)

l2 = Label(root)
l2.pack(fill=BOTH,expand=True)

btn5 = Button(l2,
text='4',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn5.pack(side=LEFT,expand=True,fill='both')
btn5.bind("<Button-1>",click)

btn6 = Button(l2,
text='5',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn6.pack(side=LEFT,expand=True,fill='both')
btn6.bind("<Button-1>",click)

btn7 = Button(l2,
text='6',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn7.pack(side=LEFT,expand=True,fill='both')
btn7.bind("<Button-1>",click)

btn8 = Button(l2,
text='-',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn8.pack(side=LEFT,expand=True,fill='both')
btn8.bind("<Button-1>",click)

l3 = Label(root)
l3.pack(fill=BOTH,expand=True)

btn10 = Button(l3,
text='7',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn10.pack(side=LEFT,expand=True,fill='both')
btn10.bind("<Button-1>",click)

btn10 = Button(l3,
text='8',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn10.pack(side=LEFT,expand=True,fill='both')
btn10.bind("<Button-1>",click)

btn11 = Button(l3,
text='9',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn11.pack(side=LEFT,expand=True,fill='both')
btn11.bind("<Button-1>",click)

btn12 = Button(l3,
text='*',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn12.pack(side=LEFT,expand=True,fill='both')
btn12.bind("<Button-1>",click)

l4 = Label(root)
l4.pack(fill=BOTH,expand=True)


btn13 = Button(l4,
text='C',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn13.pack(side=LEFT,expand=True,fill='both')
btn13.bind("<Button-1>",click)

btn14 = Button(l4,
text='0',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn14.pack(side=LEFT,expand=True,fill='both')
btn14.bind("<Button-1>",click)

btn15 = Button(l4,
text='=',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn15.pack(side=LEFT,expand=True,fill='both')
btn15.bind("<Button-1>",click)

btn16 = Button(l4,
text='/',
relief=GROOVE,
border='0',
font=('VERDANA',22))
btn16.pack(side=LEFT,expand=True,fill='both')
btn16.bind("<Button-1>",click)


root.mainloop()