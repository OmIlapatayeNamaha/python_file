'''
if not True:
    print('1')
elif not(1+1==3):
    print('2')
else:
    print("3")
'''
#Example2
'''
if 1+1*3==6:
    print("yes")
else:
    print("no")
'''
#Example3
#If
'''
a=10
b=20
if a<b:
    print("true")
'''

#Example4
#If...Else
'''
a=20
b=30
if a==b:
    print("true")
else:                  #False cond is false
    print("false")
'''
#Example5
'''
a=10
b=10
if a==b:
    print("true")
else:                 #true cond are true
    print("false")
'''
#example6
#Nested if 
'''
a=10
b=20
if a<b:
    print("true")
    if a!=b:
        print("true")
    else:
        print("false")
else:
    print("cond false")
'''
#example8
#nested if...else
'''
a=10
b=20
c=30
d=40
if a==b:
    #print("true")
    if c<d:
        print("true")
    else:
        print("false")
else:
    #print("false")
    if a<b:
        print("true")
    else:
        print("false")
'''
    
#Example9
#if elif..else
'''
a=10
b=20
if a>b:
    print("first condition true")
elif a==b:
    print("second cond true")
elif a<b:
    print("thired cond true")
else:
    print("false")
'''