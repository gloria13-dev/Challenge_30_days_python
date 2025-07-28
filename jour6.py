#Challenge python day 6
#Exercises : Level 1
#number 1
news = () #creation of an empty tuple named news

#number 2
brothers = ("Obed","Ebenezer","Olivier","Gedeon") #tuple containing the name of my brothers
sisters =("Rejoice","Priscille","Dorcas") #tuple containing the name of my sisters
print("\nMy brothers are :",brothers,"\nMy sisters are :",sisters)

#number 3
siblings = brothers + sisters #sisters and brothers tuples joining and I assigned it to siblings
print("\nMy siblings are: ",siblings)

#number 4
siblings_number = len(siblings)
print("\nI have",siblings_number,"siblings")

#number 5
siblings_list = list(siblings)  #changing the tuple siblings to a list
print("\nThe siblings list is : ",siblings_list)

siblings_list.extend(["Honoré","Antoinette"]) #adding of the name of the father and the mother into the list siblings_list
family_members = tuple(siblings_list) #assignement of the list siblings_list to the tuple family_members
print("\nMy family members are:",family_members)


#Exercises: Level 2
#number 1
siblings = family_members[:len(family_members)-2] #unpack siblings from family_members
parents = family_members[len(family_members)-2:]  #unpack parents from family_members

#number 2
fruits = ("mango","strawberry","lemon","banana","orange","pineapple")
vegetables =("carrot","onion","tomato","pepper","spinach","yam")
animal_products = ("egg","milk","fish","butter","cheese","meat")
food_stuff_tp = fruits + vegetables + animal_products

#number 3
food_stuff_lt = list(food_stuff_tp) #tuple food_stuff_tp changed into food_stuff_lt
print("\nThe food stuff list is:",food_stuff_lt)

#number 4
print(len(food_stuff_lt))
# the items number in food_stuff_lt is 18 (even number)
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt[middle_index:middle_index + 2]
print("\nthe middle items are: ",middle_item)

#number 5
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print("\nThe first three items are: ",first_three_items,"\nThe last three items are: ", last_three_items)

#number 6
del food_stuff_tp #Deleting the food_staff_tp tuple completely

#number 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway',
'Sweden')
print('Estonia' in nordic_countries) # checking if 'Estonia' is a nordic country
print('Iceland' in nordic_countries) # checking if 'Iceland' is a nordic country















