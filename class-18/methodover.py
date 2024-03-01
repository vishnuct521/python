# OVER_RIDING
# method overloading has understood in languages like java or c++,
# refers to the ability to define multiple methods with the same name but
# ccdifferent parametres with in a class how ever, pyhton does not support
# method overloading in the same way that java or c++ does.

# in python you can only have one method with a
# given name ion a class. if you define multiple
# method with the same name, the last method definition will override the previous
# once. therefore, method overloading as commonly understood, does not exist in python.

# class MathOperations:
#     def add(self, a, b):
#         return a + b
#     def add (self,a ,b ,c):
#         return a + b + c
#
# math_ops = MathOperations()
# result1 = math_ops.add(2,3,4)
# print("result 1: ", result1) # output : 9
#
# result2 = math_ops.add(2,3) # it will get error because 2nd parameter will override 3rd parameter



# how to read data from excelsheet


# open terminal and type  pip install openpyxl
# unicode error is nothing you should give two slash in the path address
import openpyxl # to impor the excel package
book = openpyxl.load_workbook("C:\\Users\\91735\\Desktop\\demo.xlsx") # To store the particular excel path
sheet = book.active # To access the excel sheet
cell = sheet.cell(row = 2, column = 1) # which column you want to see
print(cell.value)# printing the column value
#"C:\\Users\\91735\\Desktop\\demo.xlsx"