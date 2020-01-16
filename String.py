a = "hello hOW"
b = a.split(" ")
print(b)

for i in range(len(b)):
    b[i] = b[i].lower()
    b[i] = b[i].capitalize()
print(b)

d = ""
for i in b:
    d += i + " "
print(d)
