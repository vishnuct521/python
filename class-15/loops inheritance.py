# class -15 inheritance
from oops import calculator

class childimpli(calculator):
    num2 = 200
    def __init__(self):
        calculator.__init__(self,2,10)
    def getcompleteddata(self):
        return self.num2 + self.num + self.summition()

obj = childimpli()
print(obj.getcompleteddata())
