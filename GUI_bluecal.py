#
# This program creates a GUI 
# calculator using Tkinter
# Original project: https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/
#
#
#Author : Faith Verus 
#Date : November 4, 2022



#import Tkinter 
from tkinter import *

#decleare expression variable globally 
expression = ''


#function that updates expression 
def press(num):
    global expression 
    
    #concatenate string 
    expression = expression +str(num)
    
    #update the expression using set method 
    equation.set(expression)
    
#function that evalutes final expression 
def equalpress():
    
    try:
        
        global expression 
        
        total = str(eval(expression))
        
        equation.set(total)
        
        expression = ''
        
        #if an error occurs , this 
        #this exception will handle it 
    except:
        
        equation.set("error")
        expression = ''
        
#function will clear text entry box 
def clear():
    global expression 
    expression = ''
    equation.set('')
    
    
#driver code 
if __name__ == '__main__':
    #GUI window 
    gui = Tk()
    
    #set background color of GUI
    gui.configure(background='blue')
    
    #title of GUI window 
    gui.title('Blue Calculator')
    
    #Configure the GUI window 
    gui.geometry('270x150')
    
    equation = StringVar()
    
    #create text entry box for showing 
    #expression 
    expression_field = Entry(gui,textvariable=equation)
    
    #Set grid method 
    expression_field.grid(columnspan=4, ipadx=70)
    
    button1 = Button(gui, text=' 1 ', fg='black', bg='yellow',
					command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='yellow',
					command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='yellow',
					command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='yellow',
					command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='yellow',
					command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='yellow',
					command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='yellow',
					command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='yellow',
					command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='yellow',
					command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='yellow',
					command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='yellow',
				command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='yellow',
				command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='yellow',
	 				command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='yellow',
	 				command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='yellow',
				command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='yellow',
				command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal= Button(gui, text='.', fg='black', bg='yellow',
					command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
	# start the GUI
    gui.mainloop()