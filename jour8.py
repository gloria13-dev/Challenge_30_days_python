#challenge python Day 8
#Exercises
#number 1
dog = {}

#number 2
dog['name'] = 'Wiz'
dog['color'] = 'brown'
dog['breed'] = 'bulldog'
dog['legs'] = 4
dog['age'] = 2
print(dog)

#number 3
student = {'first_name':'Rejoice',
           'last_name':'HOUNKPE',
           'gender':'female',
           'age':20,
           'marital status':'single',
           'skills':['python','HTML','CSS','JavaScript'],
           'country':'Togo',
           'City':'lome'
           }
print('\nThe dictionary student is: ',student)

#number 4
print('\nThe length of the student dictionary is: ',len(student))

#number 5
print('\nThe value of skills is',student['skills'])
print('The type of the value of skills is',type(student['skills']))

#numero 6
student['skills'].append('Pascal')
print('\nThe dictionary student after modifying of skills values by adding one skills ',student)

#number 7
print('\nThe dictionary keys ares: ',student.keys())

#number 8
print('\nThe dictionary values are: ',student.values())

#number 9
print('\nThe dictionary student as a list of tuple: ',student.items())

#number 10
student.pop('marital status')
print('\nThe dictionary student after deleting one item: ', student)

#number 11
del dog #deleting of the dictionary dog