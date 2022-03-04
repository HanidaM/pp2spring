import datetime 
td = datetime.date.today()
ystd = td - datetime.timedelta(days = 1)
tmr = td + datetime.timedelta(days = 1) 
print('Yesterday : ',ystd)
print('Today : ',td)
print('Tomorrow : ',tmr)
