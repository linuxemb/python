# inhiertae 
#not delegate

class Animal:
    def __init__(self, name, num_of_legs):
        self.name = name
        self.num_of_legs = num_of_legs
                    
    def get_number_of_legs(self):
        print(f"I have {self.num_of_legs} legs")

class Dog(Animal):
   def __init__(self, name, num_of_legs):
       super().__init__(name, num_of_legs)

dog = Dog('Fido', 4)
dog.get_number_of_legs()
                                            
