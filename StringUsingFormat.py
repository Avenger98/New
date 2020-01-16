'''quantity = 3
item_no = 567
price = 49.95

my_order = "I want {} pieces of Item {} for {} $"
print(my_order.format(quantity, item_no, price))
'''
'''
age = 40
txt = "My name is John, I am {} years old"
print(txt.format(age))
'''
salary = 5000
txt = "My name is John and my salary is 10 times more than {}"
print(txt.format(salary))


txt = "HELLO WORLD"
print(txt.casefold()) # It makes the sentence lower-cases
print(txt.center(56)) # it pushes the sentence 56 spaces from the beginning
print(txt.center(100, '^')) # it putes the arrows 56 times