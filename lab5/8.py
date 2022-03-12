import re

text = "HelloWorldAndBauka"

print(re.findall('[A-Z][^A-Z]*', text))