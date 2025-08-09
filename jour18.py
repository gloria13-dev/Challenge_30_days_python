#Challenge python Day 18
#Exercises
import re
from collections import Counter
from itertools import count

#Exercises: Level 1
#number 1
paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love'''

clean_paragraph = re.sub(r'[^a-zA-Z\s]', '', paragraph)
paragraph_split = clean_paragraph.split()
count = Counter(paragraph_split)
lst = count.most_common(len(paragraph))
print(lst)
print(f'\nthe most frequent word is "{lst[0][0]}"')

# number 2
points = [-12, -4, -3, -1, 0, 4, 8]
sorted_points = sorted(points)
distance = sorted_points[-1] - (sorted_points[0])

print(f'\n The distance is: {distance}')


#Exercises: Level 2
def is_valid_variable(var):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*'
    return bool(re.match(pattern, var))



#Exercises: level 3
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!? '''


def clean_text(text):
    clean_character = re.sub(r'[^a-zA-Z\s]', '', text)
    clean = re.sub(r'\s+',' ', clean_character)
    return clean
cleaned_text = clean_text(sentence)
print(cleaned_text)


def most_frequent_words(text, n=3):
    text_split = text.split()
    count = Counter(text_split)
    return count.most_common(n)

print(most_frequent_words(cleaned_text))