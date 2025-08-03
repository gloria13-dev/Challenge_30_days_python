#challenge python jour 12
#Exercises: Level 1
from random import randint, random
import string

# number 1
def random_user_id():
    char = string.ascii_letters + string.digits
    id = ''.join(random.choices(char, k=6))
    return id

#number 2
def user_id_gen_by_user():
    characters_nb = int(input('Enter the number of characters: '))
    ids_nb = int(input('Enter the number of IDs which are supposed to be generated: '))
    char = string.ascii_letters + string.digits
    for i in range(ids_nb):
        user_id = ''.join(random.choices(char,k=characters_nb))
        return  user_id

#number 3
def rgb_color_gen():
    r = g = b = randint(0,255)
    return f'rgb({r},{g},{b})'


#Exercises: Level 2
# number 1
def list_of_hexa_colors(n):
    colors = []
    for i in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

print(list_of_hexa_colors(2))

#number 2
def list_of_rgb_colors(n):
    colors = []
    for i in range(n):
        r = g = b = randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors

# number 3
def generate_colors(color_type, n):
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(n)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."


#Exercises: Level 3
#number 1
def shuffle_list(liste):
    liste_shuffle = liste[ : ]
    random.shuffle(liste)
    return liste_shuffle

#number 2
def unique_random_numbers():
    return random.sample(range(10), 7)



#number 2



