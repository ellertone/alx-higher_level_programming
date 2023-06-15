#!/usr/bin/python3
import re

theStr = "The apex predators were the apes in the planet"

for i in re.finditer("ape.", theStr):
    locTuple = i.span()

    print (locTuple)
    print(theStr[locTuple[0]:locTuple[1]])