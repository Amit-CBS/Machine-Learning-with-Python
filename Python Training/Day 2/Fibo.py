def Fibo(n):
    i,j=0,1
    for l in range(n):
        print(i,"", end="")
        (i,j)=(j,i+j)
#Fibo(int(input("Enter a number: ")))