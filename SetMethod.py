#Add function in set
'''
st = {10,20,30}
st.add(40)
print(st)
'''
#Add function in set
'''
st1 = {10,20,30}
st1.add((40,20)) # by using data sequence(tuple,list,dict) can be create set.
print(st1)

'''
#Update function in set
'''
st2 = {10,20,30}
st2.update((40,20,20,20,80))  #here can be use (tuple,list,dict) and dduplication is not allowed
print(st2)
'''
#Update function in set
'''
st3 = {10,20,30}
st4 = st3.update({40,20,20,20,80})  #here can be use (tuple,list,dict) and dduplication is not allowed
print(st4)
'''
#create set using set method()
'''
st4=set({"Bhagya","Shree","Shivani","Niki"})
print(st4)
'''
#Creating set in immutable ele
'''
a={10,20,"a",20.5,14}
print(type(a))
'''
#Creating a set which have mutable element
'''
a={10,20,["a",20.5,14]}
print(type(a))
'''
#Removing items from the set
#Remove Method()-if the item to be deleted from the set using remove()
'''
s={1,2,3,45,"gtg"}
val=s.remove(3)
print(val)
print(s)
'''
#Discart Method()
#If the key to be deleted from the set using discard() doesn't exist in the set
'''
x=set(["Shiv","pari","shonak","rohan"])
a=x.discard("rohan")
print(a)
print(x)
'''
#Pop Method()
'''
x=set(["Shiv","pari","shonak","rohan"])
x.pop()
print(x)
'''
#Clear Method()
'''
Months = set(["January","February", "March", "April", "May", "June"])    
Months.clear()
print(Months)
'''
#Copy Method()
'''
Months = set(["January","February", "March", "April", "May", "June"]) 
x=Months.copy()
print(x)
'''
#Logical Oprations
#Union-The union of the two sets contains all the items that are present in both the sets.
#Using | pipe symbol
'''
day={"Mon","Tue","wen","thur","sun"}
day1={"fri","srt","sun"}
print(day|day1)
'''
#union are print the two set All element
#using union() keyword
'''
s={10,20,30,40}
s1={40,50,60}
print(s.union(s1))
#print(s)
'''

#Intersection()-The intersection of the two sets is given as the set of the elements that common in both sets.
#intersection are used symbol in and &
'''
s={10,20,40,60,30}
u={70,40,80,20,60,80}
print(s&u)
'''
#intersection are print in only comman element
#useing intersection()keyword
'''
s={10,20,40,60,30}
u={70,40,80,20,60,80}
print(s.intersection(u))
'''

#intersection_update()Method->The intersection_update() method removes the items from the original set that are not present in both the sets
'''
a = {10,30,40}    
b = {30,40,50}       
b.intersection_update(a)
print(b)
'''
#Difference() Method-The returned set contains items that exist only in the first set, and not in both sets.
'''
a={1,2,3,4,5}
b={2,3,6,7,8}
c=a-b
print(c)
'''
# Using difference() method
'''
a={1,2,3,4,6}
b={6,7,8,9,1}
print(a.difference(b))
'''
#Difference_Update()-removes the items that exist in both sets. and print the ele in first set
'''
a={1,2,3,7,6}
b={6,7,8,9,1}
a.difference_update(b)
print(a)

'''
#issubset
'''
s1={10,20,30}
s2={10,20,30}
print(s1.issuperset(s2))
'''



