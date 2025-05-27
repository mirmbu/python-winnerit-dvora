class Person:

    # constractor - initialize the object.
    # when no self in the init of constractor - TypeError: Person.__init__() takes 4 positional arguments but 5 were given
    def __init__(self, name: str = "Name", age: float = 0, country: str = "Israel", job: int = 0):
        self.name = name
        self.age = age
        self.country = country
        self.job = job


    # Methods - functions in class, can get into by create a object of the class.
    def say_hello(self):
        print(f"Hello!, {self.name}")

    def get_age(self):
        return self.age



#error - Person.__init__() missing 3 required positional arguments: 'name', 'age', and 'country'
#person_object = Person()

person_object = Person("John", 36, "New York", 10)
person_object.say_hello()
print(person_object.get_age())
print(person_object.job)

person_object_2 = Person("Israel Israely", 70, "Israel")
person_object_2.say_hello()
print(person_object_2.get_age())
print(person_object_2.job) # will print 0, because job is not sent.



# person = {
#     "name": "John",
#     "age": 36,
#     "city": "New York"
# }
