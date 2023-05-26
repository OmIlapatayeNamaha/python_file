#.Format
#It is work with Indexing
#accessing data in pass the index position

'''
str1=("bhagya","shree")
print(f"{str1[0]}_{str1[1]}")
'''
#Example1
'''
a="{b:*<5d}"
print(a.format(b=15))

'''
#Example2

num=100
num1=200
print("{:<5d}  {:>5d}".format(num,num1))


#With Indexing
'''
a="bhagya"
b=100
print("{} {}".format(a,b))
print("{0} {1}".format(a,b))
print("{1} {0}".format(a,b))
'''

#using single print()
'''
print("my name is {}".format("Bhagya"))
print("{:*^10s}".format("bhagya"))
print("my age is{:*^4d}".format(22))
'''
#variable declaration
#Example3
'''
str="java"
str1="c"
print("{0} {1}".format(str,str1))
'''
#Example4
'''
val=10
print("decimal:{0:d}".format(val))
print("hex:{0:x}".format(val))
print("Hex:{0:X}".format(val))
print("octal:{0:o}".format(val))
print("binary:{0:b}".format(val))
'''

#F String 
#accessing the data in variable refernces
'''
name="bhagya"
age=22
sal=2000
print(f"{name}  {age} ")
print(f"{name} {sal}")
'''

#Example1
'''
a=10
b=20
value=f"{a} {b}"
print(value)
print(f"{a}")
print(f"{a} {b}")
print(f"{}")#empty expression not allowed
'''
#example2
#String
'''
s="ak"
l="shra"
print(f"{s}{l}")
print(f"{l}{s}")
print(f"{s:*<5s}{l:*>5s}")
'''

class Myerror(Exception):
    def __init__(self,msg):
        self.msg=msg
raise Myerror("its my error")

