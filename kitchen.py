

"""
Kitchen composed by 2 other class microware and dishwasher, sho using the wrapper to override the get_attribut 

Good site for python delegate explaniatin
https://erikscode.space/index.php/2020/08/01/delegate-and-decorate-in-python-part-1-the-delegation-pattern/
"""

class Microwave:
      def __init__(self):
           pass

      def heat_up_food(self):
           print("Food is being microwaved")

class Dishwasher:
      def __init__(self):
           pass

      def wash_dishes(self):
           print("Dishwasher starting")


class Kitchen:
  def __init__(self):
    self.microwave = Microwave()
    self.dishwasher = Dishwasher()
    self.microwave_methods = [f for f in dir(Microwave) if not f.startswith('_')]  #find all mehtoud belong to microwave class
    self.dishwasher_methods = [f for f in dir(Dishwasher) if not f.startswith('_')]#find all mehtoud belong to kitchen class
  
  
  def __getattr__(self, func):
    def method(*args):
      if func in self.microwave_methods:
        # wrapp the mehtod in customized funcs which belong to microwave class
        return getattr(self.microwave, func)(*args)  
      # wrapp the mehtod in customized funcs which belong to dishwasher class
      elif func in self.dishwasher_methods:
        return getattr(self.dishwasher, func)(*args)
      else:
        raise AttributeError
    return method


# testing

def main():
    # micro= Microwave()
    # dish = Dishwasher()
    kitchen= Kitchen()
   #############musht be in another file test kitchen.py
    kitchen= Kitchen()
    kitchen.heat_up_food()

    # kitchen.dishwasher.wash_dishes()
    # kitchen.microwave.heat_up_food()
   


if __name__ == "__main__":
    main()



# What’s going on here? Well, in the Kitchen‘s constructor, we not only set the microwave and dishwasher attributes, we also set an array of available methods from within those classes (we ignore the methods that start with an underscore because those are Ptyhon built-in methods and we don’t want to hijack those).

# Then, we overwrite Kitchen‘s __getattr__ method by defining another method within it. Since this method will be called anytime an attribute that doesn’t exist in Kitchen is called, this is the ideal place to do our delegation. We catch the called method in the func argument, then check if it is within the list of available methods in Microwave or Dishwasher. If it is, we call that function with (*args), which represents any arguments the non-existent function might have been called with (though in our current case, this is irrelevant).

# This has probably been confusing so let’s see it in action and talk about what is actually going on. In your Python console:

# # >>> from kitchen import *

# is not without its downsides. For example, since delegated methods aren’t explicitly defined inside composite classes, your IDE might have a hard time offering code completion for delegated methods. In fact, it might even highlight calls to delegated methods as potential errors since, when analyzed statically, it seems like those methods don’t exist.

# Additionally, the use of metaprogramming (which is what we did when we overwrote the __getattr__ method) can slow scripts down. What you lose in execution speed, you might gain in development velocity however; all software design decisions are trade-offs.

# This pattern is a powerful tool in object oriented programming and for making code readable and extendable. It is also paramount to the next pattern we cover in this series: t