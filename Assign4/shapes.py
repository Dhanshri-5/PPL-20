
from abc import ABC, abstractmethod
from turtle import *
import math
import time
t = Turtle()
t.shape()

class Shapes(ABC):

    def __init__(self):
        self.name = ''       
    def type(self):
        print("It is a 2-D shape")

    @abstractmethod
    def draw(self):
        pass


class Interface(ABC):                
# Interface Class

    
    @abstractmethod
    def type(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shapes, Interface):
    
    def __init__(self, a=300, b=200):
        Shapes.__init__(self)
        self.a = a
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def getValue(self):
        return self.l, self.b

    def setVatue(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def draw(self):
        t.forward(self.a)
        t.right(90)
        t.forward(self.b)
        t.right(90)
        t.forward(self.a)
        t.right(90)
        t.forward(self.b)      
        
class Square(Rectangle):

    def __init__(self,s=200):
        Shapes.__init__(self)
        self.a = self.b = s

    def type(self):
        print("It is a 2-D shape")

class Triangle(Shapes, Interface):
    
    def __init__(self, a ,b,c):
        Shapes.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def type(self):
        print("It is a 2-D shape")

    def getsides(self):
        return self.a, self.b,self.c

    def setsides(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return (self.a + self.b + self.c)


    def draw(self):
        if self.c < self.a+self.b and self.a < self.b+self.c and self.b < self.a+self.c :
            
            t.forward(self.a)
            t.left(180-((math.acos((self.a ** 2 + self.b ** 2 - self.c ** 2)/(2 * self.a * self.b))) * (180 / math.pi)))
            t.forward(self.b)
            t.left(180-((math.acos((self.b ** 2 + self.c ** 2 - self.a ** 2)/(2 * self.b * self.c))) * (180 / math.pi)))
            t.forward(self.c)
        else :
            print("not a valid triangle")

    
    
class EquilateralTriangle(Triangle):
    
    def __init__(self, s  = 180):
          self.a = self.b = self.c = s
#polimorphism perimeter function of child is different from parent 
    def perimeter(self):
        return (3 * self.s)

class Pentagon(Shapes, Interface):

    def __init__(self, s = 150):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s
    
    def getside(self):
        return self.s

    def area(self):
        return ((s**2 / 4) * (math.sqrt(5 * (5 + (2*math.sqrt(5))))))

    def perimeter(self):
        return 5 * self.s

    def draw(self):
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)
        t.left(72)
        t.forward(self.s)

class Circle(Shapes, Interface):
    
    def __init__(self, r = 100):
        Shapes.__init__(self)
        self.r = r

    def type(self):
        print("It is a 2-D shape")

    def setradius(self,r):
        self.r = r

    def getradius(self):
        return self.r

    def area(self):
        return math.pi * self.r * self.r

    def perimeter(self):
        return 2 * math.pi * self.r

    def draw(self):
        t.circle(self.r)
    
class Hexagon(Shapes, Interface):

    def __init__(self, s = 100):
        Shapes.__init__(self)
        self.s = s

    def type(self):
        print("It is a 2-D shape")

    def setside(self, s):
        self.s = s

    def getside(self):
        return self.s

    def area(self):
        return (1.5 * math.sqrt(3) * (a**2))

    def perimeter(self):
        return 6 * self.s

    def draw(self):
        t.forward(self.s)
        t.right(60)
        t.forward(self.s)
        t.right(60)
        t.forward(self.s)
        t.right(60)
        t.forward(self.s)
        t.right(60)
        t.forward(self.s)
        t.right(60)
        t.forward(self.s)

class Parallelogram(Shapes, Interface):

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def type(self):
        print("It is a 2-D shape")

    def setter(self, a, b):
        self.a = a
        self.b = b

    def getter(self):
        return self.a, self.b

    def area(self):
        return (b * (a * math.sin(45 * (math.pi / 180))))

    def perimeter(self):
        return 2 * (a + b)

    def draw(self):
        t.forward(self.b)
        t.right(45)
        t.forward(self.a)
        t.right(135)
        t.forward(self.b)
        t.right(45)
        t.forward(self.a)

class Rhombus(Parallelogram):
    def __init__(self , s = 100):
        self.a=self.b = s


class Cone(Shapes, Interface):

    def __init__(self):
        Shapes.__init__(self)
        self.angle = 45
        self.side = 200

    def type(self):
        print("It is a 3-D shape")

    def perimeter(self):
        pass

    def draw(self):
        t.left(90.0 - (self.angle) / 2.0)
        t.forward(self.side)
        t.left(180)
        t.forward(self.side)
        t.right(135)
        t.forward(self.side)
        t.right(self.angle / 2.0)
        t.right(90)
        t.penup()
        t.forward(self.side * math.sin((self.angle / 2) * (math.pi / 180)))
        t.pendown()
        t.left(90)
        t.shape("circle")
        t.shapesize(7.6, 2.5, 1)
        time.sleep(1)
  



