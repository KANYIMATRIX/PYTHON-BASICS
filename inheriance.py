class Schoolmember:
    """Represents any school member"""
    def __init__(self,name,age):

        self.name=name
        self.age=age
        print('(Initialized Schoolmember: {})'.format(self.name))


    def tell(self):
        """Tell my details."""
        print('Name:"{}" Age :"{}"'.format(self.name,self.age),end="")


class Teacher(Schoolmember):

    """Represents a teacher"""
    def __init__(self,name,age,salary):

        Schoolmember.__init__(self,name,age)
        self.salary=salary
        print('(Initialised Teacher: {})'.format(self.name))

    def tell(self):
        Schoolmember.tell(self)
        print('salary: "{:d}"'.format(self.salary))

class Student(Schoolmember):
    """Represents the Student"""
    def __init__(self,name,marks,age):
        Schoolmember.__init__(self,name,age)
        self.marks=marks
        print('(Initialized Student : {}'.format(self.name))

    def tell(self):
        Schoolmember.tell(self)
        print('marks "{:d}"'.format(self.marks))


t=Teacher("mrs. Shiva",40,30000)

s=Student("Kanyi",23,78)


print()

members=[t,s]
for member in members:
    member.tell()

