from tkinter import*
from tkinter import messagebox as msg
class MyButton:
    def __init__(self, root):
        self.f=Frame(root,height=200,width=300)
        self.f.pack()
        self.b1=Button(self.f, text="Text Button", width=15,height=2,activeforeground="red",command=self.buttonclick)
        self.b1.grid(row=0,column=0,padx=10,pady=15)
        self.b2=Button(self.f, text="QUIT", width=15,height=2,activeforeground="red",command=root.destroy)
        self.b2.grid(row=0,column=1,padx=10,pady=15)
    def buttonclick(self):
        self.l=Label(self.f,text="Welcome To Python",width=20,height=2,font=('Courier',20,'bold underline'),fg="blue")
        self.l.grid(row=1,column=0)
        msg.showinfo("Title","clicked me")
root=Tk()
root.title("My first Tkinter test")
root.geometry("500x400")
obj=MyButton(root)
root.mainloop()
