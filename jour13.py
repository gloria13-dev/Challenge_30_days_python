#challenge python day 13
# Exercises
# 1: filter only negative and zero in the list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
neg_zero = [i for i in numbers if i <= 0]
print(neg_zero)

# 2: 
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [i for i in list_of_lists]
print(output)

# 3:
list_of_tuples = [(i, 1, i, i**2, i**3,i**4, i**5) for i in range(11)]
print(list_of_tuples)

# 4:
countries = [[('Finland', 'Helsinki')], [('Sweden','Stockholm')], [('Norway', 'Oslo')]]
flatten = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(flatten)

# 5
output = [{'country': country.upper(), 'city': city.upper()} for [(country, city)] in countries]
print(output)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
[('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [f"{firstname} {lastname}" for [(firstname,lastname)] in names]
print(output)

# 7
linear = lambda m, x, b: m * x + b
print(linear(1,3,3))
