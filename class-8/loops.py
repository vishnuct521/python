

#1)
temp = 77

while temp >= 68 and temp <= 77:
       print("room temp is maintened at {} deg F".format(temp))
       temp = temp -10

#2)
while True:
     print("This loop runs forever")

# MATRIX 3 X 3

number = 1

for row in range(1,4):
    for column in range(1,4):
          print(number,end=' ')
          number = number + 1
        # print() // here indentation error is there


# Break

for number in range (1,11):
     if number ==  15:
            break
     else:
           print(number)

# Continue

for number in range (1,11):
     if number ==  5:
            continue
     else:
           print(number)

for number in range (1,11):
     if number ==  5:
            continue
     else:
           print(number)
else:
     print("All the numbers were printe without breaking")




