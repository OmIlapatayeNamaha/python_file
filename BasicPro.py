#List Compration
'''li=[i for i in range (11) if i % 2]
print(li)'''
#Dict Compration
'''d={i:i*i for i in range(1,11)}
print(d)'''

#assert used for debugging
'''a,b=10,20
min = a if a<b else b
print(min)'''


'''l=[(1,2,3,4),('a','b','c','d')]
k,v=l
print(dict(zip(k,v)))'''

'''li=[10,20,30,40]
li2=[100,200,300]
for i,j in zip(li,li2):
    print(i,j)'''


'''class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def info(self):
        print(f"My name is {self.name} and i am {self.age} year old and my salary is {self.salary}")
e1=Employee('Bhagya', 21, 10000)
e1.info()
print(e1.name)
print(e1.age)
print(e1.salary)'''

'''class hello:
    def setdata(self, value):
        self.data = value

    def showdata(self):
        print(self.data)

x = hello()
y = hello()

x.setdata('Shree')
y.setdata(3.5245)

x.showdata()
y.showdata()'''


#even or odd
'''
i=20
if i%2==0:
    print('no is even')
else:
    print('no is odd')
'''


'''
str = input ('Enter a string')

words = [word.lower () for word in str.split ()]

words.sort ()

print ('The words sorted in alphabetical order are as follows:')

for word in words:
     print (word)
'''

"""
count=0
for letter in 'Hello world':
    if (letter == 'l'):
        count+=1
    print(count,'letters found')
""" 

'''li=['khandekar']
li.reverse()
print(li)'''

'''
str='I am bhagyshri'
print(str[::-1])
'''
#ematy1
'''li=[]
print(li)
'''
#sort() clear()
'''
li=['a','b','a','s','a']
# li.sort()
# li.clear()
li.count('a')
print(li)
'''

#*arg

def my(x,*y):
    print(x,y)
my(20,40,10,20,30,40)


#**arg
'''
def my(**y):
    print(y)
my(a=10,b=20)
'''









