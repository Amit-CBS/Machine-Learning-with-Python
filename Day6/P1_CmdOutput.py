from tkinter import *
class MyButton:
    def __init__(self,root):
        self.f=Frame(root,height=200,width=300)
        self.f.pack()
        self.b=Button(self.f, text="Button0", width=15,height=2,activeforeground="red",command=self.buttonclick)
        self.b.pack()
    def buttonclick(self):
        print("The \'button0 \' was clicked me")
root=Tk()
root.title("My first Tkinter test")
root.geometry("500x400")
obj=MyButton(root)
root.mainloop()
