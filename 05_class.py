#Define a class which has at least two methods:

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class MyClass():
    def __init__(self):
        pass

    def getString(self):
        self.text = input("Enter some text: ")

    def printString(self):
        print(self.text.upper())

m1 = MyClass()
m1.getString()
m1.printString()