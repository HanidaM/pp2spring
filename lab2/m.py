from datetime import datetime
    
def printDates(dates): 
   
    for i in range(len(dates)):  
        print(dates[i]) 
       
       
if __name__ == "__main__":  
  
    dates =  []  
    while True:
        dt = input()
        if dt == "0":
            break
        else:
            dates.append(dt)
      
    dates.sort(key = lambda date: datetime.strptime(date, '%d %m %Y'))
    
    printDates(dates) 