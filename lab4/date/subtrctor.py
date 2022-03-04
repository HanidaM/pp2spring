import datetime
from datetime import date, timedelta
print('Current Date :',date.today())
today = datetime.date.today()
print("Next five dates are: ")
for i in range(0, 5):
    print(today + datetime.timedelta(days = i))
    

