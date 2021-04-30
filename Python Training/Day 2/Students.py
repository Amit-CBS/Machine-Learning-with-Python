def student(name, roll=0, *ph, **marks):
    print('Name: ', name)
    print('Roll: ', roll)
    print('Phone:')
    for i in ph:
        print(i, "", end="", sep=',')
    print("\b ")
    print('Marks: ', marks)
    p=(marks['Phy']+marks['Chem']+marks['Maths'])/3
    print("Percentage: ", p)