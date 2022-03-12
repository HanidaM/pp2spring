import re

def match(text):
        match = 'a.*?b$'
        if re.search(match,  text):
                return ('Match!')
        else:
                return('Not matched!')
print(match("ab"))
print(match("aabbbbc"))
print(match("AaBbGg"))
print(match("aA"))
print(match("Aa"))