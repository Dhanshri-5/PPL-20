#implement animal and shape class to demonstrate abstraction, encapsulation, public and private access specifiers

from abc import ABC, abstractmethod
class Animal:

    sound = ''
    def __init__(self):
        self._name = ''       #protected variable
        self._living = True   # Protected variable 
        self.__eyes = 2       # Private varible 
        self.legs = 4         # Public varibale legs

    def setsound(self, sound):
        self.sound = sound
    def getsound(self):
        print(f"It makes {self.sound} sound.")   

    def getliving(self):
        return self._living
    def setliving(self, living):
        self._living = living

    def geteyes(self):
        return self.__eyes
    def seteyes(self, eyes):
        self.__eyes = eyes

    def getlegs(self):
        return self.legs    
    def setlegs(self, legs):
        self.legs = legs 

    @abstractmethod
    def features(self):
        pass

#child class 1
class Lion(Animal):
    def __init__(self):
        self._name = 'Lion'

    def eats(self):
        print("Lion eats meat!")

    def color(self):
        print("Color of Lion is Grayish Yellow!")

    def describe(self):
        print(f"{self._name} is a carnivorous animal.")

    def features(self):
        print("Males have manes. Golden brown color.")

#child class 2
class Tiger(Animal):
    def __init__(self):
        self._name = 'Tiger'

    def eats(self):
        print("A tiger eats meat!")

    def color(self):
        print("Color of Tiger is orange with black stripes!")

    def sound(self):
        print("A tiger roars!")

    def describe(self):
        print(f"{self._name} is carnivorous animal.")

    def features(self):
        print("Black stripes on orange body")

#child class 3
class Bear(Animal):
    def __init__(self):
        self._name = 'Bear'

    def describe(self):
        print(f"{self._name} is a {self._name}")

    def features(self):
        print("Sharp claws. Very powerful.")

#child class 4
class Giraffe(Animal):

    def __init__(self):
        self._name = 'Cheetah'

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def color(self):
        print("Giraffe has patterns of dark brown, orange, or chestnut spots broken up by white or cream-coloured stripes!")

    def describe(self):
        print(f"{self._name} is a caarnivorous.")

    def features(self):
        print("Tallest of all animals.")

#child class 5
class Cat(Animal):
    def __init__(self):
        self._name = 'Cat'

    def eats(self):
        print("A cat eats meat, fish, cat-food etc.!")

    def color(self):
        print("A cat could be of any color(white,black,brown,golden).")

    def describe(self):
        print(f"{self._name} is a carnivorous.")

    def features(self):
        print("Domesticated.")

#child class 6
class Dog(Animal):
    def __init__(self):
        self._name = 'Dog'

    def eats(self):
        print("A dog eats meat, veggies, dog-food etc.!")

    def color(self):
        print("A dog could be of any color(breed wise).")

    def describe(self):
        print(f"{self._name} is a {self._name}")

    def features(self):
        print("Domesticated. Human friendly")

#child class 7
class Monkey(Animal):
    def __init__(self):
        self._name = 'Monkey'

    def eats(self):
        print("Monkey eats vegetables and fruits")

    def color(self):
        print("Color of monkey is brown")

    def describe(self):
        print(f"{self._name} is a herbivorous.")

    def features(self):
        print("Humans and monkeys share common ancestors.")

#child class 8
class Deer(Animal):
    def __init__(self):
        self._name = 'Deer'

    def eats(self):
        print("A deer eats plants, leaves!")

    def color(self):
        print("Color of Deer is Reddish brown!")

    def sound(self):
        print("A Deer makes a grunting sound.")

    def describe(self):
        print(f"{self._name} is a herbivorous.")

    def features(self):
        print("Bucks have antlers.")

#child class 9
class Rabbit(Animal):
    def __init__(self):
        self._name = 'Rabbit'

    def eats(self):
        print("A rabbit eats plants, leaves!")

    def color(self):
        print("Color of rabbit is white or Reddish brown!")

    def describe(self):
        print(f"{self._name} is a herbivourous.")

    def features(self):
        print("Likes Carrots.")
#child class 10 
class Zebra(Animal):

    def __init__(self):
        self._name = 'Rabbit'

    def eats(self):
        print("Zebra eat grass!")

    def color(self):
        print("A Zebra has black and white stripes on its body.")

    def describe(self):
        print(f"{self._name} is a herbivourous.")

    def features(self):
        print("Mostly found in groups.")


#Base class
class Shapes:
    def __init__(self):
        self._Type = ''                         #Protected member
        print("A shape has been created!")

    def getType(self):
        print(self._Type)
        
    def __del__(self):
        print('Shape has been destructed!')
        
#Triangle
class triangle(Shapes):
    def __init__(self):
        self._side = 3

    #We can modify protected members via base class    
    def settype(self):
        self._Type = 'Polygon with 3 sides'

    #Only member functions can have access to private members    
    def getside(self):
        print(self._side)
        
#Equilateral traingle inherited from triangle
class equilateral(triangle):

    #We can modify protected members via base class    
    def settype(self):
        self._Type = 'Polygon with 3 sides and all three are equal'

    #Only member functions can have access to private members    
    def getside(self):
        print(self._side)

#Rectangle
class rectangle(Shapes):
    def __init__(self):
        self.__side = 4     #private attribute

    #We can modify protected members via base class    
    def settype(self,typ):

        self._Type = 'Polygon with 2 equal and 2 unequal sides'
    #Only member functions can have access to private members    
    def getside(self):
        print(self.__side)
        
#Square inherited from rectangle
class square(rectangle):
    def __init__(self):
        self.sides = 4
    #We can modify protected members via base class    
    def settype(self):
        self._Type = 'Polygon with 4 sides all of which are equal'
    
    def getside(self):
    #The function will throw an error if this is executed as the private member of base class is being accessed
    #print(self.__side)
        print(self.sides)
        
#Rhombus inherited from square
class rhombus(square):
    def settype(self):
        self._Type = 'Polygon with 4 sides all of which are equal but angles are not 90'
    
    #The base class has a public member in sides so we can access it in the base class and outside
    def getside(self):
        print(self.sides)        

#Circle
class circle(Shapes):
    def __init__(self):
        #Shapes.__init__(self)
        self.__r = 0                    #private attribute
        self.__eqn = 'x^2 + y^2 = r^2'  #private attribute
    def settype(self):
        self._Type = 'Conic'
    #Setter function for accessing private member
    def setradius(self,r):
        self.__r = r
    #Getter function for accessing private member
    def getarea(self):
        print(3.14 * (self.__r)**2)
        
#Ellipse
class ellipse(Shapes):
    def __init__(self):
        self.__a = 0
        self.__b = 0
        self.__eqn = 'x^2/a^2 + y^2/b^2 = 1'
    def settype(self):
        self._Type = 'Conic with a major and minor axis'
    #Setter function for accessing private member
    def setradius(self,a,b):
        self.__a = a
        self.__b = b
    #Getter function for accessing private member
    def getarea(self):
        print(3.14 * self.__a * self__b)        