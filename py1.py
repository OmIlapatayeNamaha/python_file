#<-------------------TypeCasting--------------------->
#int
#float
#complex
#string

#int-->int
'''
i=10
l=int(i)
print(type(l))
print(l)

'''

#int-->float
'''
i=20
l=float(i)
print(type(l))
print(l)

'''
#int-->str
'''
i=30
l=str(i)
print(type(l))
print(l)

'''
#int-->bool
'''
i=40
l=bool(i)
print(type(l))
print(l)

'''
#float-->float
'''
f=10.1
l=float(f)
print(type(l))
print(l)

'''
#float-->int
'''
f=20.1
l=int(f)
print(type(l))
print(l)

'''

#float-->bool
'''
f=30.1
l=bool(f)
print(type(l))
print(l)

'''
#float-->str
'''
f=40.1
l=str(f)
print(type(l))
print(l)

'''
#bool-->bool
'''
e=True
l=bool(e)
print(type(l))
print(l)
'''
#bool-->int
'''
e=True
l=int(e)
print(type(l))
print(l)
'''

#bool-->float
'''
e=True
l=float(e)
print(type(l))
print(l)
'''

#bool-->str
'''
e=True
l=str(e)
print(type(l))
print(l)
'''

#complex-->complex
'''
c=complex(10,20)
print(type(c))
print(c)
'''


#<-------------String Formating----------->

'''
n=10.23333333
s='value= %.2f'%n
print(s)
'''

#.format
'''print('i am {1} my agg {0}'.format('bhagya',22))'''

#f-string

'''
name='Shubh'
roll='python developer'
print(f'i am {roll} My roll {name}')
'''


#<------------Operator---------------->

#Arithmatic Operator
#+ - * / % // ** 
#+
'''
a=10
b=5
print(a+b)
'''
#-
'''print(a-b)'''
#*
'''print(a*b)'''
#/
'''print(a/b)'''
#//
'''print(a//b)'''
#**
'''print(a**b)'''

#Comparision Operator
#> < == != >= <=
'''a=10
b=20
c=30
if a<b and c>b:
    print('Hello')
else:
    print('Shubh')
'''
'''a=10
b=10
if a==b:
    print('a equal to b')
else:
    print('b equal to a')'''

#Decorator
'''def f2(f1):
    a=f1()
    b=200
    add=a+b
    print(add) 
@f2
def f1() :
    return 100 '''


#inheritance
#single inheritance
'''class A():
    print('Hii i am bhagyashri')
class B(A):
    print('Hello i have learn python')
obj=B()
'''
#Multilevel Inheritance
'''class A():
    print('i am python developer')
class B(A):
    print('as well as django')
class C(B):
    print('Hello')
obj=C()'''

'''
class A():
    def Myfun(self):#define
        print('hello shubhangi')
    
    def Bhagya(self,x):
        self.x=x
        print('hello bhagya')
obj=A()
obj.Myfun()
obj.Bhagya(10)#Calling'''


#Lambda function
'''x = lambda a : a + 10
print(x(5))'''

'''sum = lambda a,x : a+x
print(sum(10,20))
'''

#Iterator 
'''
tup=('apple','banana','cherry')
m=iter(tup)
print(next(m))
print(next(m))
print(next(m))
'''
#Example 2 string
'''
str='banana'
s=iter(str)
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
'''
#Example 3 
#Using for loop iterat the elements
'''
t1=('apple','banana','cherry')
for i in t1:
    print(i)
'''
#Example 4 
#String iterat for using for loop
'''
st='banana'
for i in st:
    print(i)
'''

#Circulary_identical
#Example1
'''
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))) 
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
'''
#Circulary_identical
#Example2
'''
list1 = [100, 10, 100, 10, 100]  
list2 = [10, 100, 0, 100, 100]  
  
a = set(list1)  
b = set(list2)  
  
if a == b:  
    print("list is Identicaly")  
else:  
    print("Not Identicaly")  
'''

#Inheritance
'''
class A():
    def __init__(self, fname,lname):
        self.firstname = fname
        self.lastname = lname
    def Printname(self):
        print(self.firstname,self.lastname)

x = A('Bhagya','Khandekar')
x.Printname()
'''       

#Decorator
'''
def f2(f1):
    a=f1()
    b=100
    add = a+b
    print(add)
@f2
def f1():
    return 200
 '''   

#Genrator
'''
def simple():
    for i in range(10):
        if(i%2==0):
            yield i
    for i in simple():
        print(i)
'''

#Example 1
#call by value
#can not modify
'''
s1='Bhagya'
def test(s1):
    s1='Bhagyashri'
    print('Inside Function:',s1)

test(s1)
print('Outside Function:',s1)
'''

#Example 2
#call by refer
#it is a modify
'''
def add(list):
    list.append(50)
    print('Inside Function:',list)
mylist=[10,20,30,40]
add(mylist)
print('Outside Function:',mylist)
'''


#String 
#String is immutable 
#immutable variable cannot the change it once created
#it you wish it can change the immutable variable
'''
a='Bhagya'
b='Bhagya'
print(id(a))
print(id(b))
print((a is b))
'''

#List
#list are mutable
# mutable variable can be changed in place'
'''
a=[10,20,30]
b=[10,20,30]
print(id(a))
print(id(b))
print(a is b)
'''

'''
class A():
    def __init__(self):
        print('i am constructor')
    def Show(self):
        print('this is show')
    def My(self):
        print('my')
obj=A()
obj.Show()
obj.My()
'''

'''
class A():
    print('i am Bhagya')
class B(A):
    print('i am Priti')
class C(B):
    print('Hello')
obj=C()
'''
#Overloading
'''
class A():
     def show(self):
        print('i am bhagya')
class A(A):
    def My(self):
        print('i am priti')

obj=A()
obj.show()
obj.My()
'''

#Overriding
'''
class A():
     def show(self):
        print('i am bhagya')
class A(A):
    def show(self):
        print('i am priti')

obj=A()
obj.show()
obj.show()
'''
#Comprehension
#list comprehension
#[expression for item in iterable if conditional]
'''
i=[]
for i in range(10):
    if i%2:
        i.append(i)
    print(i)
'''

'''li=[i for i in range(10) if i%2]
print(li)
'''


#Dict Comprehension
#{key:value for (key,value) in iterable if condition}
'''
d={}
for i in range(1,10):
    d[i]=i*i
    i.append(i)
print(d)

'''

'''
d={n:n*n for n in range(1,10)}
print(d)
'''


'''a=sorted(['1','23','22','-7','9','140','450','6'])
print(a)
'''

class classy:
    def __init__(self, id):
        self.id = str(id)
        id="11"
instance=classy(22)
instance.id






































































































































































































