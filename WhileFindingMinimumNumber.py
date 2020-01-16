cycle_number = int(input("Enter the cycle number:" ))
i = 1
sum = 0
min = 0
while i <= cycle_number:
    num = int(input('Enter the number: '))
    sum += num
    if i == 1:
        min = num
    if num <= min:
        min = num
    i += 1
print("The sum of the number entered: ", sum)
print("The minimum number is :", min)