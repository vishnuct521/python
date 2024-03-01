# encapsulation

# encapsulation allows for the hiding of the internal state and requring all interactions to occured
# to well defined interfaces this concepts at helps at acheiving data abstractions through well defined.


# private __ that will be a private attribute
# encapsulation nn paraynath method ne direct vilikkan pattulaa porath ninnu appo constructors undakanm
class car:
    def __init__(self,make,model,year):
        self.__make = make # private attribute
        self.__model = model
        self.__year = year
        self.__is_started = False
    def start__engine(self):
        self.__is_started = True
        print("engine started")
# can not call the self.__model = model directly so i need to create each methods
    def stop__engine(self):
        self.__is_started = False
        print("engine stopped")

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def is_engine_started(self):
        return self.__is_started

my_car = car(make = "toyota",model = "fortuner",year = 2023)
print("MAKE:",my_car.get_make())
print("MODEL:",my_car.get_model())
print("YEAR:",my_car.get_year())


# print("MAKE:",my_car._make())

my_car.start__engine()
print("Engine started?",my_car.is_engine_started())

my_car.stop__engine()
print("Engine stopped?" , my_car.is_engine_started())

# calling attribute i need to do method that is called encapsulation



