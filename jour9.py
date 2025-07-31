#Challenge python Day 9
#Exercises: Level 1
#number 1
from calendar import month

from jour5 import middle

age = int(input('\nEnter your age: '))
if age >= 18:
    print('You are old enough to drive.')
else:
    print(f'You need {18 - age} more years to learn to drive.')

#number 2
my_age = 19
your_age = int(input('\nEnter your age: '))
if your_age > my_age:
    if your_age - my_age == 1:
        print(f'You are {your_age -my_age} year older than me.')
    else:
        print(f'You are {your_age -my_age} years older than me.')
elif your_age < my_age:
    if my_age - your_age == 1:
        print(f"I'm {my_age - your_age} year older than you.")
    else:
        print(f"I'm {my_age - your_age} years older than you.")
else:
    print("You are the same age as me.We are friends!!")

#number 3
a = int(input('Enter number 1: '))
b = int(input('Enter number 1: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}.')
else:
    print(f'{a} is equal to {b}')


#Exercises: Level 2
#number 1
scores = int(input('Enter your scores: '))
if (scores >= 90) and (scores <= 100):
    print('You have the grade A')
elif (scores >= 70) and (scores <= 89):
    print('You have the grade B')
elif (scores >= 60) and (scores <= 69):
    print('You have the grade C')
elif (scores >= 50) and (scores <= 59):
    print('You have the grade D')
else:
    print('You have the grade F')

#number 2
month = input('Enter a month: ')
if month in ('September', 'October','November'):
    print('The season is Autumn.')
elif month in ('December', 'January',' February'):
    print('The season is Winter.')
elif month in ('March',' April',' May'):
    print('The season is Spring.')
else:
    print('The season is Summer.')

#number 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter the name of a fruit: ")
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(f'The modified list is: {fruits} ')


#Exercises: Level 3
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB','Python'],
    'address': {'street': 'Space street','zipcode': '02210'}
}
# *
if person['skills'] in person:
    if len(person['skills']) // 2 == 0:
        middle = len(person['skills']) // 2
        print(f"\nThe middle skills are {middle,middle+2}")
    else:
        print(f"\nThe middle skill is {middle,middle+1}")

# *
if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print(f" {person['last_name']} has Python Skill")
    else:
        print(f"{person['last_name']} hasn't Python skill")

# *
skills = person['skills']
if skills == ['JavaScript', 'React']:
    print("He is a front end developer")
elif all(skill in skills for skill in ['Node', 'MongoDB', 'Python']):
    print("He is a backend developer")
elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")

#*
if person['is_marred'] and person['country'] == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} lives in {person['country']}. He is married.")
