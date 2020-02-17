from tkinter import*
from tkinter import messagebox as msg
class MyText:
    def __init__(self, root):
        self.f=Frame(root, height=200, width=300)
        self.f.pack()
        self.b1=Button(self.f, text="Button1", width=15, height=2, activeforeground="red", command=self.buttonclick1)
        self.b1.grid(row=0,column=0,padx=10,pady=15)
        self.b2=Button(self.f, text="Button2", width=15, height=2, activeforeground="blue", command=self.buttonclick2)
        self.b2.grid(row=0,column=1,padx=10,pady=15)
        self.b3=Button(self.f, text="QUIT", width=15, height=2, activeforeground="red", command=root.destroy)
        self.b3.grid(row=0,column=2,padx=10,pady=15)
    def buttonclick1(self):
        print("The \'Button1\' was clicked me")#in CUI

        msg.showinfo("I will show","Text field")
        self.t=Text(self.f,width=20,height=2,font=('Courier',20, 'bold underline'), fg="blue", wrap=WORD)
        self.t.insert(END,"This is a text field")
        self.t.grid(row=1,column=0)

        msg.showinfo("I will show","Label")
        self.l=Label(self.f,text="This is a label",width=20,height=2,font=('Courier',20,'bold underline'),fg="blue")
        self.l.grid(row=1,column=1)
        
        msg.showinfo("1st button","ends")
    def buttonclick2(self):
        print("The \'Button2\' was clicked me")#in CUI
root=Tk()
root.title("My first Tkinter test")
root.geometry("900x500")
obj=MyText(root)
root.mainloop()