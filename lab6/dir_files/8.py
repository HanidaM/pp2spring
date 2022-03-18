import os 
    
target = 'test.py'
location = "/Users/bk/Desktop/pp2"
path = os.path.join(location, target) 

if (os.access(target, os.F_OK)):
    os.remove(path) 