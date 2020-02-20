# tkinter_calc.py
# Calculate HRA as 10% of input Salary using tkinter GUI

from tkinter import *
from tkinter import messagebox as msg

def calculate():
      try:
         principal=float(Principal.get())
         rate=float(Rate.get())
         years=float(Years.get())
         if ( principal<= 0 or rate<= 0 or years<=0):
            raise AssertionError
      
         amount = principal*rate*years/100 + principal
         output_label.configure(text = 'Amount {:.2f}'.format(amount))
         
      except ValueError as e:
         msg.showerror('Must be numeric', 'Must be numeric')
         Principal.focus()
         
      except AssertionError as e:
         if principal<= 0:
            msg.showerror('Principal cannot be <=0', 'Principal must be >0')
         if rate<=0:
            msg.showerror('Rate cannot be <=0', 'Rate must be >0')
         if years<=0:
            msg.showerror('Years cannot be <=0', 'Years must be >0')
         Principal.focus()
               
def reset():
      Principal.delete(0,END)    # clears the entry box
      Rate.delete(0,END)    # clears the entry box
      Years.delete(0,END)    # clears the entry box

      output_label.configure(text = '')   # Erase the label text
      Principal.focus()          # Move the cursor to salary entry field

      
#----------------------------------------     
root = Tk()
root.title('Amount from Principal')
root.geometry('600x400')

# Creating widgets 
Principal_Label = Label(root,text='Enter Principal',font=('Arial', 14))
Principal = Entry(root, font=('Arial', 14), width=6)

Rate_Label = Label(root,text='Enter rate',font=('Arial', 14))
Rate = Entry(root, font=('Arial', 14), width=6)

Years_Label = Label(root,text='Enter years',font=('Arial', 14))
Years = Entry(root, font=('Arial', 14), width=6)

output_label = Label(root,text='', font=('Arial', 14))

calc_button = Button(root,text='Calculate HRA', font=('Arial', 14), bg='Orange', fg='Black',command=calculate)
reset_button = Button(root,text='Clear', font=('Arial', 14), bg='Khaki', fg='Black', command=reset)
exit_button = Button(root,text='Exit', font=('Arial', 14), bg='Yellow', fg='Black', command=root.destroy)

# Placing widgets using grid manager
Principal_Label.grid(row=0, column=1)
Principal.grid(row=0, column=2)

Rate_Label.grid(row=1, column=1)
Rate.grid(row=1, column=2)

Years_Label.grid(row=2, column=1)
Years.grid(row=2, column=2)
# Years.place(x=50,y=50)

calc_button.place(x=100,y=100)
reset_button.place(x=250,y=100)
exit_button.place(x=330,y=100)
output_label.grid(row=6, column=0, columnspan=3)

# Focus the mouse on salary entry
Principal.focus()

# mainloop
root.mainloop()