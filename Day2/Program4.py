def midIns(s1,s2):
    s1=s1[:(int)(len(s1)/2)]+s2+s1[(int)(len(s1)/2):]
    return s1

s1=input("Enter a string: ")
s2=input("Enter the string which has to be inserted: ")

print("New string=", midIns(s1,s2))