# Scrivi un programma in Python che chieda all'utente il suo reddito annuo e calcoli l'ammontare delle tasse dovute basandosi su semplici fasce di reddito.

# Prima di tutto chiedere all'utente il suo nome e cognome in una sola stringa (usando cioè un solo input).
# Se il suo nome o cognome includono "Pagliaccio" (indipendentemente dalle maiuscole), allora stampare direttamente "Sei nulla tenente, popi popi" e chiudere il programma.
# Altrimenti procedere come segue:

# Redditi fino a 10.000 €: esenti da tasse.
# Redditi superiori a 10.000 € e fino a 20.000 €: tassati al 10%.
# Redditi superiori a 20.000 € e fino a 30.000 €: tassati al 20%.
# Redditi superiori a 30.000 €: tassati al 30%.
# Il programma dovrebbe mostrare l'ammontare delle tasse dovute secondo queste regole.

print("Benvenuto nel Reddittometro :) \n")

nomi = input("Inserisci il tuo nome e cognome: \n")

if "pagliaccio" in nomi.lower():
    print("Sei nulla tenente, popi popi")

else:

    redditoannuo = input("Inserisci il tuo reddito annuo: \n")
    reddito = int(redditoannuo)

    if int(reddito) < 10000:
        tasse = reddito * 0

    if reddito >= 10000 and reddito <= 20000:
        tasse = reddito / 100 * 10

    elif reddito >= 20000 and reddito <= 30000:
        tasse = reddito / 100 * 20

    elif reddito >= 30000:
        tasse = reddito / 100 * 30

    tasse = int(tasse)

    print("Le tasse che devi versare equivalgono a: \n")
    print(tasse)
