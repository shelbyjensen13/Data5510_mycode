'''Hard Question (7 points)

3.Create a class called Pet with attributes name and age.
Implement a method within the class to calculate the age of 
the pet in equivalent human years. Additionally, create a 
class variable called species to store the species of the pet. 
Implement a method within the class that takes the species of the 
pet as input and returns the average lifespan for that species.

- Instantiate three objects of the Pet class with different names, ages,
  and species.
- Calculate and print the age of each pet in human years.
- Use the average lifespan function to retrieve and print the average 
  lifespan for each pet's species.'''

class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def human_age(self):
       if self.species == 'dog':
        return  self.age * 7
       elif self.species == 'cat':
        return self.age * 4
       elif self.species == 'giant tortoise':
        return self.age * .60

    def lifespan(self, species):
      if species == 'dog': # not taking self.species because the question said to take it as input
        return 12
      elif species == 'cat':
        return 15
      elif species == 'giant tortoise':
        return 120

pet1 = Pet('Sally', 3, 'cat')
pet2 = Pet('Jane', 5, 'cat')
pet3 = Pet('Brook', 30, 'giant tortoise')

print(pet1.name, pet1.human_age(), pet1.lifespan(pet1.species))
print(pet2.name, pet2.human_age(), pet2.lifespan(pet2.species))
print(pet3.name, pet3.human_age(), pet3.lifespan(pet3.species))

# https://chatgpt.com/share/6aa611f0-5c28-83ea-939f-957e59b587dc
    