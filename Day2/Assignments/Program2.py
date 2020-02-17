st=input("Enter a string: ")
n=(int)(input("Enter index number of character which has to be removed: "))
if len(st)>0:
    if n<len(st):
        st=st[:n]+st[n+1:]
        print("New string=",st)
    else:
        print("Index out of bounds")