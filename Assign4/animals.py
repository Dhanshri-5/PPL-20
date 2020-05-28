from abc import ABC, abstractmethod

class Animal(ABC):              
#A class with both abstract and concrete methods are called as Abstract classes

    def __init__(self):
        _name = ''
        _sound = ''

    def Legs(self):
        print("It has 4 legs.")
    @abstractmethod
    def getName(self):
        pass
    @abstractmethod
    def getSound(self):
        pass
    @abstractmethod
    def setName(self, name):
        pass
    @abstractmethod
    def setSound(self, sound):
        pass


class Interface(ABC):                      
# A class with only abstractmethods and no concrete methods are called as Interface classes.
   
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def is_extinct(self):
        pass
#animal = Animal()  generates error as class is abstract

class Cat(Animal):                                                              
    #constructor
    def __init__(self):
        self._name = 'Cat' #protected attribute
        self._sound = 'Meow'
                
    def eats(self):
        print('It likes to eats meat and fish')

    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")

    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound
    def describe(self):
        self.getName()
        self.getSound()
        self.Legs()
        self.eats()
        print('\n')


class Lion(Cat , Interface):
# Heirarchical inhertance from Cat which inherits from Animals

    #constructor
    def __init__(self):
        self._name = 'Lion' #protected attribute
        self._sound = 'Roar'

    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")

    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of Lion is Grayish Yellow!")
    def is_extinct(self):
        print("No, Lion is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.eats()
        print('\n')


class Tiger(Cat , Interface):
    #constructor
    def __init__(self):
        self._name = 'Tiger' #protected attribute
        self._sound = 'Roar'
    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")
    
    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound
    
    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of Tiger is Yellow-Brown!")
    def is_extinct(self):
        print("Tiger is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.eats()
        print('\n')


class Cheetah(Cat , Interface):
    #constructor
    def __init__(self):
        self._name = 'Cheetah' #protected attribute
        self._sound = 'Roar'
    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")
    
    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of Cheetah is Yellow-Brown!")
    def is_extinct(self):
        print("Cheetah is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.eats()
        print('\n')

class SaberTooth(Cat , Interface):

    def __init__(self):
        self._name = 'SaberTooth'
        self._sound = 'Roar'

    # A virtual method eats()
    def eats(self):                                   # Overriding eats method of the class Cat. Showing Polymorphism.
        print("A saber-tooth cat used to eat meat from other animals!")

        #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")
    
    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of Saber-Tooth was Yellow, Brown, Black, White!")
    def is_extinct(self):
        print("SaberTooth is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.eats()
        print('\n')

class Canidae(Animal):
    def __init__(self):
        self._name = "Canid"
        self._sound = 'Howling'
    def habitat(self):
        print('Its found in all continents except Antartica.')

    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")

    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound
    def describe(self):
        self.habitat()

class Dog(Canidae , Interface):

    #constructor
    def __init__(self):
        self._name = 'Dog' #protected attribute
        self._sound = 'Bark'
    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")

    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

    
    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of Dog is Brown, Black, White!")
    def is_extinct(self):
        print("Dog is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.habitat()
        print('\n')

        
class Wolf(Interface , Canidae):
    #constructor
    def __init__(self):
        self._name = 'Wolf' #protected attribute
        self._sound = 'Howl'

    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")

    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

        
    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Wolf is brown in colour")
    def is_extinct(self):
        print("Wolf is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        self.habitat()
        print('\n')

class PolarBear(Animal , Interface):
    #constructor
    def __init__(self):
        self._name = 'PolarBear' #protected attribute
        self._sound = 'Growl'
    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")
    def setName(self, name):
        self._name = name
    def setSound(self, sound):
        self._sound = sound

    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Polar Bear is white in colour")
    def is_extinct(self):
        print("Polar bear is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        print('\n')


class Monkey(Animal, Interface):

    def __init__(self):
        self._name = 'Monkey'
        self._sound ='Screech , Chatter'

    def eats(self):
        print("Monkey eats vegetables and fruits")
    #implementing abstract base class methods
    def getName(self):
        print("The animal is", self._name)
    def getSound(self):
        print(self._name, self._sound + "sound.")
    def setName(self, name):
        self._name = name

    def setSound(self, sound):
        self._sound = sound
    def getSound(self):
        print("A Monkey makes " + self._sound + " sound.")

    def Legs(self):
        print("It has 4 legs.")
    def color(self):
        print("Color of monkey is brown")
    def is_extinct(self):
        print("No, Monkey is not extinct.")
    def describe(self):
        self.getName()
        self.getSound()
        self.color()
        self.Legs()
        self.is_extinct()
        print('\n')

