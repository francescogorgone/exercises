# Creare un programma che analizzi tre interi forniti dall'utente. 

# PARTE 1 #
# Prima di tutto chiedere il nome dell'utente. Se l'utente non ha scritto il nome con la maiuscola nella prima lettera, sostituirla.
# PS: x.isupper() controlla se una variabile è maiuscola. 
# Stampare un messaggio di benvenuto usando il nome utente eventualmente corretto


# PARTE 2 #
# Poi, in un solo input, chiedere due numeri separati da virgola Esempio: 3,2
# In un successivo input, chiedere il terzo intero

# Ospitare tutti i numeri in una lista,
# - stamparli uno per uno
# - stampare la media

# Eseguire i controlli (per ogni controllo dare un feedback all'utente tramite una stampa)
# - Verificare se il terzo numero sia maggiore della somma degli altri due
# - Verificare se i tre numeri sono tutti diversi fra loro
# - Verificare se la somma dei tre numeri è maggiore o minore al numero di caratteri nel nome dell'utente

nome = input ("Benvenuto, inserisci il tuo nome utente \n")

#non è necessario scrivere l'if, basta capitalizzare direttamente
if nome.isupper():
    print("Benvenuto", nome)
else:
    nome = nome.capitalize()
    print("Benvenuto", nome)

numeri1 = input('Inserisci due numeri interi minori di 10, separati da virgola "," per favore \n')

numeri2 = input("Inserisci un terzo numero intero minore di 10 per favore \n")

l = numeri1.split(",") # "4,5" --> ["4", "5"]

l.append(numeri2) # ["4", "5", "9"]

print("Il primo numero è: ", l[0])
print("Il secondo numero è: ", l[1])
print("Il terzo numero è: ", l[2])

media = ((int(l[0]) + int(l[1]) + int(l[2])) / 3) #meglio scrivere così che sum(lista) / 3 perché se la lista non fosse composta da tre
#elementi il denominatore sarebbe sbagliato, quindi non è scritta in modo generale.
#il modo corretto sarebbe stato sum(lista) / len(lista)
#oppure direttamente la funzione per fare la media mean(lista)

print("La media dei tre valori da te forniti è: ", media)

print("Ecco alcune considerazioni sui valori da te inseriti: \n")

#controllo1

if int(l[2]) > (int(l[0]) + int(l[1])):
    print("Il terzo valore da te inserito è maggiore della somma dei primi due \n")
else:
    print("Il terzo valore da te inserito non è maggiore della somma dei primi due \n")

#controllo2

if int(l[0]) != int(l[1]) != int(l[2]):
    print("Tutti i valori da te inseriti sono differenti tra loro \n")
else:
    print("I valori da te inseriti non sono tutti differenti tra lor \n")

#controllo3

if int((int(l[0]) + int(l[1]) + int(l[2])) > int(len(nome))):
    print("La somma dei numeri da te forniti è maggiore del numero di caratteri del tuo nome utente: \n")
else:
    print("La somma dei numeri da te forniti non è maggiore del numero di caratteri del tuo nome utente \n")
