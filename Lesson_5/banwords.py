# Esempio di software. Detector di parole bannabili, implementato in una chat di Twitch
# Ogni messaggio viene controllato e se contiene una parola bannabile viene scartata
# Chiedere messaggio all'utente e stampare il messaggio se non è bannabile, un messaggio di alert se lo è

p1 = "sentret"
p2 = "piedi"
p3 = "kick"
p4 = "clown"
p5 = "pagliaccio"
p6 = "nparola"

# esecuzione esercizio

banwords = [p1, p2, p3, p4, p5, p6]

messaggio = input("Benvenuto in chat, scrivi un messaggio: \n")

if p1 in messaggio.lower() or p2 in messaggio.lower() or p3 in messaggio.lower() or p4 in messaggio.lower() or p5 in messaggio.lower() or p6 in messaggio.lower() :
    print("Parola bannata individuata, il tuo messaggio non è stato inoltrato")
else:
    print(messaggio)


# miglioro l'esercizio precedente

banwords = ["sentret", "piedi", "kick", "clown", "pagliaccio", "nparola"]

messaggio = input("Benvenuto in chat, scrivi un messaggio: \n")

if messaggio.lower() in banwords:
    print("Parola bannata individuata, il tuo messaggio non è stato inoltrato")
else:
    print(messaggio)









