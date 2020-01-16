# from ITEmployees import *
#
# # first = parent(1)
# # print(first)
# #
# # second = parent(2)
# # print(second)
# print("Enter 0 to quit the programm")
# while True:
#
#      num = int(input("Enter the number: "))
#      first = parent(num)
#      second = parent(num)
#
#      if num > 0:
#          if num == 1:
#              print(first)
#              print()
#          elif num == 2:
#              print(second)
#              print()
#          else:
#              print("No such operator is found")
#              print()
#      else:
#          break


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper()


def say_whee():
    print("Whee")


say_whee = my_decorator(say_whee)
