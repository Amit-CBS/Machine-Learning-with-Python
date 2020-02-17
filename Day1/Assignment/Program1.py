for i in range(2,50):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
            break
    if c==0:
        print(i, end=" ")
print()