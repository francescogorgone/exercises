# Chiedere una frase all'utente e stampare il numero di parole
# che contiene (consideriamo lo spazio come separatore di parola)

frase = input("Dimmi una frase \n")

frase = frase.split(" ")

print("Hai scritto", len(frase), "parole")

# Poi chiedere all'utente quale parola vuole cambiare.
# L'utente fornirà la posizione della parola
# (verificare che sia una posizione esistente)
# Scambiare la prima parola della frase con la parola nella posizione fornita dall'utente.
# Esempio: 'Ciao come stai?' fornendo 2 diventa 'come Ciao stai?'
# Fare dunque attenzione alla distizione fra indici e posizioni. 

print("Che parola della tua frase vuoi cambiare?")
cambio = int(input("Fornisci la posizione della parola selezionando un numero \n"))

if cambio > len(frase):
    print("La posizione che hai fornita non è valida")
    
else:
    if cambio == 0:
       print("La posizione che hai fornita non è valida")
    elif cambio ==1:
        print(frase)
    elif cambio == 2:
        temp = frase[1]
        frase[1] = frase[0]
        frase[0] = temp
        print(frase)
    elif cambio == 3:
        temp = frase[2]
        frase[2] = frase[1]
        frase[1] = frase [0]
        frase[0] = temp
        print(frase)
