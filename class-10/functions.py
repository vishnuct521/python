# functions

# 25/1/2024
# class-10
# user defined functions

def helloworld():
    print("welcome to the session")

helloworld()

def greet(name):
    print("Hello"+" "+name+"!")
greet("vishnu")


def calculate(length,width):
    area = length * width
    print(area)
calculate(25,35)


def display(length,width):
    area = length * width
    return area
rectangle_length = 5
rectangle_width = 3
area_result = rectangle_length,rectangle_width
print(f"The area of the rectangle is : {area_result}")
display(2,5)


