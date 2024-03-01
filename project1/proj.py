
store =[]

def create():
    name = input("enter your name")
    password = str(input("enter your password"))
    if len(password) < 3:
        print("password should be more than three digit \nenter a valid password ")
    else:
        print("login successfully")
        return
    user = {"name":name , "password" : password}
    store.append(user)


def exist():
    name = input("enter your name")
    password = int(input("enter your password"))
    for user in store:
        if user.get("name") == name and user.get("password") == password:
            print("login successfully")
        else:
            print("please enter again")




def main():
    while(True):
       print("enter 1 to create account")
       print("enter 2 to accessing existing account")
       print("enter 3 to exit")
       number = int(input("enter the number"))
       if number == 1:
           create()

       if number == 2:
           exist()

       else:
        print("exited")

main()

