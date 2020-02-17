# tkinter_calc.py
# Calculate HRA as 10% of input Salary using tkinter GUI

from tkinter import *
from tkinter import messagebox as msg

def calculate():
      try:
         if (float(sal_entry.get()) <= 0):
            raise AssertionError
      
         hra  = 0.10 * float(sal_entry.get())  
         output_label.configure(text = 'HRA {:.2f}'.format(hra))
         
      except ValueError as e:
         msg.showerror('Salary Must be numeric', 'Salary must be numeric')
         sal_entry.focus()
         
      except AssertionError as e:
         msg.showerror('Salary can not be <= 0', 'Salary must be >=0')
         sal_entry.focus()
               
def reset():
      sal_entry.delete(0,END)    # clears the entry box
      output_label.configure(text = '')   # Erase the label text
      sal_entry.focus()          # Move the cursor to salary entry field
      
#----------------------------------------     
root = Tk()
root.title('10% HRA calculation from Salary')
root.geometry('600x400')

# Creating widgets 
message_label = Label(root,text='Enter Salary',font=('Arial', 14))
output_label = Label(root,text='', font=('Arial', 14))
sal_entry = Entry(root, font=('Arial', 14), width=6)

calc_button = Button(root,text='Calculate HRA', font=('Arial', 14), bg='Orange', fg='Black',command=calculate)
reset_button = Button(root,text='Clear', font=('Arial', 14), bg='Khaki', fg='Black', command=reset)
exit_button = Button(root,text='Exit', font=('Arial', 14), bg='Yellow', fg='Black', command=root.destroy)

# Placing widgets using grid manager
message_label.grid(row=0, column=0)
sal_entry.grid(row=0, column=1)
calc_button.grid(row=2, column=1)
reset_button.grid(row=2, column=2)
exit_button.grid(row=2, column=3)
output_label.grid(row=1, column=0, columnspan=3)

# Focus the mouse on salary entry
sal_entry.focus()

# mainloop
root.mainloop()