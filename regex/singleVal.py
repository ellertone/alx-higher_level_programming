#!/usr/bin/python3

import re
'''
 \w : [a-zA-Z0-9] match all single values
 \W :[^w]

 \s : matches all other requirements [\f\n\r\t\v]
'''

pNum = "2547-123-7744"

if re.search("\w{4}-\w{3}-\w{4}", pNum):
    print("Kenyan Phone number")