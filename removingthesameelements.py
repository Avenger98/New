a = []
cycle_number = int(input("Enter the cycle number: "))
for i in range(cycle_number):
    num = int(input("Enter the number: "))
    a.append(num)
print("This is the list created: ", a)

b = []
for numbers in a:
    if numbers not in b:
        b.append(numbers)
print(b)