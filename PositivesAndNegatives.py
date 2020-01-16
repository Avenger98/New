a = []
cycle_number = int(input("Enter the cycle number: "))
for i in range(cycle_number):
    num = int(input("Enter the num: "))
    a.append(num)
print("This list was created:",a)

positives = []
negatives = []
for i in a:
    if i < 0:
        negatives.append(i)
    else:
        positives.append(i)
print("Negatives:",negatives)
print("Positives:",positives)