# Challenge python Jour 4
# Numero 1
sentence1 = "Thirty" + " " + "Days" + " " + "Of" + " " + "Pyton"

#numero 2
sentence2 = 'Coding' + ' ' + 'For' + ' ' + 'All'

#numero 3
company = "Coding For All"

#numero 4
print(company)

#numero5
print(len(company))

#numero 6
print(company.upper())

#numero 7
print(company.lower())

#numero 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#numero 9
print(company[0:6])

#numero 10
print("Coding" in company)

#numero 11

print(company.replace("Coding","Python"))

#numero 12
sentence = "Python For Everyone"
print(sentence.replace("Everyone","All"))

#numero 13
print(company.split())

#numero 14
resaux =  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(resaux.strip(','))

#numero 15
print(company[0])

#numero 16
print("last index is : ", len(company) - 1)

#numero 17
print(company[10])

#numero 18
acronym1 = ''.join([word[0] for word in sentence.split()])
print(acronym1)

#numero 19
acronym2 = ''.join([word[0] for word in company.split()])
print(acronym2)

#numero 20
print(company.find('C'))

#numero 21
print(company.find("F"))

#numero 22
position_sentence = "Coding For All People"
print(position_sentence.rfind('l'))

#numero 23
sentence_23 = """You cannot end a sentence with because because
because is a conjunction"""
print(sentence_23.index("because"))

#numero 24
print(sentence_23.rindex("because"))

#numero 25
print(sentence_23[31:54])

#numero 26
print(sentence_23.find("because"))

#numero 27
print(sentence_23[31:54])

#numero 28
print(company.startswith("Coding"))

#numero 29
print(company.endswith("coding"))

#numero 30
sentence_30 = ' Coding For All  '
print(sentence_30.strip())

#numero 31
variable1 = "30DaysOfPython"
variable2 = "thirty_days_of_python"
print(variable1.isidentifier())
print(variable2.isidentifier())

#numero 32
libraries = ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" ".join(libraries))

#numero 33
print("I am enjoying this challenge.\nI just wonder what is next")

#numero 34
print("Name\t Age\t Country\t City\nAsabeneh\t 250\t Finland\t Helsinki")

#numero 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#numero 36
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))
























