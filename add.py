
li=[6,8,5,2,9,11,2,6,8]

n=len(li)
i=0
while(i < n):

    pos=0
    while(pos<len(li)-1):
        x = li[pos]
        y = li[pos+1]
        if x>y:
            li[pos] = y
            li[pos+1] = x
            pos=pos+1
            n=n-1
            print(li)
            
                
        
            
        
            
        





      
