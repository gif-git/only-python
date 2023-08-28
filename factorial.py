a = input("Give any number to find Factorial: ")
num = int(a)
fact = 1
for i in range(1, num + 1):
    fact =fact*i
    print("The Factorial Number of", num, "is", fact)
