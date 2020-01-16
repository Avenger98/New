# cycle_number = int(input("Enter the cycle number: "))
# i = 1
# max1 = 0
# max2 = 0
# sum = 0
# while i <= cycle_number:
#     num = int (input("Enter a value for number: "))
#     sum += num
#     if i == 1:
#        max1 = num
#     if i == 2:
#         max2 = num
#     if num > max2:
#         max2 = num
#     if max2 > max1:
#         temp = max2
#         max2 = max1
#         max1 = temp
#     i += 1
# print("The sum of the numbers: ", sum)
# print("The maximum number is: ", max1, "The second maximum number is: ", max2)

cycle_number = int(input("Enter the cycle number: "))
i = 0
result = 0
max2 = 0
list1 = []
while i < cycle_number:
    num = int(input("Enter the number: "))
    if i == 0:
        max1 = num
    if i == 1:
        max2 = num
    if num > max2:
        max2 = num
    if max2 > max1:
        temp = max2
        max2 = max1
        max1 = temp
    result += num
    i += 1
    list1.append(num)
print("This is the list created:", list1)
print(result)
print("The second maximum number:", max2, "\nThe maximum number:", max1)
