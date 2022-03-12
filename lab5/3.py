import re

def text_match(text):
        match = '^[a-z]+_[a-z]+$'
        if re.search(match,  text):
                return ('Match!')
        else:
                return('Not matched!')
print(text_match("ab"))
print(text_match("aabbbbc"))
