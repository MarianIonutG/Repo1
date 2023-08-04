# Exercitii Obligatorii

# Exercitiul 1

'''
O variabila este metaforic o cutie in care putem stoca diverse valori.
De asemenea este o adresa de memorie alocata uned se pot stoca valori.
'''

# Exercitiul 2 si Exercitiul 3

a = "Tema" # Declarare si initializare variabila de tip STRING
tip_a = type(a)
print(f'Variabila "a" este de tip: {tip_a}')
b = 43 # Declarare si initializare variabila de tip INTEGER
tip_b = type(b)
print(f'Variabila "b" este de tip: {tip_b}')
c = -2.34 # Declarare si initializare variabila de tip FLOAT
tip_c = type(c)
print(f'Variabila "c" este de tip: {tip_c}')
d = True # Declarare si initializare variabila de tip BOOLEAN
tip_d = type(d)
print(f'Variabila "d" este de tip: {tip_d}')

# Exercitiul 4

c = round(c) # Rotunjire valoare din variabila "c" cu functia round() si suprascrierea noii valori rotunjite
print(f'Variabila updatata "c" are acum valoarea {c} si este de tipul de date: {tip_c}')

# Exercitiul 5

print(f'Variabila "a" este de tip {tip_a} si are valoarea {a}')
print(f'Variabila "b" este de tip {tip_b} si are valoarea {b}')
print(f'Variabila "c" este de tip {tip_c} si are valoarea {c}')
print(f'Variabila "d" este de tip {tip_d} si are valoarea {d}')
'''
Dupa rotunjire prin functia round, tipul de date pentru variabila "c" a ramas float, dar ar putea fi
si de tip integer cu actuala valoare. 
Pentru a converti din FLOAT in INTEGER variabila "c" voi folosi functia ,,float" si suprascriere
'''
c_int = int(c)
tip_c_int = type(c_int)
print(f'Variabila "c" este acum de tip {tip_c_int} si are valoarea {c_int}')

# Exercitiul 6

numele = input("Va rugam completati numele dumneavoastra: ")
prenumele = input("Va rugam completati prenumele dumneavoastra: ")
lungime_nume = len(numele)
lungime_prenume = len(prenumele)
print(f'Numele complet are {lungime_nume} caractere')
print(f'Prenumele complet are {lungime_prenume} caractere')

# Exercitiul 7

lungime_dreptunghi = float(input('Va rugam sa introduceti lungimea dreptunghiului: ')) # deoarece orice este dat de la tastatura este vazut ca string, e nevoie de convertirea datelor de intrare in date tip ,,float"
latime_dreptunghi = float(input('Va rugam sa introduceti latimea dreptunghiului: ')) # deoarece orice este dat de la tastatura este vazut ca string, e nevoie de convertirea datelor de intrare in date tip ,,float"

aria_dreptunghi = lungime_dreptunghi * latime_dreptunghi # Aria dreptunghiului este Lungime * Latime
print(f'Aria dreptunghiului este {aria_dreptunghi} ')

# Exercitiul 8 si Exercitiul 9

propozitie ="Coral is either the stupidest animal or the smartest rock"
nr_the = propozitie.count("the") # Folosim metoda "count" pentru a numara de cate ori apare "the" in propozitie
print(f'Cuvantul "the" apare de {nr_the} ori') # Afisam de cate ori apare "the" in propozitie

# Exercitiul 10

'''
Pentru acest exercitiu vom folosi metoda isnumeric pentru a verifaca daca un string contine doar caractere gen cifra (-2 nu ar fi numeric fiindca ,,-" nu e numeric)
Functia va returna True daca va contine doar caractere numere. Deoarece vom folosi assert si stringul nostru nu are 
doar caractere numere va rezulta o eroare cu mesajul ales de noi 'Stringul nu contine doar numere'
'''

assert propozitie.isnumeric() == True, 'Stringul nu contine doar numere'

