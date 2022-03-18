import string, os


if not os.path.exists("ABS"):
   os.makedirs("ABS")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)