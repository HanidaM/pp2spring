import re

def match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return ('Match!')
        else:
                return('Not matched!')
print(match("ac"))
print(match("abb"))
