import re
with open('raw.txt') as f:
    text = f.readlines()
print(re.sub("[ ,.]", ":", text))