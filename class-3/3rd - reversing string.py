# class - 1

pgm = "python pgm is easy"
print(pgm.replace("easy", "powerfull")) # To replacing

# To retrieve string from variable  using intex position
pgm = "python pgm is easy"
print(pgm[0:6])
print(pgm[-3::-1])



# string number formating
# one way
number = 21;
str = "my number is {}".format(number)
print(str)

# second way
number2 = 22;
str2 = "my number is {}"
print(str2.format(number2))

# third way :- use this one this is the best way
number3 = 45;
str3 = f"my number is {number3}"
print(str3)









