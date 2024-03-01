# OOPS
# classes = they are user defined blueprint or prototype
# EG :- if calculator is a class then sum , mutiplication and substracyion will be method
# so classes will be consists of methods , class variable , instence variable and constructorn etc
# creation of new object not needed...


# class calculator:
#     num = 100
#     def getdata(self):
#         print("i am now executing as method in class")
# obj = calculator()
# obj.getdata()
# print(obj.num)


# step -2 => constructor
# class calculator:
#     num = 100
#     def __init__(self):
#         print("i am called automatically when object is created")
#
#     def getdata(self):
#         print("iam now executing as mothod in class")
# obj = calculator()
# obj.getdata()
# print(obj.num)

# notes
# constructor
# when you defined methods in a class
#     self key word is manditory for variable name into methods
#     if constructor...... is None:
#         new keyword is not required for creating class


class calculator:
    num = 100
    def __init__(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("i am called automatically when object is created")

    def getdata(self):
        print("iam now executing as mothod in class")

    def summition(self):
        return  self.firstnumber + self.secondnumber + calculator.num
obj = calculator(20,20)
obj.getdata()
print(obj.num)
print(obj.summition())

# calculator(20,20)
# calculator.getdata()
# print(calculator.num)
# print(calculator.summition())



