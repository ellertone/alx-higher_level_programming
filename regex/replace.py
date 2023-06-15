#!/usr/bin/python3

import re

owlFood = "rat cat bat pat"

regex = re.compile("[cb]at")

owlFood =  regex.sub("owl", owlFood)

print(owlFood)