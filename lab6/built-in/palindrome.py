

string = input("Input string to check palindrome: ")

ispalindrome = string[::-1] #reverse of string 

if(string == ispalindrome):             #if hello =! olleh prints NOPE else "yes it matched "
    print("Yes it is palindrome")
else:
    print("NOPE")

string = input()

if(string) == "".join(reversed(string)): #Reversed method (Built in Function)
    print("Palindrome")
else:
    print("Not PAlindrome")

