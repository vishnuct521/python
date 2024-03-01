

# if condition
# conditional statements are block of statement whose execution depends on a certain conditions
# simple if condition is one where block of statements gets executed if the condition mentioned
# in the if statement evaluates true

# if-else statement
# ifelse statements is one where a block of statement under if condition where gets executed if the
# condition evaluates  to true if the condition evaluates to false the block of statements under else is executed""

# IF ELIF - STATEMENT
# IF ELIF is statement is one where multiple if conditions are evaluated one after another
# if an " if " statement evaluates to false. elif stands for else-if.
# If all the if conditions evaluates to false, the block of statement under " else " gets executed "

# conditional statement

# if condition
total_mark = 90
# total_mark = 30
# total_mark = 45
if total_mark >= 90:
    print("congrats you have secured 'A' grade") # if condition is true the if block will execute

# elif - condition
elif total_mark >= 40:
    print("you have cleared the exams")
else:
    print("you failed the exam") # else don't have any condition it is like an exit


# nested if condition
# * it will check the two condition also

total_mark = 100
if total_mark >= 90:
    print("congrats you have secured 'A' grade")
    if total_mark == 100:
        print("you have also secured full mark")
elif total_mark < 100:
    print("your make is below 100") # I did this code just for checking

# if with logical operators
total_mark = 95
attendance = 90

if total_mark >= 90 and attendance >= 90: # and / or / not
    print("you are a very disciplined student")


# if fruit is "mango" or fruit is "apple"
fruit = "apple"
if fruit == "mango" or fruit == "apple":
    print("i like that fruit")