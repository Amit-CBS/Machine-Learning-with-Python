def fun1(*b):
    s=0
    c=0
    for i in b:
        try:
            s+=int(i)
            c+=1
        except:
            print('Error converting', i, 'into integers')
    return s/c
def fun2(*b):
    return sum(b)/len(b)


a = fun1(10,20,'30',40, 'a')
print(a)    