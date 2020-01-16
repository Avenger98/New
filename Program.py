FILENAME = 'users.txt'
users = []

def signIn():
    login = input("Enter the name: ")

    if not isUserExists(login):
        print("User does not exist")
        return

    password = input("Enter the password: ")
    user = {}
    for i in users:
        if login == i['login']:
            user = i
            break
    if user['Password'] != password:
        print("Sign in error")

    print("Welcome", user['login'], "\n")
    userMenu(user)


def isUserExists(login):
    for i in users:
        if i['login'] == login:
            return True
    return False

def signUp():
    login = input("Enter name: ")

    if isUserExists(login):
        print("User is already exist")
        return


    password = input("Enter the password: ")
    confirmPassword = input("Confirm Password: ")
    if password != confirmPassword:
        print("Passwords are not equal")
        return
    user = {'login': login, 'password': password, 'balance': '0'}
    users.append(user)

    print("The user signed up successfuly\n")


def showUsers():
    print("List of users: ")
    for i in users:
        print(i['login'], i['password'], i['balance'], '$')
        print(i)
    print("\n")


def editUsers(user):
    password = input("Enter the password: ")
    user['password'] = password

    print("Password changed succesfully\n")


def deleteUser(user):
    for i in users:
        if i['login'] == user['login']:
            users.remove(i)


def putMoney(user):
    money = float(input("Enter the money: "))

    user['balance'] += money

def userMenu(user):
    while True:
        print("Login : ", user['login'])
        print("Balance: ", user['balance'], "$")

        option = int(input("1)Edit\n2)Delete\n3)Put Money\nChoose one Option above"))

        if option == -1:
            break
        if option == 1:
            editUsers(user)
        if option == 2:
            deleteUser(user)
        if option == 3:
            putMoney(user)
        else:
            print("No operation found")
def readUsers():
    file = open(FILENAME, "r")
    for line in file:
        data = str(line).split(" ")

        users.append({'login':data[0], 'password': data[1], 'balance': data[2]})
        file.close()
def writeUsers():
    file = open(FILENAME, "w")
    for i in users:
        file.write(i['login']+ " " + i['password']+ " " + i['balance']+ "\n")

    file.close()

def main():
    print("Welcome to Application")
    readUsers()
    while True:
        option = int(input("1)Sign in\n2)Sign up\n3)List of Users\nChoose one of the following: "))

        if option == -1:
            break
        if option == 1:
            signIn()
        if option == 2:
            signUp()
        if option == 3:
            showUsers()
        else:
            print("No such operator")
    writeUsers()
    print("Bye")
