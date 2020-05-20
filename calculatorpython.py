from tkinter import *

window = Tk()
window.title('Calculator Project')
window.geometry('350x370+250+200')
window.configure(background='#ACFA58')
window.resizable(width=False,height=False)

icon = PhotoImage(file='my_photo.png')
window.call('wm','iconphoto',window._w,icon)

my_input = StringVar()
my_operator = ""

def click_buttons(numbers):
	global my_operator
	my_operator += (str(numbers))
	my_input.set(my_operator)

def result_button():
	global my_operator
	result = str(eval(my_operator))
	my_input.set(result)
	my_operator = result

def Clear_button():
	global my_operator
	my_operator = ""
	my_input.set("")


textResult = Entry(window,width=25,font=('Times',16,'bold'),textvariable=my_input,bg='powder blue',bd=6,justify='right')
textResult.place(x=30,y=50)

btn7 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='7',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(7))
btn7.place(x=30,y=105)

btn8 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='8',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(8))
btn8.place(x=110,y=105)

btn9 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='9',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(9))
btn9.place(x=190,y=105)

btn4 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='4',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(4))
btn4.place(x=30,y=170)

btn5 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='5',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(5))
btn5.place(x=110,y=170)

btn6 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='6',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(6))
btn6.place(x=190,y=170)

btn1 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='1',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(1))
btn1.place(x=30,y=235)

btn2 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='2',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(2))
btn2.place(x=110,y=235)

btn3 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='3',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(3))
btn3.place(x=190,y=235)

btn0 = Button(window,padx=10,pady=2,width=4,height=2,font=('Times',12,'bold'),text='0',bd=4,bg='#CEECF5',
	fg='black',command=lambda:click_buttons(0))
btn0.place(x=250,y=305)

btnAddition = Button(window,padx=2,pady=2,font=('Times',10,'bold'),width=4,height=2,bg='orange',bd=2,text='+',command=lambda:click_buttons('+'))
btnAddition.place(x=270,y=110)

btnsubstract = Button(window,padx=2,pady=2,font=('Times',10,'bold'),width=4,height=2,bg='orange',bd=2,text='-',command=lambda:click_buttons('-'))
btnsubstract.place(x=270,y=155)

btnmultiply = Button(window,padx=2,pady=2,font=('Times',10,'bold'),width=4,height=2,bg='orange',bd=2,text='*',command=lambda:click_buttons('*'))
btnmultiply.place(x=270,y=200)

btndivision = Button(window,padx=2,pady=2,font=('Times',10,'bold'),width=4,height=2,bg='orange',bd=2,text='/',command=lambda:click_buttons('/'))
btndivision.place(x=270,y=245)

equalButton = Button(window,padx=4,pady=2,font=('Times',12,'bold'),width=10,height=2,bg='light blue',
	text='=',bd=2,fg='black',command=result_button)
equalButton.place(x=30,y=305)


clearButton = Button(window,padx=4,pady=2,font=('Times',12,'bold'),width=8,height=2,bg='light blue',
	text='C',bd=2,fg='black',command=Clear_button)
clearButton.place(x=150,y=305)



window.mainloop()