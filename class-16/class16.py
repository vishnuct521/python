# set = {1,2,3}
# set1 = {3,4,5}
# print(set - set1)
# print(set | set1)
# print(set & set1)

# over_rading
# class inherit :- using class inherit it will inherit all properties from the parent if needed
# super :-  if you use super() it will go to the original value

class Employee:
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 40;

    def displaythenumberofworkinghours(self): # only one display is enough for classes
        print(self.numberofworkinghours)

# inherit class
class Trainee(Employee):
    def setnumberofworkinghours(self):
        self.numberofworkinghours = 45;

    def resetnumberofworkinghour(self):
        super().setnumberofworkinghours() # if you use super() it will go to the original value


employee = Employee()
employee.setnumberofworkinghours()
print(f"number of working hours of employees:{employee.setnumberofworkinghours()}")
employee.displaythenumberofworkinghours()

# inheritance
trainee = Trainee()
trainee.setnumberofworkinghours()
print("number of working hours of trainee,", end = ("") )
trainee.displaythenumberofworkinghours()

trainee.resetnumberofworkinghour()
print("number of working has been reset :", end = " ")
let = str(trainee.displaythenumberofworkinghours())