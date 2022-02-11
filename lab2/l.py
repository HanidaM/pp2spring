def strong(n):
    brackets = ['()', '{}', '[]']
    while any(x in n for x in brackets):
        for br in brackets:
            n = n.replace(br, '')
    return not n


n = input()
print("Yes"
      if strong(n) else "No")
