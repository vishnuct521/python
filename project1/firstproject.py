list1 = []


def createAccount():
    name = input("enter userName name")
    password = input("enter a password")
    if len(password) < 3:
        print("enter more than three digit /nplease enter valid password")

        return
    user = {"name": name, "password": password}
    list1.append(user)


def existingAccount():
    name = input("enter userName name")
    password = input("enter a password")
    for user in list1:
        if user.get("name") == name and user.get("password") == password:
            print("login succesfully")
        else:
            print("invalid password or username")


def mainfun():
    while True:
        print("Enter 1 to create a account ")
        print("Enter 2 to access existing account")
        print("Enter 3 to exit")
        number = int(input("Enter number"))
        if number == 1:
            createAccount()
        elif number == 2:
            existingAccount()
        else:
            return


mainfun()
