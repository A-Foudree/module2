"""
Program: List and List Methods
Author: Ashley Fry
Last date modified: 01/23/2023
The purpose of this program is to show list of different types and any explanations if needed.
"""
'\nProgram: List and List Methods\nAuthor: Ashley Fry\nLast date modified: 01/23/2023\nThe purpose of this program is to show list of different types and any explanations if needed.\n'

Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list_one = ['taco','mango','cake']
print(list_one)
['taco', 'mango', 'cake']
list_one.append('apple')
list_one
['taco', 'mango', 'cake', 'apple']

list_two=[]
list_two=list_one.copy()
list_two
['taco', 'mango', 'cake', 'apple']
print(list_one[1])
mango
print(list_one[6])
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(list_one[6])
IndexError: list index out of range

print(list_one.count("apple"))
1
list_one.insert(0,"pie")
list_one
['pie', 'taco', 'mango', 'cake', 'apple']

list_one.remove("pie")
list_one
['taco', 'mango', 'cake', 'apple']
list_one.reverse()
list_one
['apple', 'cake', 'mango', 'taco']

list_one.sort()
list_one
['apple', 'cake', 'mango', 'taco']
list_one.clear()
list_one
[]







