# # def say_hello(name):
# #     print("Hello", name)
# #
# #
# def readCars():
#     file = open("Cars.txt", "r")
#     print(file.read())
#     file.close()
#
#
# def writeCar(name, price):
#     file = open("Cars.txt", "a")
#     file.write(name + "      " + price + "\n")
#     file.close()
#
#
# def main():
#
#     while True:
#         readCars()
#         creatingcar = input("Do you wan to create a new car (Yes or No): ")
#         if creatingcar == "No":
#             break
#         elif creatingcar != "Yes" or "yes":
#              print("Incorrect Argument")
#         name = input("Enter the name: ")
#         price = input("Enter the price: ")
#         writeCar(name, price)