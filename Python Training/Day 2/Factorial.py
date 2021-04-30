def fact1(n):
    p=1
    for i in range(1, n+1):
        p=p*i
    print(p)
#fact1(len(str(int(input("Enter a number:")))))
fact1(int(input("Enter a number:")))
def fact2(n):
    if n==0:
        return 1
    else:
        return n*fact2(n-1)
print(fact2(int(input("Enter a number:"))))