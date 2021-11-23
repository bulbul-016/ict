
a = int(input('Enter starting number: ')) 
b = int(input('Enter ending number: ')) 
 
 
def primery(d):        
    if d < 2:          
        return False    
 
    for j in range(2, d): 
        if d % j == 0: 
            return False    
    return True             
 
 
for i in range(a, b + 1): 
    if primery(i): 
        print(i)