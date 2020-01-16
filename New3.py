# word1 = input("Enter the word: ")
# char = input("Enter the character: ")
# adding = ""
# adding1 = "abc"
# adding2 = ','
# for i in word1:
#     if i != char:
#         adding += i
#     elif i == char:
#         adding += adding2 + adding1
# print(adding)

word1 = input("Enter the word: ")
char = input("Enter the character: ")
word2 = input("Enter the word: ")
adding = ""
for i in word1:
    if i == char:
        adding += word2
    else:
        adding += i
print(adding)
