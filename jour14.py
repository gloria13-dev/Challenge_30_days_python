#challenge python day 14
#Exercises
from functools import reduce
from collections import Counter
from asttokens.util import is_starred
import countries_data.py

from Day_2.variable import country

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark',
'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Exercises: Level 1
# number 1: difference between map, filter and reduce
""" * map is a built-in function that takes another function and an iterable as parameters and returns an iterable but 
    * filter is a built-in function which takes a function which returns boolean and an iterable as parameters and return iterable while
    * reduce is a function import from functools which takes a function and an iterable like map and filter but it returns a single result"""

#number 2: difference between higher order function, closure and decorator
""" * higher order function is a function that takes another function as an argument or returns one, while 
    * closure os a nested function that remembers the variables from its outer scope and
    * decorator is  special kind of higher-order function that modifies another function"""

#number 3:
#map
def cube_num(a):
    return a ** 2
numbers_cube = map( cube_num,numbers)
print(list(numbers_cube))

#filter
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers = filter(is_prime,numbers)
print(f'The prime numbers in numbers is: {list(prime_numbers)}')

#reduce
total = reduce(lambda x,y: x + y ,numbers)
print(total)

#number 4
for i in range(len(countries)):
    print(countries[i])

#number 5
for i in range(len(names)):
    print(names[i])

#number 6
for i in range(len(numbers)):
    print(numbers[i])


#Exercises: Level 2
#number 1: changing each country to uppercase in the countries list
def upper_changing(country):
    return country.upper()
countries_upper = list(map(upper_changing, countries))
print(f'\nThe new list is: {countries}')

#number 2
def square(x):
    return x**2
numbers_square = list(map(square,numbers))
print(f'\nThe new list which contains the square of each number in numbers list is: {numbers_square} ')

#number 3
def upper_changing(name):
    return name.upper()
names_upper = list(map(upper_changing, names))
print(f'\nThe new list is: {names_upper}')

#number 4
def contain_land(country):
    if 'land' in country:
        return True
    return False

contain_land_countries = list(filter(contain_land,countries))
print(f"\nthe list of countries containing 'land': {contain_land_countries}")

#number 5
def num_characters(country):
    if len(country) == 6:
        return True
    return False
six_char_countries = list(filter(num_characters,countries))
print(f'\nThe countries having exactly 6 characters are: {six_char_countries}')

#number 6
six_more_characters = list(filter(lambda country: len(country) >= 6,countries))
print(f'\nThe countries having 6 or more letters are: {six_more_characters}')

#number 7
start_with_e = list(filter(lambda country: is_starred('e'),countries))
print(f"\ncountries starting with 'ef' are: {start_with_e}")

#number 8
mapped = map(lambda x: x * 2, numbers)

filtered = filter(lambda x: x > 5, mapped)

result = reduce(lambda x, y: x + y, filtered)

print(result)

#number 9
def get_string_lists(number):
    string_list = str(number)
    return string_list
print(numbers)

#number 10
total = reduce(lambda a,b: a + b, numbers)
print(f'the sum of all numbers in the numbers list is {total}')

#number 11
def concatenate_countries(country):
    sentence = reduce(lambda x, y: x + ', ' + y, country[:- 1])
    sentence += ' and ' + country[-1]
    sentence += ' are north European countries'
    return sentence
print(concatenate_countries(countries))

#number 12
countries_list = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
    'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
    'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Chad',
    'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
    'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic',
    'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
    'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France',
    'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana',
    'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau',
    'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland',
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
    'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan',
    'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait',
    'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho',
    'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
    'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
    'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
    'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
    'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru',
    'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger',
    'Nigeria', 'North Korea', 'North Macedonia', 'Norway', 'Oman',
    'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay',
    'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar',
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
    'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 'Senegal',
    'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea',
    'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
    'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
    'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu',
    'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
    'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela',
    'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]
def categorize_countries(pattern):
    return [country for country in countries_list if pattern.lower() in country.lower()]

#number 13
def count_countries_by_letter(country):
    letter_counts = {}
    for country in countries:
        first_letter = country[0].upper()
        letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1
    return letter_counts

print(count_countries_by_letter(countries))

#number 14
def get_first_ten_countries(countries_list):
    return countries[:10]
print(get_first_ten_countries(countries_list))

#number 15
def get_last_ten_countries(country):
    return country[-10:]
print(get_last_ten_countries(countries_list))


#Exercises: Level 3
#Sort countries by name, by capital, by population
sorted_by_name = sorted(countries, key=lambda x: x['name'])
sorted_by_capital = sorted(countries, key=lambda x: x['capital'])
sorted_by_population = sorted(countries, key=lambda x: x['population'])

#Sort out the ten most spoken languages by location.
language_counter = Counter()

for country in countries:
    for lang in country['languages']:
        language_counter[lang] += 1
print(language_counter.most_common(10))

#Sorting out the ten most populated countries.
top_populated = sorted(countries, key=lambda x: x['population'], reverse=True)[:10]

for country in top_populated:
    print(f"{country['name']} - {country['population']}")

