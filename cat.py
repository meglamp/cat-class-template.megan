#Revmoe pass and complete the cat class
class Cat():
    def __init__ (self):
        self.name = "Unknown"
        self.age = 0
    def speak(self):
        return("Meow")
    
stella = Cat()
stella.name = "Stella"
stella.age = 7

garfield = Cat()
garfield.name = "Garfield"
garfield.age = 50

print(stella.speak)
print(garfield.speak)

#Create objects here
#These should NOT be indented inside the class

