# File name = pet_main.py
import pet # Name of the class file we are going to use
def main():
    my_pet1 = pet.Pet("Tegan", "Dog", 7)
    my_pet2 = pet.Pet("Felix", "Cat", 3)
    my_pet3 = pet.Pet("Ralph", "Parrot", 2)
 # Display the information
    print(f'Pet1: [Name: {my_pet1.name} Type: {my_pet1.animal_type} Age:{my_pet1.age}]')
    print(f'Pet2: [Name: {my_pet2.name} Type: {my_pet2.animal_type} Age:{my_pet2.age}]')
    print(f'Pet3: [Name: {my_pet3.name} Type: {my_pet3.animal_type} Age:{my_pet3.age}]')
# Call the main function
main()