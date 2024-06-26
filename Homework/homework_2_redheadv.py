print("Benvenuto utente\n")

primo = input("Scegli un numero:\n")

secondo = input("Scegline un altro\n")

terzo = input("Ora un terzo\n")

quarto = input("E infine un quarto\n")

somma = int(primo) + int(secondo) + int(terzo) + int(quarto)

print("Hai scelto questi numeri:")
print(primo, secondo, terzo, quarto)
print("Ecco la tua somma:")
print(somma)

print("E se ora ti chiedessi un quinto numero?\n")

quinto = input("Scegli il tuo quinto\n")

print("\nGrazie, il numero da te scelto è stato sottratto da", somma) 

differenza = somma - int(quinto)

print("Ecco il risultato finale:")
print(differenza)

