def counter(heads,legs):
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print("ERROR")
    elif(legs%2!=0):
        print("ERROR")
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print("Count of Chicken",int(chicken_count),"\n","Count of Rabblits",int(rabbit_count))
    
if __name__ == "__main__":
    heads = int(input("Number of Heads: "))
    legs = int(input("Number of Legs: "))
    counter(heads, legs)