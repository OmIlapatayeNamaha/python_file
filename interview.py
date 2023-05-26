#*arg
#keyword arguments 
#returns a tuple
'''
def f1(**a):
    print(a)
f1(a=10,b=20,c=30,d=40,e=50,f=60)
'''
#Interview que

a=[1,2,3,8,9]
k=4
n=len(a)
for i in range(0,n,k):
    a[i:i+k]=a[i:i+k][::-1]
print(a)




