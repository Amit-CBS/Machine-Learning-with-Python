from tkintertable import TableCanvas,TableModel
from tkinter import *
class TestApp():
    def __init__(self,root):
        self.f=Frame(root,height=200,width=100)
        self.f.pack(fill=BOTH,expand=1)
        self.table=TableCanvas(self.f,read_only=True)
        self.table.importCSV('/media/amit/Work/GitHub/Machine Learning with Python/DataSets/empsal.csv')
        print(self.table.model.columnNames)
        self.table.show()
root=Tk()
root.title("Title6")
root.geometry('800x400')
obj=TestApp(root)
root.mainloop()