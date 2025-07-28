#Challenge Python Jour 3
#numero 1
age = 19

#numero 2
taille = 1.55

#numero
complexe = 3 + 2j

#numero 4
base = int(input("Entrez la base: "))
hauteur = int(input("Entrez la hauteur: "))
print(f"La zone du triangle est de {base * hauteur * 0.5}")

#numero 5
A = int(input("Entrez le côté A: "))
B = int(input("Entrez le côté B: "))
C = int(input("Entrez le côté C: "))
print(f"Le périmètre du triangle est {A + B + C}")

#numero 6
longueur = int(input("Entrez la longueur: "))
largeur = int(input("Entrez la largeur: "))
print(f"La surface du rectangle est {longueur * largeur}")
print(f"Le périmètre du rectangle est {2 * (longueur + largeur)}")

#numero 7
pi = 3.14
rayon= int(input("Entrez le rayon : "))
print(f"La zone du cercle est {pi * rayon * rayon}")
print(f"La circonférence du cercle est {2 * pi * rayon}")

#numero 8

#numero 9

#numero 10

#numero 11
x = -3
c = x**2 + 6 * x + 9
print(f"c = {c}")

#numero 12
print(f"la longueur de 'Pyton' est : {len("Python")}")
print(f"la longueur de 'Dragon' est : {len("Dragon")}")
print(len("pyton") < len("dragon"))

#numero 13
print('on' in 'python' and 'on' in 'dragon')

#numero 14
print('jargon' in 'I hope this course is not full of jargon')

#numero 15
print('on' not in 'python' and 'on' not in 'dragon')

#numero 16
length = len("python")
print(float(length))
print(str(length))

#numero 17
number = 13
if number % 2 == 0:
    print("le nombre est pair")
else:
    print("le nombre est impair") 

#numero 18
print(7 // 3 == int(2.7))

#numero 19
print(type('10') == type(10))

#numero 20
print(int('9.8') == 10)

#numero 21
heure = int(input("Entrez les nombre d'heures"))
taux = int(input("Saisir le taux par heure"))
print(f"Votre gain hebdomadaire est {taux * heure}")

#numero 22
nb_annee = int(input("Entrez le nombre d'années que vous voulez faire sur la terre"))
print(f"vous vivrez pendant {nb_annee * 31536000}")

#numero 23
for i in range(1,6):
    print(f"{i} 1 {i} {i**2} {i**3} ")


