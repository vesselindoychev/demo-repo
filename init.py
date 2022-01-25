from re import S


class Person:
    def __init__(self, first_name, last_name, age, city) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        
    def call_person(self):
        return f"Hi, I am {self.first_name} {self.last_name} from {self.city} and\
            i am {self.age} years old."
            
            
p = Person('Ivan', 'Ivanov', 'Pleven', '12')
print(p.call_person)