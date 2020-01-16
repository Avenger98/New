import random

list1 = []
list2 = []
cycle_numbers = int(input("Enter the cycle number: "))
for i in range(cycle_numbers):
    list1.append(random.randint(0, 5))
    list2.append(random.randint(0, 2))
print("This is the first list created: ", list1)
print("This is the second list created: ", list2)
list3 = []
list4 = []
list5 = []
for numbers in list1:
    if numbers not in list3:
        list3.append(numbers)
for numbers in list2:
    if numbers not in list4:
        list4.append(numbers)
print("Before sorting")
print(list3)
print(list4)

list3.sort(reverse=False)
list4.sort(reverse=False)
print("After sorting")
print(list3)
print(list4)