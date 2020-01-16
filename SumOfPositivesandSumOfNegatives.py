cycle_number = int(input("Enter the cycle number: "))
positive = 0
negative = 0
i =1
while i <= cycle_number:
    num = float(input("Enter any number: "))
    if num > 0:
        positive += num
    else:
        negative += num
    i+=1
print("Sum of positives:", positive)
print("Sum of negatives: ", negative)