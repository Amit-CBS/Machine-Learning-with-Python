x=int(input('Input a number: '))
i=1
c=0
while i<=x:
    if(x%i==0):
        c+=1
    i+=1
if(c==2):
    print("Prime")
else:
    print("Not prime")

//a=2
//while a<x:
// if x%a==0:
//  print(x, "not prime")
//  break
// a+=1
//if a==n
// print(x, 'is prime')
//print(i, i*10, end="\n", sep=" ")