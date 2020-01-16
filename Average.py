cycle_number = int(input("Enter the cycle number:"))
i = 1
sum = 0
average = 0
while i <= cycle_number:
    num = int(input("Enter the number: "))
    sum += num
    i+= 1
average = sum / cycle_number
print("The sum of the numbers entered:", sum)
print("The average is: ", average)