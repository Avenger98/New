i = 1
first = 1
second = 1
print(first)
print(second)
while i <= 10 :
    next = first + second
    first = second
    second = next
    i+=1
    print(next)
