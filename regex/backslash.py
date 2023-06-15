#!/usr/bin/python3

import re

# randStr = "Here is \\stuff"

# print("Find \\stuff: ", re.search(r"\\stuff", randStr))

# speecial escape characters
'''
\b :backspace
# \f :form feed
\r : carriage return
\t : tab
\v : vertical tab
\d :  all digits
\D : [^0-9]  except digits
'''

randStr = "123 12345 123456 1234567"

print("Matches : ", len(re.findall("\d{5,7}", randStr)))