#Aliasing 
#two list same address stored
li=[1,2,3]
l1=li
print(li is l1)#True
print(id(li))
print(id(l1))
print(type(l1))
print(l1)

#two list are diffrent address are stored
l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2)#False
print(id(l1))
print(id(l2))



'''l1=[1,2,3]
l2=l1
l1[1]=55
print('l1 modify:',l1)
print('l2 :',l2)'''


'''l1=[1,2,3]
l2=l1
l2[1]=55
print('l1 modify:',l1)
print('l2 :',l2)
'''


'''
a=[10,20,30,40]
print(a)
print(a[1])
a[1]=40
print(a[1])
'''

#Accessing list in using loop
'''
li=[10,20,30,'a']
for i in li:
    print(i)

n=len(li)
for i in range(n):
    print(a[i])
    print(i,a[1])
'''

#Method List
#append()-->this method are use in add single element in existing of list
'''li=[10,20,30]
li.append(50)
print(li)'''

#Extend()-->this method are use in add multiple element in existing of list
'''b=[1,2,3]
a=[4,5,6]
b.extend(a)
print(b)'''

#Insert()-->insert the value in particular position of the existing list
'''a=[1,2,3,4]
a.insert(3,'python')
print(a)'''

#Getting list input from user
'''a=[]
print(a)
n=int(input('enter the number:'))
for i in range(n):
    a.append(int(input('enter the element')))
    print('list:')
    for ele in a:
        print(ele)
    print(a)'''


#pop()-->this method is use remove the last element from the existing list
'''li=[10,20,30,40]
li.pop(1)
print(li)'''

#remove()-->this method is use remove first element
'''li=[10,20,30]
li.remove(20)
print(li)'''

#index()-->this method use in find the  position
'''a=[10,20,30]
b=a.index(10)
print(b)'''

'''
li=[1,2,3]
a=li
a[1]=4
print(a)
print(id(li))
print(id(a))
print(a is li)
print(a == li)'''

'''li=[1,2,3]
l1=[1,2,3]
print(li is l1)'''



#example
'''
a=[0,1,2,3]
for a[-1] in a:
    print(a[-1])
'''
#Interview Que
#Without list comprehension you will have to write a for statement with a conditional test inside:
'''fru=['apple','banana','cherry','kiwi','mango']
li=[]
for x in fru:
    if "a" in x:
        li.append(x)
print(li)'''

#with list comprehension you can do all that with only one line of code
'''fru=['apple','banana','cherry','kiwi','mango']
li=[x for x in fru if "a" in x]
print(li)'''


'''
a=2
def mul():
    b=3
    return a*b
print(mul())
'''
#Pass 
'''
def f():
    pass
print(type(f()))
'''

#Recarsive 
'''
def myfun():
    print("Hello")
    myfun()
myfun()
'''

