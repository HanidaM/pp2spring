import random

name = input("Hello What is your name?: ")
print("Well,",name ,", I am thinking of a number between 1 and 20.")


x = random.randint(1, 20)

 
count = 0

while count < 20:
    count += 1
    
    
    guess = int(input("Take a guess: "))
 
    if x == guess:
        print("Good Job, you guessed in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too low!")
    elif x < guess:
        print("You Guessed too high!")
 

if count >= 20:
    print("The number is ", x)
    print("Better Luck Next time!", name)
 