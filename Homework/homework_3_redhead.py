# Creare una applicazione bancaria che permette di effettuare un prelievo o deposito monetario. 

# 1. Effettuare il login chiedendo separatamente nome utente e password. Ci sono solo due utenti registrati. Se il nome utente o la password sono errati (la coppia non è corretta, oppure il nome utente non esiste), dare un messaggio di errore e terminare il programma.

# 2. Se il login è corretto, stampare il bilancio del conto e chiedere se l'operazione desiderata è prelievo o deposito. Qualunque altro inserimento risulta nella terminazione del programma con un messaggio di errore.
# op = input("Prelievo o deposito?") 

# 3. Se l'operazione è di deposito, chiedere la cifra (si assuma che l'utente inserisca un intero), aggiornare il totale del conto e stamparlo a video terminando così il programma.

# 4. Se l'operazione è di prelievo, chiedere la cifra (si assuma che l'utente inserisca un intero) e verificare che il bilancio sia sufficente. Se lo è detrarlo dal totale e stampare il nuovo bilancio a video terminando così il programma. Se non lo è terminare il programma con un messaggio di errore.

print("Benvenuto nel portale di Banca dei Grandi Soldi")

#database

user1 = "Francesco"
psw1 = "nonteladico"
bilancio1 = 2000

user2 = "Nurberto"
psw2 = "dogmeat"
bilancio2 = 10000

#login

nome_utente = input("Inscerisci il tuo nome utente: \n")
password = input("Inserisci la tua password \n")

#verifico che l'utente sia registrato e la password corrisponda

isuser1 = nome_utente == user1 and password == psw1
isuser2 = nome_utente == user2 and password == psw2

if isuser1 or isuser2:
	print("Benvenuto/a", nome_utente)

	#scelgo il bilancio basandomi sull'utente
	if isuser1:
		bilancio = bilancio1
	else:
		bilancio = bilancio2

	print("Il tuo bilancio è:", bilancio)

	prelievo = "prelevare"
	deposito = "depositare"

	operazione = input('Desideri "prelevare o depositare"? \n')
	operazione_prelievo = operazione == prelievo
	operazione_deposito = operazione == deposito
	if operazione_prelievo:
		importo = input("Quando desideri prelevare? \n")
		if int(importo) <= bilancio:
			nuovobilancio = bilancio - int(importo)
			print("Il tuo nuovo bilancio è:", nuovobilancio)
			if isuser1 or isuser2:
					if isuser1:
						bilancio1 = nuovobilancio
					else:
						bilancio2 = nuovobilancio
		else:
			print("Credito insufficiente")
	
	elif operazione_deposito:
		importo = input("Quando desideri depositare? \n")
		nuovobilancio =  bilancio + int(importo)
		print("Il tuo nuovo bilancio è:", nuovobilancio)
		if isuser1 or isuser2:
			if isuser1:
				bilancio1 = nuovobilancio
			else:
				bilancio2 = nuovobilancio
	else:
		print("Operazione sconosciuta")

else:
	print("Nome utente invalido o inesistente o password errata")

print("FINALE")
print("Francesco: ", bilancio1)
print("Nurberto: ", bilancio2)
