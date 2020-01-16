# list1 = []
# while True:
#     num = int(input("Enter the number: "))
#     if num < 0:
#         break
#     list1.append(num)
# print("This is the list created:", list1)
# list2 = set(list1)
# print("This is the set created:", list2)

list = []
while True:
    num = int(input("Enter the number: "))
    if num < 0:
        break
    else:
        list.append(num)
print(list)
list1 = set(list)
print(list1)
