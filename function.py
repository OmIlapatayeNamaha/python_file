#Function
#Function is group of statatements
#built in funtion-->print(),upper()
def add():  #Defination
    x=10
    y=20
    c=x+y
    print(c)
add()  #Calling Function


#Return Statement
def add(y):
    x=10
    c=x+y
    return c #Arg
a=add(20)
print(a)

#return expression
def add(y):
    x=20
    return x+y 
a=add(50)
print(a)

#return multiple expression
def add(y):
    x=10
    c=x+y
    d=y-x
    return c, d
a,b=add(20)
print(a)
print(b)

#Nested Function
def disp():
    def show():
        print("Show Function")
    print("Disp Function")
    show()
disp()

#Example2
def disp():
    def show():
        return "show function"
    result=show() + " disp function "
    return result
a=disp()
print(a)

# example3
def disp(st):
    def show():
        return "Show Function" 
    result=show()+st+" Disp Function"
    return result
print(disp("Bhagya"))

#Pass a function as parameter
def disp(sh):
    print("disp function" + sh())
def show():
    return "Show Function"
disp(show)

#Function return another function
def disp():
    def show():
        return "Show Function"
    print("Disp Function")
    return show
sh=disp()
print(sh())

#Actual and Formal Argument
def sum(x,y):#Formal Paramenters
    c=x+y
    print(c)
sum(10,2)#Actual Paramenters

#Types of Actual Arguments
#1.Positional Arguments
def pw(x,y):
    z=x**y
    print(z)
pw(5,2)


#EX2
def pw(x,y):
    z=x**y
    print(z)
pw(2,5)

#EX3
'''
def pw(x,y):
    z=x**y
    print(z)
pw(2,5,6)#Typeerror
'''
li=[1,2,3]
l1=li*4
print(l1)


