# date - 22/1/2024
#finnally
#Try
#Exception
# excception - try , except - eg :- user name is invalid


# exception handling
# length = 25
# width = 0
# print(length/width) # it will go infinity so it will through an error

try: # here catching the errror only
    # length = 10
    width = 0
#except Exception: # don't use first if you know the erro it will check the all error and print so use last (nameerror and zerodivisionerror will focus on the name error and zerodivisionerror)
#    print()
except NameError:
    print("variable has to be used before defining it")
except ZeroDivisionError:
    print("division by zero is invalid! kindly change your input ")
except Exception:
    print("Have caught a new error") # if you don't know the error we can use the exception error otherwise don't use
finally:
    print("finally block excuted")# its like else, it will work if there is no error also if we have error also it will print

# some contents are here so i missed
    # the try block contains the code that might rise an exception and the except block specifies how to handle the exception



