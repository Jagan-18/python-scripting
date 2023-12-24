class Data:
    num = 3.14
print(Data)



class Data:
    num = 3.14
var = Data()
print(var.num)



class Data:
    def __init__(self, euler_number, pi_number, golden_ratio):
        self.euler_number = euler_number
    self.pi_number = pi_number
    self.golden_ratio = golden_ratio
val = Data(2.718, 3.14, 1.618)
print(val.euler_number)
print(val.golden_ratio)
print(val.pi_number)



class Data:
    def __init__(self, euler_number, pi_number, golden_ratio):
        self.euler_number = euler_number
    self.pi_number = pi_number
    self.golden_ratio = golden_ratio
    def msg_function(self):
        print("The euler number is", self.euler_number)
    print("The golden ratio is", self.golden_ratio)
    print("The pi number is", self.pi_number)
val = Data(2.718, 3.14, 1.618)
val.msg_function()




"""
The following codes are the same as the above codes under the title 'Methods'.
You see that the output is the same, but this codes contain 'classFirstParameter' instead of 'self'.
"""
class Data:
    def __init__(classFirstParameter, euler_number, pi_number, golden_ratio):
        classFirstParameter.euler_number = euler_number
    classFirstParameter.pi_number = pi_number
    classFirstParameter.golden_ratio = golden_ratio
    def msg_function(classFirstParameter):
        print("The euler number is", classFirstParameter.euler_number)
    print("The golden ratio is", classFirstParameter.golden_ratio)
    print("The pi number is", classFirstParameter.pi_number)
val = Data(2.718, 3.14, 1.618)
val.msg_function()






# Creating a class to draw a rectangle
class Rectangle(object):
    # Contructor
    def __init__(self, width, height, color):
        self.width = width
    self.height = height
    self.color = color
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
    plt.axis('scaled')
    plt.show()
# import library to draw the Rectangle
import matplotlib.pyplot as plt
%matplotlib inline
# creating an object blue rectangle
one_Rectangle = Rectangle(20, 10, 'blue')
# Printing the object attribute width
print(one_Rectangle.width)
# Printing the object attribute height
print(one_Rectangle.height)
# Printing the object attribute color
print(one_Rectangle.color)
# Drawing the object
one_Rectangle.drawRectangle()
# Learning the methods that can be utilized on the object 'one_rectangle'
print(dir(one_Rectangle))
# We can change the properties of the rectangle
one_Rectangle.width = 15
one_Rectangle.height = 15
one_Rectangle.color = 'green'
one_Rectangle.drawRectangle()
# Using new variables, we can change the properties of the rectangle
two_Rectangle = Rectangle(100, 50, 'yellow')
two_Rectangle.drawRectangle()





# Creating a class to draw a circle
class Circle(object):
    # Contructor
    def __init__(self, radius, color):
        self.radius = radius
    self.color = color
    # Method
    def increase_radius(self, r):
        self.radius = self.radius + r
    return self.radius
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), self.radius, fc=self.color))
    plt.axis('scaled')
    plt.show()
# import library to draw the circle
import matplotlib.pyplot as plt
%matplotlib inline
# creating an object blue circle
one_Circle = Circle(3.14, 'blue')
# Printing the object attribute radius
print(one_Circle.radius)
# Printing the object attribute color
print(one_Circle.color)
# Drawing the object
one_Circle.drawCircle()
# Learning the methods that can be utilized on the object 'one_rectangle'
print(dir(one_Circle))
# We can change the properties of the rectangle
one_Circle.radius = 15
one_Circle.color = 'green'
one_Circle.drawCircle()
# Using new variables, we can change the properties of the rectangle
two_Circle = Circle(100, 'yellow')
print(two_Circle.radius)
print(two_Circle.color)
two_Circle.drawCircle()
# Changing the radius of the object
print('Before increment: ',one_Circle.radius)
one_Circle.drawCircle()
# Increment by 15 units
one_Circle.increase_radius(15)
print('Increase the radius by 15 units: ', one_Circle.radius)
one_Circle.drawCircle()
# Increment by 30 units
one_Circle.increase_radius(30)
print('Increase the radius by 30 units: ', one_Circle.radius)
one_Circle.drawCircle()






class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi_number = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are special.'
special_numbers = SpecialNumbers()
print('The euler number is', getattr(special_numbers, 'euler_number'))
print('The golden ratio is', special_numbers.golden_ratio)
print('The pi number is', getattr(special_numbers, 'pi_number'))
print('The message is ', getattr(special_numbers, 'msg'))



class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are special.'

    def parameter(self):
        print(self.euler_constant, self.euler_number, self.pi, self.golden_ratio, self.msg)
special_numbers = SpecialNumbers()
special_numbers.parameter()
delattr(SpecialNumbers, 'msg') # The code deleted the 'msg'.
special_numbers.parameter() # Since the code deleted the 'msg', it returns an AttributeError



class ComplexNum:
    def __init__(self, a, b):
        self.a = a
    self.b = b
    def data(self):
        print(f'{self.a}-{self.b}j')
var = ComplexNum(3.14, 1.618)
var.data()



class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species

    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
#Use the Data class to create an object, and then execute the microorganism method
value = Data('Aspergillus', 'niger')
value.microorganism()





class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    pass
value = Recombinant('Aspergillus', 'sojae')
value.microorganism()






class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    def __init__(self, genus, species):
        Data.__init__(self, genus, species)
value = Recombinant('Aspergillus', 'sojae')
value.microorganism()




class SpecialNumbers(object):
    def __init__(self, special_numbers):
        print('6 and 28 are', special_numbers)
class PerfectNumbers(SpecialNumbers):
    def __init__(self):

    # call superclass
    super().__init__('perfect numbers.')
    print('These numbers are very special in mathematik.')
nums = PerfectNumbers()





class Animal(object):
    def __init__(self, AnimalName):
        print(AnimalName, 'lives in a farm.')

class Cow(Animal):
    def __init__(self):
        print('Cow gives us milk.')
    super().__init__('Cow')

result = Cow()




class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    def __init__(self, genus, species):
        super().__init__(genus, species) # 'self' statement in this line was deleted as different from the above codes
value = Recombinant('Aspergillus', 'sojae')
value.microorganism()




class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    def __init__(self, genus, species):
        super().__init__(genus, species)
    self.activity = 2500 # This information was adedd as a Property
value = Recombinant('Aspergillus', 'sojae')
print(f'The enzyme activity increased to {value.activity} U/mL.')



class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    def __init__(self, genus, species, activity):
        super().__init__(genus, species)
    self.activity = activity # This information was adedd as a Property
value = Recombinant('Aspergillus', 'sojae', 2500)
print(f'The enzyme activity increased to {value.activity} U/mL.')




class Data:
    def __init__(self, genus, species):
        self.genus = genus
    self.species = species
    def microorganism(self):
        print(f'The name of a microorganism is in the form of {self.genus} {self.species}.')
class Recombinant(Data):
    def __init__(self, genus, species, activity):
        super().__init__(genus, species)
    self.activity = activity # This information was adedd as a Property

    def increment(self):
        print(f'With this new recombinant {self.genus} {self.species} strain, the enzyme activity increased 2-times with {se
value = Recombinant('Aspergillus', 'sojae', 2500)
value.increment()





