#Python challenge day 7
#Exercises

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1
# number 1
length_it_comp = len(it_companies)
print("The length of the set 'it_companies' is: ",length_it_comp)

#number 2
it_companies.add('Twitter')
print("the new set of it_companies after adding 'Twitter' is:",it_companies)

#number 3
it_companies.update({"Meta","Intel","Samsung","Flutterwave"})
print(it_companies)

#number 4
it_companies.remove("Flutterwave")

#number 5
# La difference entre remove et discard:
print("\nLorsqu'on utilise la methode remove() Si l'élément à supprimer n'est pas trouvé, la méthode remove() affiche une erreur alors que la méthode discard() n'affiche pas d'erreurs même si l'élement recherché n'est pas dans l'ensemble")

it_companies.discard("Linkedin")
print(it_companies) #Il n'a pas d'erreur quand bien même que 'Linkedin' n'appartient pas à it_companies

#it_companies.remove("Linkedin")
#print(it_companies) # ceci affiche une erreur parce que 'Linkedin' n'appartient pas à it_companies


#Exercises: Level 2
#number 1
print("\nThe joining of A and B is: ",A.union(B))

#number 2
print("\nthe intersection of A and B is: ",A.intersection(B))

#number 3
print(A.issubset(B))

#number 4
print(A.isdisjoint(B))

#number 5
A.union(B) # A join with B
B.union(A) # B join with A

#number 6
print(f"The symmetric difference between A and B is:{A.symmetric_difference(B)} \n")

#number 7
del it_companies,A,B #deleting of the sets

#Exercises: Level 3
#number 1
age_set = set(age)
print(age_set)
print(age)
print(len(age_set) < len(age)) # The length of the list is bigger than the length of the set

#number 2
print("\nA string is a sequence of character which is ordered,immutable,indexed and iterable.")
print("A list is a collection of items written in square brackets.It is a data which is ordered,mutable,indexed and iterable.The items of a list can be duplicate")
print("A tuple is a collection of items written in parentheses.It is ordered,immutable,indexed,iterable.")
print("A set is a collection of unique items written in curly braces. A set is unordered, un-indexed, iterable and immutable.")

#number 3
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split( )
sentence_s = set(words)

print("\nThe number of unique words is ",len(sentence_s))
print("The unique words which have been used in the sentence are: ",sentence_s)

