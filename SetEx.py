'''
s={1,2,3,4,5}
print(type(s))
s1={1,2,'a','b',3,1,4}
print(s1)
'''
#add() #Remove() pop()
#add
'''
s2={10,20,30,40,50}
s2.add(50)
print(s2)
'''
#remove
'''
s2.remove(30)
print(s2)
'''
#pop()
'''
val=s2.pop()
print(val)
print(s2)
'''
#empty set are type in dict
'''
s3={'1:try'}
print(type(s3))
'''
#Membership
'''
a={10,20,30,40}
b={30,10,40,30}
print(50 in b)
'''
#iterating/reading
'''
s={1,2,3,4,5,'a',10.3,(10,30),'b'}
for ele in s:
    print(ele)
print(s[-1])#typeerror:set object is not subscriptable
'''
#issubset
'''
s1={10,20,30,50}
s2={10,20,60,70}
s3={20,50,10,30,70,60}
s4={20,30,10,50,60,70}# s5={1,2,3}
print(s1==s2)
print(s1==s3)
print(s1.issbubset(s3))
print(s1.issubset(s2))
print(s1.issuperset(s3))
print(s1.isdisjoint(s5))
print(s1.intersection(s3))
print(s1.intersection_update(s3))
print(s1.difference())
'''
'''
s={20,30,50,40,65}
print(s)
u={200,300,400}
s.update(u)
print(s)
u.add(864)
print(u)
u.remove(300)
print(u)
val=u.pop()
print(val)
s.discard(50)
print(s)


'''