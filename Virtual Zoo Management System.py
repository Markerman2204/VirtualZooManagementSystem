import random
#list for stuff

animalnames = []
animalspecies = []
animalages = []
animalweights = []
animalhealth = []

def add_animal():

    #input variabes
    name = input("Enter the animal name\n ")
    species = input("Enter the animal species\n")
    age = int(input("Enter the animal age\n"))
    while age < 1 or age > 50:
        age = int(input("Invalid. Enter the animal age\n"))
    weight = float(input("Enter the animal weight\n"))
    while weight < 0.1 or weight > 1000:
        weight = float(input("Invalid. Enter the animal weight\n"))
    #print the names
    print("Name :", name)
    print("Species :", species)
    print("Age :", age)
    print("Weight :", weight)

    animalnames.append(name)
    animalspecies.append(species)
    animalages.append(age)
    animalweights.append(weight)
    animalhealth.append("Healthy")

def view_animal():

    #check if there's any animals
    if len(animalnames)==0:
        print("no animal\n")
        return

    #now we print the animals in list
    for i in range (len(animalnames)):
        print(f"Animal{i+1}:")
        print(f"Name: {animalnames[i]}")
        print(f"Species: {animalspecies[i]}")
        print(f"Age: {animalages[i]} years")
        print(f"Weight: {animalweights[i]} kg")

def data():
    if len(animalnames)==0:
        print("no animal\n")
        return

    total_animals = len(animalnames)
    total_weight = sum(animalweights)
    heaviest_weight = max(animalweights)
    lightest_weight = min(animalweights)

    print("Total number of animals:", total_animals)
    print("Total weight of all animals:", total_weight)
    print("Heaviest animal weight:", heaviest_weight)
    print("Lightest animal weight:", lightest_weight)

def feed():
    if len(animalnames) == 0:
        print("No animals to feed.\n")
        return
    for i in range(len(animalnames)):
        print(f"{i + 1}. {animalnames[i]} ({animalspecies[i]})")

        # Ask which animal
    choi = int(input("Animal id for the one you want to feed: "))
    if choi <= len(animalnames):
        print(f"You fed it food.")
        animalhealth[choice - 1] = "Healthy"
    else:
        print("Invalid animal number.")

def checkhealth():
    if len(animalnames) == 0:
        print("No animals.\n")
        return
    for i in range(len(animalnames)):
        print(f"{i + 1}. {animalnames[i]} ({animalspecies[i]})")

    cho = int(input("Animal id for the one you want to check health: "))
    if len(animalnames) == 0:
        print("No animals to feed.\n")
        return
    if cho <= len(animalnames):
        new_health = input("Enter new health status (Healthy/Sick/Injured): ")
        animalhealth[cho - 1] = new_health
    else:
        print("Invalid animal number.")

#menu to do stuff
while True:

    print("1. Register new animal")
    print("2. View all animals")
    print("3. Show statistics")
    print("4. Exit")
    print("5. Feed")
    print("6. Check Health")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_animal()
    elif choice == "2":
        view_animal()
    elif choice == "3":
        data()
    elif choice == "4":
        break
    elif choice == "5":
        feed()
    elif choice == "6":
        checkhealth()
    else:
        print("no,pick 1-4\n")