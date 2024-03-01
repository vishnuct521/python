# note - 1
# Metod overriding refers to the ablility
# of a subclass to provide a specific
# implementation of a method that is difined
# in its superclass.
#
# note - 2
# when a method in a subclass has the sname
# name, parameters and return type as
# method in its superclass , the method in the
# subclass overrides the method in the superclass

# multiple inheritance


# DIMOND PROBLEM

class A:
    def method(self):
        print("Method of class A")

class B(A):
     def method(self):
         print("Method of class B")
class C(A):
    def method(self):
        print("Method of class C")


class D(C,B): # FOR GIVING THE RESON MEANS 'D' IS HAVING MULTIPLE INHERITANCE,
    # it will take the first variable only that is the rule
    # That is the most priority
# class D(B,C): # it will access the method of C only why because
    pass # in future some will be there implementation
d = D()
d.method()



# return is use to inside a function to exit the function and return
# a value back to the caller it is tippically a last statement in the function
# although you can have multiple return statement in different part of the function.
#
#
# pass is a null operation in python it is used as a place_holder when a statement is syntatically
# required but you dont want to execute in the code it is typicaly used in placess where syntax is required
# syntax required the statement but you donn'd need any action to be taken.
#
#
#
# polymorphisam
# polymorphisam in python refer ability of different object to respond to the same method or function called in different
# ways it allows objects of different classes to be treated as objects of a common superclass

# DUCK TYPE
# A Duck typing is a concept in python where the time of class of an object is less importance then the method it defined
