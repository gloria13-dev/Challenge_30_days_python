#challenge python day 19
#exercises: Level 1
import json
import re
from collections import Counter
# 1:function which count number of lines and number of words in a text.

def lines_words_numbers(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        lines_number = len(lines)
        words_number = sum(len(line.split()) for line in lines)
    return f'{lines_number = }, {words_number = }'

print(lines_words_numbers('data/obama_speech.txt'))
print(lines_words_numbers('data/michelle_obama_speech.txt'))
print(lines_words_numbers('data/donald_speech.txt'))
print(lines_words_numbers('data/melina_trump_speech.txt'))


#2: a function that finds the ten most spoken languages
def most_spoken_languages(file, n):
    with open(file, 'r') as f:
        countries = json.load(f)

    language_counter = Counter()
    for country in countries:
        for language in country.get('languages', []):
            language_counter[language] += 1
    return language_counter.most_common(n)

print(most_spoken_languages('data/countries_data.json', 10))


#3
def most_populated_countries(f,n):
    with open(f, 'r') as f:
        countries = json.load(f)

    sorted_countries = sorted(countries,key=lambda x: x.get('population', 0),reverse=True)
    return [{'country': country['name'], 'population': country['population']} for country in sorted_countries[:n]]

print(most_populated_countries('data/countries_data.json', 10))


#Exercises: level 2
#4: Extraction of all incoming email addresses as a list
def extract_emails(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', content)
    return emails

emails = extract_emails('data/email_exchange_big.txt')
print(emails[:10])



#5
def find_most_common_words(file, n):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = re.findall(r'\b\w+\b', text)
    counter = Counter(words)
    return counter.most_common(n)

print(find_most_common_words('data/sample.txt', 10))
print(find_most_common_words('data/sample.txt', 5))


