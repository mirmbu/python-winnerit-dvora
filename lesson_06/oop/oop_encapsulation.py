class Human:
    def __init__(self, name, age):
        # protected: one _ ,like self._name ->
        self._name = name
        # privet: two _, like self.__age
        self.__age = age

    # method in the class can get to privet variable.
    def print_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")

    # method that encapsulation the age. and by this method, can get the age even it private.
    def get_age(self):
        return self.__age



human_1 = Human("John", 30)
human_1.print_info()

human_2 = Human("Jane", 25)
human_2.print_info()


human_2._name = "xxxx" #still can init a protected variable.
# human_2.age = -5 #variable that created in run time, only for this object. not change the class. not good.
# print(human_2._name) #Alert - Access to a protected member _name of a class, but not get an exception
# print(human_2.__age) #Error - AttributeError: 'Human' object has no attribute 'age' (private variable)
print(human_2.get_age())