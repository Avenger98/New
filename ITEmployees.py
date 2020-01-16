# def parent():
#
#     print("Printing from the parent() function")
#
#     def first_child():
#         print("Printing from the first child")
#
#     def second_child():
#         print("Printing  from the second child")
#
#     first_child()
#     second_child()
#
#
# parent()

def parent(num):
    def first_child():
        return "Hi, I am John"
    def second_child():
        return "Call me Liam"
    if num == 1:
        return first_child()
    else:
        return second_child()
