#Arithmetic Operator
#Addition,Substraction,Multiplication,Division,Modual,Expoent,Floor Division
#+ - * / % ** //

#Example1
'''
a=10
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
'''

#Example2
'''
a=10
b=5
print(a+b,a-b,a*b,a/b,a%b,a**b,a//b)

'''
# Relational or Comparision Operator
# < > <= >= == !=
#basically this operators is used to check the conditions
'''
a=10
b=5
print(a<b)#False
print(b<a)
print(a>b)
print(b>a)#False
print(a<=b)#False
print(a>=b)
print(a==b)
print(a!=b)
'''
#Logical Operator And Relational Operator
#AND OR NOT
#AND Operator
#first True and second true
'''
a=10
b=10
if a==b and b==a:
    print("True")
else:
    print("False")
'''
#first true but second false
'''
a=10
b=5
if a>b and a<b:
    print("true")
else:
    print("false")
'''
#first cond false and second true
'''
a=5
b=10
if a>b and b>a:
    print("true")
else:
    print("false")
'''
#all condition are false
'''
a=10
b=5
if a<b and b>a:
    print("true")
else:
    print("false")

'''
#OR Operator
#first true or second true
'''
a=10
b=20
if a<b or b>a:
    print("true")
else:
    print("false")
'''
#first true or second false
'''
a=20
b=10
if a<b or b<a:
    print("true")
else:
    print("false")
'''
#first false or second true
'''
a=10
b=20
if a>=b or b>=a:
    print("true")
else:
    print("false")
'''
#first false or second false
'''
a=10
b=20
if a<b or a>b:
    print("true")
else:
    print("false")
'''
#Not
#condion are true
'''
a=10
b=10
if not a==b:
    print("true")
else:
    print("false")
'''
#condition are false
'''
a=10
b=10
if not a!=b:
    print("true")
else:
    print("false")
'''
#Assignment Operator
#= += -= *= /= %= **= //=
'''
a=10#=
a+=5#+=
print(a)
'''
#-=
'''
a=10
a-=5
print(a)
'''
#*=
'''
a=10
a*=5
print(a)
'''

#/=
'''
a=10
a/=5
print(a)
'''
#%=
'''
a=10
a%=5
print(a)
'''
#**=
'''
a=10
a**=5
print(a)
'''
#//=
'''
a=10
a//=5
print(a)
'''
#Bitwise Operator
#And & OR | XOR ^ Inversion ~ Left shift << Right shift >>
#AND &
'''
a=10
b=20
if a>b & b>a:
    print("true")
else:
    print("false")
'''
#OR |
'''
a=10
b=20
if a<b | b>a:
    print("true")
else:
    print("false")
'''
#XOR ^ first cond are true result are flase and cond are false then result is true
'''
a=10
b=20
if a>b ^ b<a:
    print("true")
else:
    print("false")
'''
# Inversion ~
'''
x=10
y=20
if ~ x!=y :
    print("true")
else:
    print("false")
'''
#Left shift <<
'''
x=20
y=10
if  x<<y :
    print("true")
else:
    print("false")
'''
# Right shift >>
'''
x=10
y=20
if  x>>y :
    print("true")
else:
    print("false")
'''
#Membership operator
#in not in 
#In
'''
s='welcome to pune'
print("to" in s)
'''
#IN NOT
'''
s='welcome  pune'
#print("to" not in s)#false to is present s
print("to" not in s)
'''
#Identity Operator
#Is is not
#is
'''
a=10
b=10
print(a is b)
'''
#is not

'''a=10
b=20
print(a is not b)'''


#In Or Not In
#In
'''str='bhagyashri is good in python'
print('is' in str)'''

#not in
'''str='python is simple and easy to learn'
print('bhagya' not in str)'''



