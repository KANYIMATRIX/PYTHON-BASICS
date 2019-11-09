class Schoolmember:
    """Represents the schoolmember"""
    def __init__(self,name,age):
        self.age=age
        self.name=name
        print('(Intialized schoolmember : {})'.format(self.name))
        
        
    def tell(self):
        Schoolmember.__init__(self)
        print('Name "{}" Age "{}"'.format(self.name,self.age,end=""))
        
class Teacher(Schoolmember):
    """Represents the Teacher"""
    def __init__(self,name,age,salary):
        
        Schoolmember.__init__(self,name,age)
        self.salary=salary
        
        print('(Initialized teacher : {})'.format(self.name))
        
        
    def tell(self):
        Schoolmember.tell(self)
        print('salary is "{:d}"'.format(self.salary))
        
        
        
class Student(Schoolmember):
        
        def __init__(self,name,age,marks):
            Schoolmember.__init__(self,name,age)
            self.marks=marks
            print('(Intialized Student: "{}")'.format(self.name))
            
            
        def tell(self):
            Schoolmember.tell(self)
            print('marks "{:d}"'.format(self.marks))
            
            
            
t=Teacher("mrs Shivani",40,67888)
s=Student("Kanyi",24,67)

print()

members=[t,s]
for member in members:
    member.tell()

































