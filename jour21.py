#challenge python Day 21
#Exercises: Level 1

import statistics
from itertools import count
import math
from collections import Counter

class Statistics:
    def init(self, data):
        self.data = data

    def count(self,data):
        return len(self.data)

    def sum(self,data):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        return self.data[mid]

    def mode(self):
        freq = Counter(self.data)
        mode = freq.most_common(1)[0]
        return {'mode': mode[0], 'count': mode[1]}

    def var(self):
        mean = self.mean()
        return round(sum((x - mean) ** 2 for x in self.data) / self.count(), 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def freq_dist(self):
        freq = Counter(self.data)
        return sorted([(v * 100 / self.count(), k) for k, v in freq.items()], reverse=True)

    def describe(self):
        print('Count:', self.count())

    print('Sum: ', data.sum())
    print('Min: ', data.min())
    print('Max: ', data.max())
    print('Range: ', data.range())
    print('Mean: ', data.mean())
    print('Median: ', data.median())
    print('Mode: ', data.mode())
    print('Variance: ', data.var())
    print('Standard Deviation: ', data.std())
    print('Frequency Distribution: ', data.freq_dist())


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32,
        33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)
data.describe()


#Exercises: Level 2

class PersonAccount:
    def _init_(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description=''):
        self.incomes.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description=''):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(i['amount'] for i in self.incomes)

    def total_expense(self):
        return sum(e['amount'] for e in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f'''
        Name: {self.firstname} {self.lastname}
        Total Income: {self.total_income()}
        Total Expense: {self.total_expense()}
        Balance: {self.account_balance()}
        '''



print(person.account_info())




