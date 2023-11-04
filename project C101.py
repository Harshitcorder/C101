import random
dise=input("Enter yes to run no to exit :")
i="yes"
while i==dise:
    num=random.randint(1,6) 
    print(num)
    i=input("Enter yes to run again no to exit :")
