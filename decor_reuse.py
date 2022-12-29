""" we could have Report objects floating around that can tug_on_leash.
 Is there anything we can do to prevent this?
 The goal is making sure that the only models passed to the LeashedDogDecorator are
  instances of the Dog class. Using python’s type checking, we would do something liek 'this:
"""


class Animal:
  def __init__(self, name, num_of_legs):
    self.name = name
    self.num_of_legs = num_of_legs
  
  def get_number_of_legs(self):
    print(f"I have {self.num_of_legs} legs")

class Dog(Animal):
  def __init__(self, name, num_of_legs):
    super().__init__(name, num_of_legs)

  def bark(self):
    print("Woof woof")


class Decorator:
  def __init__(self, model):
    self.model = model
    self.model_methods = [f for f in dir(type(self.model)) if not f.startswith('_')]
    self.model_attributes = [a for a in self.model.__dict__.keys()]
  
  def __getattr__(self, func):
    if func in self.model_methods:
      def method(*args):
        return getattr(self.model, func)(*args)
      return method
    elif func in self.model_attributes:
      return getattr(self.model, func)
    else:
      raise AttributeError

###   type hints. ======
#The goal is making sure that the only models passed to the
#  LeashedDogDecorator are instances of the Dog class. Using python’s type checking, we would do something liek this:
# The goal is making sure that the only models passed to the LeashedDogDecorator are
#   instances of the Dog class. Using python’s type checking, we would do something liek 'this:
class LeashedDogDecorator (Decorator):
    """s making sure that the only models passed to the LeashedDogDecorator are Dog class 
    """
    def __init__(self, dog:  Dog):  #using type hints
        super().__init__(dog)    # make dog instance

    def tug_on_leash(self):
        print("Let's Goo!!")

#----------------testing
# >> d=Dog('f',3)
# >>> d=LeashedDogDecorator(dog)
# >>> d.tug_on_leash()
# #Let's Goo!!