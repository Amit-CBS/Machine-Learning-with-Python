def ODDsum(n):
    sum=0
    for i in range(1,n+1,2):
        if i%2==1:
            sum+=i
    print("Sum of odd numbers=", sum)
def Square50():
    print("Squares from 1 to 50: ")
    for i in range(1,51):
        print(i**2, end=" ")
    print()