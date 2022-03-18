import os

print('Exist:', os.access('/Users/bk/Desktop/pp2/lab6/built-in/palindrome.py', os.F_OK))
print('Readable:', os.access('/Users/bk/Desktop/pp2/lab6/built-in/palindrome.py', os.R_OK))
print('Writable:', os.access('/Users/bk/Desktop/pp2/lab6/built-in/palindrome.py', os.W_OK))
print('Executable:', os.access('/Users/bk/Desktop/pp2/lab6/built-in/palindrome.py', os.X_OK))
