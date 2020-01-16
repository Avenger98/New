# cycle_number = int(input("Enter the cycle number: "))
# i = 1
# sum = 0
# max = 0
# while i <= cycle_number:
#     num = int(input("Enter the number: "))
#     sum += num
#     if i == 1:
#         max = num
#     if num > max:
#         max = num
#     i += 1
# print("The sum of the numbers: ", sum)
# print("The maximum number: ", max)

cycle_number = int(input("Enter the cycle number: "))
i = 0
result = 0
while i < cycle_number:
    num = int(input("Enter the number: "))
    if i == 0:
        max = num
    if num > max:
        max =  num
    result += num
    i+=1
print(result)
print(max)