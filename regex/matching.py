#!/usr/bin/python3

import re
animalStr = "Cat bat, rat mat pat"

allAnimals =  re.findall("[Cbrmp]at", animalStr)

for i in allAnimals:
    print(i, end=" ")

someAnimals =  re.findall("[c-mC-M]at", animalStr) # find all between c and m
#                       ("[^C]") all except those with C in them
    
for i in someAnimals:
    print(i, end=" ")