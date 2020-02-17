# empsalmenu.py 
# Main menu program for Project 1

from tkinter import *
import sys
import os
import subprocess

class Empsal:

    # Constructor
    def __init__(self, root):

        self.main_lbl=Label(root, text='Project Title', fg='blue', font=('Arial', -15, 'bold underline'))
        self.main_lbl.place(x=200, y=250)
       
        # Create menubar
        self.menubar=Menu(root)
        root.config(menu=self.menubar)            # attach the menubar to root
        # Now create Single menubar operation menu
        self.mysql_menu=Menu(root, tearoff=0)

        self.menubar.add_cascade(label='Data Conversion', menu=self.mysql_menu)
        # Now create menu items under menubar 
        self.mysql_menu.add_command(label='Build DF', command=self.create_df)
        self.mysql_menu.add_command(label='Build CSV', command=self.create_csv)
        self.mysql_menu.add_command(label='Convert to Excel', command=self.mysql_to_xls)
         
        # Now add a separator
        self.mysql_menu.add_separator()
        # Now create a Exit menu
        self.mysql_menu.add_command(label='Exit', command=root.destroy)

        # Now create Data Maintenance operation menu
        self.data_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Reports', menu=self.data_menu)
        self.data_menu.add_command(label='Rep1', command=self.rep1)
        self.data_menu.add_command(label='Rep2', command=self.rep2)
        self.data_menu.add_command(label='Rep3', command=self.rep3)
        self.data_menu.add_command(label='Plot', command=self.plot)
        
        # Prediction Menu
        self.predict_menu=Menu(root, tearoff=0)
        self.menubar.add_cascade(label='Prediction', menu=self.predict_menu)
        self.predict_menu.add_command(label='Predict', command=self.predict)
         

    def create_df(self):
        subprocess.check_call(["python.exe","create_df.py"])
    def create_csv(self):
        subprocess.check_call(["python.exe","create_csv.py"])
    def mysql_to_xls(self):
        subprocess.check_call(["python.exe", "create_excl.py"])
    
    def rep1(self):
        subprocess.check_call(["python.exe", "rep1.py"])
    def rep2(self):    
        subprocess.check_call(["python.exe", "rep2.py"])
    def rep3(self):
        subprocess.check_call(["python.exe", "rep3.py"])               
    def plot(self):
        subprocess.check_call(["python.exe", "plot.py"])
        
    def predict(self):
        subprocess.check_call(["pythonw.exe", "predict.py"])     
#=====================================================================================================
  
root=Tk()
root.title('Your Title Here')

obj=Empsal(root)
root.geometry('800x600')
root.mainloop()

                                 
        
        
        
        
                 
