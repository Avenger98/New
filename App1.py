list = []

while True:
    num = int(input("Enter the number: "))
    if num < 0:
        break
    else:
        list.append(num)
print("This is the list created:", list)
