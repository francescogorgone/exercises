#####################################################
# Questi esercizi NON sono generici. Non sappiamo ancora trattare le liste con generalità e dinamicità, ma vogliamo allenarci a scrivere codice che coinvolga le liste.

# Modificare l1 in modo che l'i-esimo elemento di l1 risulti sé stesso meno l'i-esimo elemento di l2.
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [2, 2, 2, 5] #lunghezza fissa, valori variabili

l1[0] = l1[0]-l2[0]
l1[1] = l1[1]-l2[1]
l1[2] = l1[2]-l2[2]

print(l1,l2)

# Modificare l1. Raddoppiare l'i-esimo elemento di l1 se e solo se l'i-esimo elemento di l2 è uguale a 1
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [1, 0, 0] #lunghezza fissa, valori variabili

if l2[0] == 1:
    l1[0] = l1[0]*2
if l2[1] == 1:
    l2[1] = l2[1]*2
if l2[2] == 1:
    l2[2] = l2[2]*2

print(l1,l2)

# Creare una lista l3 che contenga tutti e soli gli elementi comuni sia a l1 che a l2
l1 = [2, 3, 4] #lunghezza fissa, valori variabili
l2 = [4, 2, 5] #lunghezza fissa, valori variabili

l3 = []

if l1[0] in l2:
    l3.append(l1[0])
if l1[1] in l2:
    l3.append(l1[1])
if l1[2] in l2:
    l3.append(l1[2])

print(l3)

# Costruire la lista l3 che è la somma elemento per elemento delle liste l1 ed l2.
# Mettere a zero l'i-esimo elemento di l3 se l'i-esimo elemento di l2 è 1.

# Soluzione 1

l1 = [7, 8, 9]
l2 = [0, 1, 0]

l3 = []

l3 = [l1[0] + l2[0], l1[1] + l2[1], l1[2] + l2[2]]

if l2[0] == 1:
    l3[0] = 0
if l2[1] == 1:
    l3[1] = 0
if l2[2] == 1:
    l3[2] = 0

print(l3)

# Soluzione 2 usare append e non puoi usare l'assegnamento

l1 = [7, 8, 9]
l2 = [0, 1, 0]

l3 = []

l3.append(l1[0]+l2[0])
l3.append(l1[1]+l2[1])
l3.append(l1[2]+l2[2])

if l2[0] == 1:
    l3[0].append(0)
if l2[1] == 1:
    l3[1] = 0
if l2[2] == 1:
    l3[2] = 0

print(l3)
