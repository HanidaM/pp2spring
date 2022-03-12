import re
def spaces(txt):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print(spaces("Hello"))
print(spaces("HelloWorld"))
print(spaces("HelloWorldAndBauka"))
