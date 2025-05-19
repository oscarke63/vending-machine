#class Dog:
    #species = "canine"
    #def __init__(self,name,age):
        #self.name = name
        #self.age = age
#dog1 = Dog("Buddy", 3)
#print(dog1.name)
#print(dog1.species)
#print(dog1.age)
#print(dog1.name,dog1.species,dog1.age)
class Dog:
    def __init__(self, name):  # Corrected '__init__'
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")

class Labrador(Dog):  # Single Inheritance
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name} guides the way!")  # Fixed formatting

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()