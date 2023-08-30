a = input("Give any number to find Factorial: ")
num = int(a)


def findfact(num):
    fact = 1
    for i in range(1, num + 1):
     fact =fact*i
    return fact
     
     
x= findfact(num) 
print("The Factorial Number of", num, "is", x)
