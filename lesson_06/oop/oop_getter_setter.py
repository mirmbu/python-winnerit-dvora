class Human:
    def __init__(self, name, age):
        self._name = name
        self.__age = age if age > 0 else 18

    def print_info(self):
        print(f"Name: {self._name}, Age: {self.__age}")


    #get with decorator property.
    @property
    def name(self):
        return self._name

    #set with decorator of the property. should be after get, and with the same name
    @name.setter
    def name(self, new_name: str):
        self._name = new_name


    #return the age.
    def get_age(self):
        return self.__age

    #set the age.
    def set_age(self, new_age):
        if new_age < 0:
            # get an error if age is negative.
            raise ValueError(f"Provided age '{new_age}' cannot be negative.")
        self.__age = new_age


human_1 = Human("John", -5)
print(human_1.get_age())
human_1.set_age(90)
print(human_1.get_age())
#property:
print(human_1.name)
human_1.name = "Dvora"
print(human_1.name)
#Name mapping - not recommended
#print(human_1._Human__age)