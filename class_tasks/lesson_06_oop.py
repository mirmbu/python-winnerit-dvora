class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return f"Name from Person class: {self._name}"



class Student(Person):
    def __init__(self, name, student_id: int):
        super().__init__(name)
        self.__student_id = student_id

    def display_student_id(self):
        return f"Student ID: {self.__student_id}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


#Main
person = Person("Dvora")
print(person.get_name())

student = Student("Lea", 123)
print(student.name)
print(student.display_student_id())

student.name = "Dina"
print(student.name)

