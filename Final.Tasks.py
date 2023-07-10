"""
# Task 1

text = input("Enter the text: ")
word = input("Enter the word to search for: ").lower()
punctuations = ",.!?;:/[]@#%&*-+=^()<>"

count = 0
text = text.lower()

for p in punctuations:
    text = text.replace(p, " ")

text = text.split()

for i in text:
    if word in i or word[::-1] in i:
        if len(i) == len(word):
            count += 1

print("The word", word, "appears", count, "times in the text.")

"""


"""
# Task 2

text = input("Enter the text: ")
words = input("Enter the words to search for (separated by commas): ").lower().split(',')
punctuations = ",.!?;:/[]@#%&*-+=^()<>"

text = text.lower()

for p in punctuations:
    text = text.replace(p, " ")

text = text.split()

for word in words:
    count = 0
    for text_word in text:
        if word == text_word or word == text_word[::-1]:
            count += 1

    print(word, "- appears", count, "times in the text.")
    
"""


"""
# Task 3

txt = "Cat runs. Dog runs. Cat jumps."

replacements = ["cat", "dog"]
new_words = ["bird", "fish"]

count1 = 0
count2 = 0

print(txt)
sepp = txt.lower().split(" ")

for i in range(len(sepp)):
    if sepp[i] in replacements:
        index = replacements.index(sepp[i])
        sepp[i] = new_words[index]
        if index == 0:
            count1 += 1
        else:
            count2 += 1

txt_join = ' '.join(sepp)

new_txt = ''
count = txt_join.count('.')
start = 0

for i in range(count):
    index = txt_join.find('.', start)
    new_txt += txt_join[start:index].capitalize() + '. '
    start = index + 2
print(new_txt)
print()
print("Cat/Bird –", count1)
print("Dog/Fish -", count2)

"""

"""
# Task 4.1
import random

lst1 = []
lst2 = []
lst3 = []
lst4 = []

for i in range(5):
    lst1.append(random.randint(0, 100))
    lst2.append(random.randint(0, 100))
    lst3.append(random.randint(0, 100))
    lst4.append(random.randint(0, 100))
print(f"lst1 = {lst1}\nlst2 = {lst2}\nlst3 = {lst3}\nlst4 = {lst4}")

lst5 = lst1 + lst2 + lst3 + lst4
lst5.sort(reverse=True)
print()
print(f"lst5 = {lst5}")

"""

"""
# Task 4.2

lst1 = [2, 15, 99, 6, 43]
lst2 = [2, 82, 99, 34, 15]
lst3 = [3, 2, 99, 15, 28]
lst4 = [99, 15, 67, 2, 75]

remove_lst = []
new_lst = []

for i in lst1:
    if i in lst2 and i in lst3 and i in lst4:
        remove_lst.append(i)

for i in lst1 + lst2 + lst3 + lst4:
    if i not in new_lst:
        new_lst.append(i)

lst5 = []
for i in new_lst:
    if i not in remove_lst:
        lst5.append(i)
print(lst5)

"""

"""
# Task 4.3

lst1 = [2, 15, 99, 6, 43]
lst2 = [2, 82, 99, 34, 15]
lst3 = [3, 2, 99, 15, 28]
lst4 = [99, 15, 67, 2, 75]

lst5 = []

for i in lst1:
    if i in lst2 and i in lst3 and i in lst4:
        lst5.append(i)

print("lst5 =", lst5)

"""

"""
# Task 4.4

import random

lst1 = []
lst2 = []
lst3 = []
lst4 = []

for i in range(5):
    lst1.append(random.randint(0, 100))
    lst2.append(random.randint(0, 100))
    lst3.append(random.randint(0, 100))
    lst4.append(random.randint(0, 100))
print(f"lst1 = {lst1}\nlst2 = {lst2}\nlst3 = {lst3}\nlst4 = {lst4}")
print()
lst5 = []


def is_prime(num):
    if num < 2:
        return False
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


for element in lst1 + lst2 + lst3 + lst4:
    if element not in lst5 and is_prime(element):
        lst5.append(element)

print("lst5 =", lst5)

"""


"""
# Task 5

mystr = input("Enter a mathematical expression: ")
mystr = mystr.replace(" ", "")
numbers = []
operators = []
str_num = ""

for i in mystr:
    if i.isnumeric():
         str_num += i
    else:
        numbers.append(int(str_num))
        str_num = ""
        operators.append(i)

numbers.append(int(str_num))
result = numbers[0]

for i in range(len(operators)):
    if operators[i] == "+":
        result += numbers[i + 1]
    elif operators[i] == "-":
        result -= numbers[i + 1]

print(result)

"""
