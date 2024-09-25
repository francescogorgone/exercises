#####versione alternativa: metti la prima parola della lista nella posizione "cambio"

print("Versione alternativa\n")

frase = input("Dimmi una frase \n")

frase = frase.split(" ")

print("Hai scritto", len(frase), "parole")

print("Che parola della tua frase vuoi cambiare?")
cambio = int(input("Fornisci la posizione della parola selezionando un numero \n"))

if cambio > len(frase):
    print("La posizione che hai fornita non è valida")

else:
    if cambio == 0:
        print("La posizione che hai fornita non è valida")
    elif cambio ==1:
        print(frase)
    elif cambio ==2:
        temp = frase[1]
        frase[1] = frase[0]
        frase[0] = temp
        print(frase)
    elif cambio ==3:
        temp = frase[0]
        frase[0] = frase[1]
        frase[1] = frase[2]
        frase[2] = temp
        print(frase)
