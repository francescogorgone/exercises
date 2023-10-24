#loop
#dizionari e liste
#funzioni



#loop (while)

name = input("Insert name: ")


while len(name) < 1:
    print("Name is wrong")
    name = input("Insert name: ")


surname = input("Insert surname: ")

while len(surname) < 1:
    print("Surname is wrong")
    surname = input("Insert surname: ")

age = int(input("Insert age: "))

while age < 18:
    print("u smol")
    age = int(input("Insert age: "))


if (name > str(1)):
    if (surname > str(1)):
        if (age >= (18)):
            print("Benvenuto, dacci tutti i tuoi soldi :)")
            
            name_cap = name.capitalize()
            surname_cap = surname.capitalize()

            print(name_cap, surname_cap, age)








    
