dic = {"name" : "francesco" , "nickname" : "grg"}

print(dic["name"])

##compito1

#dichiarare due liste di numeri con 5 elementi ciascuna e creare una lista concatenata che le includa entrambe

list1 = [0, 1, 2, 3, 4]
list2 = [5, 6, 7, 8, 9]

list_tot = [list1 + list2]

print(list_tot)

#bonus: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno
##compito 1.5

#dichiarare una lista e stamparne il reverse (senza usare altre variabili).

list3 = [1, 2, 3]
list3.reverse()
print(list3) 

##compito 2
#modifichiamo l'esercizio del casinò in un registro degli utenti del suddetto. Creare una interfaccia da terminale per aggiungere N utenti
#e salvare ciscuno in un dizionario (e dunque in una lista che li contenga tutti). Il programma deve rifiutare un'inserzione
#se il nickname di uno degli utenti è già presente nel dizionario.

#Finita l'inserzione creare un modulo statistico che analizzi i dati inseriti nel sistema.
#In particolare si vuole sapere:
#la percentuale di maschi e di femmine e l'età massima, minima e media dei registrati.

#Struttura utente:
# Nickname
# Età
#Gender

#si suggerisce di utilizzare le strutture di supporto adatte alla risoluzione del problema, come ad esempio liste temporanee

#INIZIO

listautenti = []

#UTENTE1

nickname1 = input("Insert nickname: ")

if nickname1 in listautenti:
    print("nickname alredy registered")

while len(nickname1) < 1:
    print("Nickname is wrong")
    nickname1 = input("Insert nickname: ")

age1 = int(input("Insert age: "))

while age1 < 18:
    print("u smol")
    age1 = int(input("Insert age: "))

genderlist = [str("male"), str("female")]

gender1 = input("Insert gender: ")

while (gender1 not in genderlist):
    print("gender not defined")
    gender1 = input("Insert gender: ")

nickname1_cap = nickname1.capitalize()
gender1_cap = gender1.capitalize()

if nickname1 in [user['Nickname'] for user in listautenti]:
    print("Nickname already registered")
else:
    print("Benvenuto, dacci tutti i tuoi soldi :)")
    user1 = {"Nickname": nickname1, "Age": age1, "Gender": gender1}
    listautenti.append(user1)

print(user1)

#UTENTE2

nickname2 = input("Insert nickname: ")

if nickname2 in listautenti:
    print("nickname alredy registered")

while len(nickname2) < 1:
    print("Nickname is wrong")
    nickname2 = input("Insert nickname: ")

age2 = int(input("Insert age: "))

while age2 < 18:
    print("u smol")
    age2 = int(input("Insert age: "))

gender2 = input("Insert gender: ")

while (gender2 not in genderlist):
    print("gender not defined")
    gender2 = input("Insert gender: ")

if nickname2 in [user['Nickname'] for user in listautenti]:
    print("Nickname already registered")
else:
    print("Benvenuto, dacci tutti i tuoi soldi :)")
    user2 = {"Nickname": nickname2, "Age": age2, "Gender": gender2}
    listautenti.append(user2)

print(user2)

#UTENTE3

nickname3 = input("Insert nickname: ")

if nickname3 in listautenti:
    print("nickname alredy registered")

while len(nickname3) < 1:
    print("Nickname is wrong")
    nickname3 = input("Insert nickname: ")

age3 = int(input("Insert age: "))

while age3 < 18:
    print("u smol")
    age3 = int(input("Insert age: "))

genderlist = [str("male"), str("female")]

gender3 = input("Insert gender: ")

while (gender3 not in genderlist):
    print("gender not defined")
    gender3 = input("Insert gender: ")

nickname3_cap = nickname3.capitalize()
gender3_cap = gender3.capitalize()

if nickname3 in [user['Nickname'] for user in listautenti]:
    print("Nickname already registered")
else:
    print("Benvenuto, dacci tutti i tuoi soldi :)")
    user3 = {"Nickname": nickname3, "Age": age3, "Gender": gender3}
    listautenti.append(user3)

print(user1)

#FINALE

print(listautenti)

#Modulo statistico

#Calcola la percentuale di maschi e femmine

male_count = sum(user["Gender"] == "male" for user in listautenti)

female_count = sum(user["Gender"] == "female" for user in listautenti)

total_users = len(listautenti)

male_percentage = (male_count / total_users) * 100
female_percentage = (female_count / total_users) * 100

print(f"Percentage of males: {male_percentage}%")

print(f"Percentage of females: {female_percentage}%")

#Calcola età massima, minima e media

ages = [user["Age"] for user in listautenti]

max_age = max(ages)
min_age = min(ages)
avg_age = sum(ages) / total_users

print(f"Maximum age: {max_age}")
print(f"Minimum age: {min_age}")
print(f"Average age: {avg_age}")
