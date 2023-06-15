#!/usr/bin/python3

import re

if re.search("ape", "The baby is in the planet of the apes"):
    print(" The baby is dead")

allApes = re.findall('ape', "The apex predators were the apes in the planet of the apes")

for i in allApes:
    print(i)