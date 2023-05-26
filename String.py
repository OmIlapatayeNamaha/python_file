#Creating string
'''
st="bhagyashree"
print(st)
'''
#Slicing in String
'''
st="welcom in pune"
print(st[1:3])
print(st[3:5])
print(st * 6) #print the string in multi time

#exampl2
s="Hello"
for i in s:
    print(i)

print(s[:]) #hello
print(s[1:])#ello
print(s[:5])#hello
print(s[:3])#hel
print(s[2:4])#ll
print(s[:-1])#hell
print(s[-5:])#hell
print(s[:-3])#he
'''
#String Methods
#Upper()
'''
str="SHREE"
print(str.isupper())
'''
#lower()
'''
str="shreee"
print(str.islower())
'''
#swapcase()
'''
str='bhagyashree'
print(str.swapcase())#all lower string in convert the upper case
'''
#title()
'''
str="pune"
print(str.title()) #first character are upper and remaing are lower
'''
#find()
'''
str="welcom to pune"
print(str.find("to"))#find only t index position becouse o is 2 times present in string
'''
#index()
'''
str="i am in pune"
print(str.index("n"))#6
print(str.index("b"))#substring not found
'''
#isdigit()
'''
str='12'
print(str.isdigit())#only digits
'''
#isalph()
'''
str='Chshdj'
print(str.isalpha())#one character are upper case present in string else con false
'''
#alnum()
'''
str='Charater24'
print(str.isalnum())# this string present in all upper and lower case and No are present the cod are true else false
'''
#isspace()
'''
str='  '
print(str.isspace())#this method only contains space then true else false
'''
#lstrip()
'''
str='  bhagya'
print(str.lstrip())#remove the space in left side
'''
#rstrip()
str='bhagya   '
print(str.rstrip())

#strip()
'''
str="  bha  gya  "
print(str.strip())#remove the space in both side
'''
#replace()
'''
str='i am bhagya'
s=str.replace("bhagya","shree")#replace the string in bhagya to shree
print(s)
'''
#split()
'''
str='i am bhagyshree how are you'
print(str.split())#split in string and return in list
'''

#join()
'''
str='bhagya'
x="hello" .join(str)
print(x)
'''
#Example
'''
str1 = str("python")
str2 ="python"
print(str1==str2,str1 is str2)
'''
#rfind
'''s="hii bhagya how are you"
x=s.rfind('q')
print(x)
'''

'''
a=10
b=20
a,b=b,a
print(a,b)
'''
#-0 slicing
'''
my_str="python.hub"
print(my_str[-0])
'''