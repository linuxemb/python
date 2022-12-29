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
"""  poor design
class Kitchen:
      def __init__(self):

          self.microwave = Microwave()
          self.dishwasher = Dishwasher()
"""
""" delegation wrapper
"""
class Kitchen:

    def __init__(self):
      self.microwave = Microwave()
      self.dishwasher = Dishwasher()

    def  heat_up_food(self):
      self.microwave.heat_up_food()

    def wash_dishes(self):
      self.dishwasher.wash_dishes()

k = Kitchen()

