# -*- coding: utf-8 -*-

import os

data_0 = ""
data_1 = ""
data_2 = ""

print("START")
print("Data 0")
with open(os.path.join("Lowercase Data", "479343684937187330_lower.txt"), "r+", encoding="utf-8") as file:
    data_0 = file.read()

data_0 = data_0.split()

print("Data 1")
with open(os.path.join("Lowercase Data", "730188056014880831_lower.txt"), "r+", encoding="utf-8") as file:
    data_1 = file.read()

data_1 = data_1.split()

print("Data 2")
with open(os.path.join("Lowercase Data", "748914505915826297_lower.txt"), "r+", encoding="utf-8") as file:
    data_2 = file.read()

data_2 = data_2.split()

data = data_0 + data_1 + data_2

dictionary = list(set(data))

print(len(dictionary))

for i in range(len(dictionary)):
    dictionary[i] = dictionary[i].strip("!\'\"@#$%¨&*()-=+*,.;:<>?/0123456789 []{}\\|~^`´_⣿")

dictionary = list(set(dictionary))

for string in dictionary:
    if string == '':
        dictionary.remove(string)
    # if not string.isalpha() or len(string) > 30:
    #     dictionary.remove(string)

print(len(dictionary))
dictionary.sort()

with open(os.path.join("General Data", "dict.txt"), "w+", encoding="utf-8") as file:
    for element in dictionary:
        file.write(f"{element}\n")

print("END")
