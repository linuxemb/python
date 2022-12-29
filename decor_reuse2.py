
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
  def __init__(self, model, callback_methods=[]):
    self.model = model
    self.model_methods = [f for f in dir(type(self.model)) if not f.startswith('_')]
    self.model_attributes = [a for a in self.model.__dict__.keys()]
    self.callback_methods = callback_methods
    self.list_of_callback_methods = []
    self.__divide_callback_functions()
  
  def __getattr__(self, func):
    if func in self.model_methods and func not in self.list_of_callback_methods:
      def method(*args):
        return getattr(self.model, func)(*args)
      return method
    elif func in self.model_attributes:
      return getattr(self.model, func)
    elif func in self.list_of_callback_methods:
      def method(*args):
        return self.__callback_switchboard(func, *args)
      return method
    else:
      raise AttributeError
  
  def __divide_callback_functions(self):
    for method in self.callback_methods:
      if 'before' in method.keys(): self.list_of_callback_methods.append(method['before'])
      if 'after' in method.keys(): self.list_of_callback_methods.append(method['after'])     ### after wont work

  def __callback_switchboard(self, func, *args):
    for method in self.callback_methods:
      if 'before' in method.keys() and func == method['before']:
        getattr(self, method['do'])()
        getattr(self.model, func)(*args)
      if 'after' in method.keys() and func == method['after']:
        getattr(self.model, func)(*args)
        getattr(self, method['do'])()


class LeashedDogDecorator(Decorator):
  def __init__(self, dog: Dog):
    callbacks = [
      {'before': 'bark', 'do': 'growl'},  # only worked for base class member funcs
      {'after': 'bark', 'do': 'tug_on_leash'},  # only worked for base class member funcs
      #  {'before':  'tug_on_leash', 'do': 'bark'},  ## wont work as tg_on_leash is not func of base class 
    #  {'before': 'bark', 'do': 'growl'},
    #   {'after':  'tug_on_leash', 'do': 'bark'},
 
    ]
    super().__init__(dog, callback_methods=callbacks)
  
  def tug_on_leash(self):
    print("Let's GOOOOO!!!")
  

  def growl(self):
    # We’re going to make a method called growl and 
    # we’re going to make it fire before the Dog‘s bark method
    print("Grrr")

#_________________Testing____________
# >>> dog=Dog('f',3)
# >>> dog=LeashedDogDecorator(dog)
# >>> dog.bark()
# Grrr     
# Woof woof

   # {'before': 'bark', 'do': 'growl'},