import re

def ToSnake(text):
        import re
        txt = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', txt).lower()

print(ToSnake('HelloWorldAndBauka'))