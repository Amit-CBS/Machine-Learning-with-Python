from tkinter import*
from tkinter import messagebox as msg
class MyButton:
    def __init__(self, root):
        self.f=Frame(root, height=200, width=300)
        self.f.pack()
        self.b1=Button(self.f, text="Text Button", width=15, height=2, activeforeground="red", command=self.buttonclick)
        self.b1.grid(row=0,column=0,padx=10,pady=15)

        self.b2=Button(self.f, text="Text Button", width=15, height=2, activeforeground="blue", command=self.buttonclick)
        self.b2.grid(row=3,column=1,padx=10,pady=15)

        self.b3=Button(self.f, text="Quit", width=15,height=2,activeforeground="red",command=root.destroy)
        self.b3.grid(row=0,column=2,padx=10,pady=15)
    def buttonclick(self):
        msg.showinfo("Not","clicked me")
root=Tk()
root.title("My first Tkinter test")
root.geometry("500x400")
obj=MyButton(root)
root.mainloop()