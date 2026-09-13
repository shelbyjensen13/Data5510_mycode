'''Easy Question: (3 points)
1.
Create a class called Rectangle with attributes length and width. Implement a
method within the class to calculate the area of the rectangle. Instantiate an object of 
the Rectangle class with length = 5 and width = 3, and print its area.'''

class Rectangle: # creating an object called rectangle
    def __init__(self, length, width): # init is the setup instructions for a new rectangle
        self.length = length # self means this particular object
        # ^the left side - the attribute we're storing in the object
        self.width = width
        #            ^the right side is the value was passed in

    def area(self): # defining the area formula
        return self.length * self.width

rectangle = Rectangle(5,3)

print(rectangle.area())

# https://chatgpt.com/share/6aa6087c-40fc-83e9-814b-f8ffae6f1cb7

