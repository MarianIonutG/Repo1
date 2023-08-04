# Exercitiul 1 de la tema optionala

a = input("Introduceti de la tastatura un string impar: ") # se citeste de la tastatura un string de dimensiune impara
lungime = len(a) # se declara si se atribuie variabilei "lungime" dimensiunea stringului introdus de la tastatura
ind_mij = int((len(a)-1) / 2) # se declara si se atribuie variabilei "ind_mij" indexul din mijlocul stringului "a". Se foloseste formula (lungime string - 1) / 2. In acelasi timp se converteste valoarea in integer
print(a[ind_mij]) # Se printeaza valoarea de la indexul "ind_mij" (de la indexul din mijlocul stringului "a")

# Exercitiul 2 de la tema optionala

a = input("Introduceti un string de la tastatura: ") # se citeste de la tastura un string
inv_a = a[::-1] # se declara si se atribuie variabilei "inv_a" stringul inversat introdus de la tastatura.
assert a == inv_a, "Acesta nu este un palindrom! " #cu assert se verifica daca stringul introdus de la tastatura este la fel cu cel inversat si in caz de inegalitate se va afisa mesajul "Acesta nu este un palindrom! "

# Exercitiul 3 de la tema optionala

a = input("Scrieti doua cuvinte: "); ind_a = a.find(' '); unu = a[0:ind_a]; doi = a[(ind_a+1):len(a)]; print(unu); print(doi)
''' 
Se introduce de la tastatura cu "input" un string compus din doua cuvinte separate de spatiu " ". Prima data cautam primul spatiu " " din stringul introdus si indexul lui se salveaza in ind_a.
Dupa, salvam in variabila "unu" primul cuvant inainte de spatiu care va fi sirul de caractere de la indexul 0 pana la indexul spatiului. Dupa salvam in variabila "doi" cel de-al doilea cuvant
de dupa spatiu. Acesta va fi la nivel de string introdus de la indexul + 1 al spatiului pana la dimensiunea stringului introdus. Dupa se afiseaza pe rand atat primul cuvant cat si cel de-al 
doilea. De mentionat ca in python putem scrie codul pe o singura linie daca folosim ";" ca separator dupa fiecare actiune. Secventa se va executa de la stanga la dreapta.
'''

# Exercitiul 4 de la tema optionala

x = input("Introduceti un sir de caractere: ") # Se introduce un sir de caractere de la tastatura cu input
caracter = x[0] # se declara si atribuie variabilei "caracter", valoarea primului caracter din stringul introdus
inlocuieste = x.replace(caracter, caracter.upper()) # cu functia "replace" se inlocuieste fiecare caracter (stocat in variabila caracter) si este inlocuit de aceeasi litera dar scrisa cu majuscula (ex.: in loc de "a" vom avea "A"). Functia "upper" realizeaza transformarea din litera mare in litera mica
first_low = inlocuieste[0].lower() # Prima litera din sirul de caracter ar fi tot cu litera mare, dar noi decidem sa o convertim in litera mica prin indicarea indexului 0 si practic functia upper este folosita acum doar pentru primul caracter din sirul introdus de la tastatura
latest_low = inlocuieste[-1].lower() # Daca ultima litera ar fi fost aceeasi ca primul caracter, acesta ar fi ramas cu litera mare, dar decidem sa il facem cu litera mica folosit aceeasi metoda "lower" si indicata doar la indexul final (-1 reprezinta ultima litera din string)
rezultat = first_low + inlocuieste[1:(len(inlocuieste)-1)] + latest_low # Acum rezultatul final va fi o concatenare dintre prima litera, continutul stocat si ultima litera
print(rezultat) # se va afisa rezultatul obtinut

# Exercitiul 5 de la tema optionala

user = input("Introduceti un username: ") # Se introduce de la tastatura un username
parola = input("Introduceti o parola: ") # Se introduce de la tastatura o parola
x = parola.replace(parola,"*" * (len(parola))) # In variabila "x" inlocuim parola tastata cu un numar de "*" prin multiplicarea caracterului cu lungimea parolei
lung = len(x) # In variabila "lung" stocam lungimea parolei
print(f'Parola pentru user {user} este {x} si are {lung} caractere') # Se afiseaza mesajul folosind valoarea variabilei "user" (introduse de la tastatura) si a variabilei "lung" (dimensiunea parolei). "x" reprezinta conversia parolei intr-un sir de "*".