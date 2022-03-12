import re

def text_match(text):
        match = 'ab{2,3}'
        if re.search(match,  text):
                return ('Match!')
        else:
                return('Not matched!')
print(text_match("ab"))
print(text_match("aabbbbc"))
