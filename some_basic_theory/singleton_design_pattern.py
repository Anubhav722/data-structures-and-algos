# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton


# This pattern restricts the instantiation of a class to one object.
# It is a type of creational pattern and involves only one class to
# create methods and specified objects.


# https://www.geeksforgeeks.org/singleton-design-pattern/ - JAVA SOLUTION

class Singleton:
   __instance = None

   @staticmethod
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance

   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance != None:
         raise Exception("This class is a singleton!")
      else:
         Singleton.__instance = self

s = Singleton()
print s

s = Singleton.getInstance()
print s

s = Singleton.getInstance()
print s
