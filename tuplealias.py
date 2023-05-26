'''tu=(1,2,3)
sb=(1,2,3)
print(tu is sb)
print(id(tu))
print(id(sb))'''

#Aliasing
'''
t=(1,2,3)
b=t
print(b)
print(id(t))
print(id(b))   
'''
#Example
tup=(1,2,3)
b=tup
print(tup is b)

#Copy
'''
a=(10,20,30,40)
print(a)
b=a
print("A:",a)
print("B:",b)
'''
#Example
'''arr=[[["*" for col in range(6)] for col in range(4)] for row in range(3)]
print(arr, sep='\n')'''

'''
test_list=[(4,5,9),(3,2,-3),(-3,5,6),(4,6)]
res=[]
for tup in test_list:
    if all(ele>=0 for ele in tup):
        res.append(tup)
print('Positive element Tuples:'+str(res))
'''
'''
aTuple = 1,2,3
a,b,c = aTuple
print(a)
'''
#example fun
'''
class Marks:
    def __init__(self,student):
        self.student = student
obj = Marks(100)
obj.mark = 40
obj.number = 2
print(obj.mark + len(obj.__dict__))
'''
#Example
'''s1='ram'
x='Hello'.join('ram')
print(x)
'''
#add tuple element
'''
a=(10,20,30,60,70)
print(a)
print(id(a))
b=(40,50)
c=a+b
print(c)
print(id(c))'''
#Example
'''
a=(10,20,50,'shree')
s=(30,40)
s1=a[0:2]
s2=a[2:]
tup=s1+s+s2
print(tup)
'''










