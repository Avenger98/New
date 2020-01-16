import random
a = []
b = []
cycle_number = int(input("Enter the cycle number: "))
for i in range(cycle_number):
    a.append(random.randint(0, 10))
    b.append(random.randint(0, 10))
print("The first list was created:", a)
print("The second list created: ", b)




