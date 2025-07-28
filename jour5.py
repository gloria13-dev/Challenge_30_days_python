# Challenge python jour 5
#Level 1
#numero 1
informations = [ ]

#numero 2
fruits = ['orange', 'mango', 'stramberry', 'lemon','grape','banana','watermelon']

#numero 3
print('The length of the list is : ',len(fruits))

#numero 4
print('The first item is : ', fruits[0])
print('The middle item is :', fruits[len(fruits) // 2])
print('The last item is: ',fruits[-1])

#numero 5
mixed_data_types = ['KPOGO Gloria', 19, 155,'single', '91 30 25 35']

#numero 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#numero 7
print(it_companies)

#numero 8
print('the number of companies is: ',len(it_companies))

#numero 9
print('The first company is: ',it_companies[0])
print('The middle company is: ',it_companies[len(it_companies) // 2])
print('The last company is: ',it_companies[-1])

#numero 10
it_companies[3] = 'Intel'
print("modifiying of one of the company",it_companies)

#numero 11
it_companies.append('Apple')
print("Adding of an IT company to it_company",it_companies)

#numero 12
it_companies.insert( len(it_companies) // 2, 'Adobe')
print("insertion of an IT company: ",it_companies)

#numero 13
it_companies[0] = it_companies[0].upper()
print("Changement of the name of one company to uppercase: ",it_companies)

#numero 14
print("#; ".join(it_companies))

#numero 15
print("Apple" in it_companies)

#numero 16
it_companies.sort()
print(it_companies)

#numero 17
it_companies.reverse()
print(it_companies)

#numero 18
print("The last 3 company are: ",it_companies[0:3])

#numero 19
print("The last 3 company are: ",it_companies[-4:-1])

#numero 20
middle = len(it_companies) // 2
middle_company = it_companies[middle:middle+1]
print("the middle IT company is ", middle_company)

#numero 21
it_companies.remove(it_companies[0])
print(it_companies)

#numero 22
it_companies.remove(middle_company)

#numero 23
it_companies.remove(it_companies[-1])
print(it_companies)

#numero 24
it_companies.clear()
print(it_companies)

#numero 25
del it_companies

#numero 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#numero 27
full_stack = front_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)


#Level 2
#numero 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('The min age is: ', min(ages))
print('The max age is: ',max(ages))

ages.extend([min(ages),max(ages)])
print(ages)

#Median
ages.sort()
len(ages)
middle = len(ages) // 2
median = (ages[middle - 1] + ages[middle]) / 2
print("The Median age is: ", median)

#Average
average = sum(ages) / len(ages)
print("The Average age is: ", average)

#Range
age_range =max(ages) - min(ages)
print("The Range of the age is: ", age_range)

#Comparison
print("Min - avg:", abs(min(ages) - average))
print("Max - avg:", abs(max(ages) - average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan',
  'Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan',
  'Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',]
print(len(countries))
index = len(countries) // 2
middle = [countries[index]]
print("Middle country:", middle)

#numero 3
first_half = countries[:index + 1]
second_half = countries[index + 1]
print("First half:", first_half)
print("Second half:", second_half)

#numero 4
country1, country2, country3, *scandic = countries
print("The First three countries are: ", country1, country2, country3)
print("The Scandic countries are: ", scandic)




