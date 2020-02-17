from tkintertable import TableCanvas,TableModel
from tkinter import *
from tkintertable.Testing import sampledata
data=sampledata()
class TestApp(Frame):
    def __init__(self,parent=None):
        self.parent=parent
        Frame.__init__(self)
        self.main=self.master
        self.main.geometry('800x500+200+100')
        self.main.title('Title')
        f=Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        table=TableCanvas(f,data=data)
        print(table.model.columnNames)
        table.show()
        return
app=TestApp()
app.mainloop()