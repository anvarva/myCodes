# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:44:10 2019

@author: AnvarVA

All the codes below is from the youtube video link

https://www.youtube.com/watch?v=C-gEQdGVXbk&t=1042s

"""
"""
Terniery operators
"""

condition = True

x = 1 if condition else 0

print(x)

"""
large numbers

"""
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')

"""
file opeining and closing

"""

with open ('text.txt', 'r') as f:
    file_contents = f.read()
    
words = file_contents.split(' ')
word_count = len(words)
print(word_count)
#print(words)


"""
Looping, counter, unpacking

"""

names = ['Corey','Chris', 'Dave', 'Travis']
second_names = ['dop','mop', 'cop', 'sop']
nationalities = ['USA','Canada', 'India', 'Mexico']

for index, name in enumerate(names, start = 1):
    print(index, name)
    
for name, second_name, nationality in zip(names, second_names, nationalities ):
    print(f'{name} {second_name} is from {nationality}')
