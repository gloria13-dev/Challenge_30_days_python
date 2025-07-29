#Level 1
#Day 2: 30 Days of python programming
from itertools import product
from math import floor

first_name = "Yayra Gloria"
last_name = "KPOGO"
full_name = "KPOGO Yayra Gloria"
country = "TOGO"
city = "LOME"
age = 19
year = 2025
is_married = False
is_true = True
is_light_on = True
name, surname,My_country,age,school_year = "gloria","KPOGO","Togo", 19, 2025

# Level 2
#numero 1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#numero 2
print(len(first_name))

#numero 3
print(len(first_name) == len(last_name))

#numero 4
num_one = 5
num_two = 4

#numero 5
total = num_one + num_two
print("Le total des deux nombres est: ",total)

#numero 6
diff = num_one - num_two
print("la différence des deux nombres est: ",diff)

#numero 7
product = num_one * num_two
print("le produit des deux nombres est: ",product)

#numero 8
division = num_one / num_two
print("La division des deux nombres est: ",division)

#numero 9
remainder = num_two % num_one
print("Le reste de la division du nombre 2 par le nombre 1 est: ",remainder)

#number 10
exp = pow(num_one,num_two)
print("Le nombre 1 à la puissance du nombre 2 est: ",exp)

#numero 11
floor_division = num_one // num_two
print("La division entière du nombre 1 par le nombre 2 est: ",floor_division)

#numero 12
radius = 30
# i
area_of_circle = radius * radius * 3.14
print("la zone d'un cercle de rayon",radius,"mètres est: ", area_of_circle)

# ii
circum_of_circle = 2 * 3.14 * radius
print("la circonférence d'un cercle de rayon",radius,"est: ", circum_of_circle)

#iii
rayon = int(input("Veuillez saisir le rayon du cercle"))
area_of_circl = rayon * rayon * 3.14
print("la zone d'un cercle de rayon",rayon,"mètres est: ",area_of_circl)

#numero 13
first_name = input("Entrez votre prenom")
last_name = input("Entrez votre nom de fammille")
country = input("Saisissez votre pays d'origine")
age = int(input("Veuillez saisir votre age actuel"))

#numero 14
help('keywords')
