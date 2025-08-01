#challenge python day 10
#Exercises: Level 1
#number 1
for i in range(11):  #Iterate 0 to 10 using for
    print(i)

i = 0
while i <= 10:  #Iterate 0 to 10 using While
    print(i)
    i += 1

#number 2
for i in range(10,-1,-1):  #Iterate 10 to 0 using for
    print(i)

i = 10
while i >= 0:  #Iterate 10 to 0 using While
    print(i)
    i -= 1

#number 3
for i in range(1,8):
    print('#' * i)

i = 1
while i <= 7:
    print("#" * i)
    i += 1

#number 4
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

#number 5
for i in range(11):
    print(f"{i} x {i} = {i * i}")

#number 6
tech_list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in tech_list:
    print(item)

#number 7
for i in range(0, 101):
    if i % 2 == 0:
        print(i)

#number 8
for i in range(0, 101):
    if i % 2 != 0:
        print(i)


#Exercises: Level 2
#number 1
total = 0
for i in range(101):  # de 0 à 100 inclus
    total += i
print("The sum of all numbers is", total)

#number 2
sum_even = 0
sum_odd = 0

for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(f"The sum of all evens is {sum_even} The sum of all odds is {sum_odd}")

#Exercises: Level 3

#number 2
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruits:", reversed_fruits)


