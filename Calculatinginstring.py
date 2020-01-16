word1 = input("Enter the word: ")
word2 = word1.split(" ")
print("List created:", word2)

sum = 0
distinction = 0
mult = 0
division = 0

if word2[0] == '+':
     sum = float(word2[1]) + float(word2[2])
     print('Sum of the numbers:', round(sum, 2))

elif word2[0] == '-':
    distinction = float(word2[1] ) - float(word2[2])
    print('Distinction of the two number:', round(distinction, 2))

elif word2[0] == '*':
    mult = float(word2[1]) * float(word2[2])
    print("Multiplication of two numbers:", round(mult, 2))

elif word2[0] == '/':
    division = float(word2[1]) / float(word2[2])
    print("The Division of the two numbers:", round(division, 2))

else:
    print("No operators found")

# word1 = input("Enter the word: ")
# word2 = word1.split(" ")
# result = 0
# if word2[0] == "+":
#     result = int(word2[1]) + int(word2[2])
#     print(result)
# elif word2[0] == "-":
#     result = int(word2[1]) - int(word2[2])
#     print(result)
