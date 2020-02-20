# age_calc_from_dob_gui.py
# Testing Tkinter features with Python
# calculating age from DOB

from tkinter  import *
from tkinter  import messagebox as msg
from datetime import datetime, date

class GetAge:
      # Constructor
      def __init__(self, root1):
          self.f = Frame(root1, height=350, width=500)
          self.f.pack()    # Place the frame on root1 window
          # Creating label and Entry widgets
          self.message_label = Label(self.f,text='Enter your DOB (dd/mm/yyyy) :',font=('Arial', 14))
          self.output_label = Label(self.f,text='', font=('Arial', 14))
          self.age = Entry(self.f, font=('Arial', 14), width=12)
          self.age.bind('<Return>', self.calc_age) # Hit Enter key to call 'calculate' func
          # Creating button widgets
          self.calc_button = Button(self.f,text='Get Age', font=('Arial', 14), bg='Orange', fg='Black', command=self.calc_age)
          self.reset_button = Button(self.f,text='Clear', font=('Arial', 14), bg='Brown', fg='Black', command=self.reset)
          self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow', fg='Black', command=root1.destroy)

          # Placing the widgets using grid manager
          self.message_label.grid(row=0, column=0)
          self.age.grid(row=0, column=1)
          self.calc_button.grid(row=2, column=1)
          self.reset_button.grid(row=2, column=2)
          self.exit_button.grid(row=2, column=3)
          self.output_label.grid(row=1, column=0, columnspan=3)
          # Focus the cursor on age field
          self.age.focus()

      def calc_age(self):
       
          try:
                # Age calculation based on DOB input
                temp_dt = self.age.get()
                lst = temp_dt.split('/')
                print(lst)
                yr = int(lst[2])
                mm = int(lst[1])
                dy = int(lst[0])
                print(yr,mm, dy)
                birth_dt =  date(yr,mm,dy)
                days_in_year = 365.2425
                age = int((date.today() - birth_dt).days / days_in_year)
                print('Age :', age, ' years')
                self.output_label.configure(text = 'Age : ' + str(age) + '  years')
                
          except (ValueError, IndexError) as e:
                self.output_label.configure(text='Please enter a valid Date Of Birth.' + str(e))
                msg.showerror('Enter a valid Date of Birth', 'Date of Birth must be valid')
                self.reset()
                self.age.focus()
            
      def reset(self):
          
          self.age.delete(0,END)                   # clears the entry box
          self.output_label.configure(text = '')   # Erase the contents of the label text
          self.age.focus()                         # Focus the cursor on age field
           
#----------------------------------------  
root1 = Tk()
root1.title('Age Calculation from Date Of Birth')
root1.geometry('600x400')
temp_conv = GetAge(root1)
# mainloop
root1.mainloop()