"""
Applicability:

* Creating complex objects with many parts
* The construction process is independent of the main object
* The same construction process can be used to create different representations of the main object

Consequences:

* Isolates the construction code from the main object
* Allows for different representations of the main object to be created using the same construction process
* Provides finer control over the construction process
* Can create immutable objects
* Increases code complexity

"""

class MealBuilder:
  """The builder class"""
  def __init__(self):
    self.meal = Meal()
  
  def build_burger(self, name, price):
    self.meal.add_item(Burger(name, price))
  
  def build_drink(self, name, price):
    self.meal.add_item(Drink(name, price))
  
  def build_dessert(self, name, price):
      self.meal.add_item(Dessert(name, price))
  
  def get_meal(self):
      return self.meal
  
class Meal:
  """The main object"""
  def __init__(self):
    self.items = []
  
  def add_item(self, item):
      self.items.append(item)
  
  def get_cost(self):
      total_cost = 0
      for item in self.items:
          total_cost += item.price
      return total_cost
  
  def show_items(self):
      for item in self.items:
          print(f"Item: {item.name}, Price: {item.price}")

class Item:
  """The abstract interface for building items"""
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Burger(Item):
  """The concrete implementation for building burgers"""
  pass

class Drink(Item):
  """The concrete implementation for building drinks"""
  pass

class Dessert(Item):
  """The concrete implementation for building desserts"""
  pass
  
if __name__ == "__main__":
  builder = MealBuilder()
  builder.build_burger("Cheeseburger", 5.99)
  builder.build_drink("Coke", 1.99)
  builder.build_dessert("Ice Cream", 2.99)
  meal = builder.get_meal()
  meal.show_items()
  print(f"Total cost: {meal.get_cost()}")
