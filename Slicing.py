#Using For Loop Reveres the string
def reveres(b):
    str=""
    for i in b:
        str=i+str
    return str
b="GeeksforGeeky"
print(b)
print(reveres(b))


#reveres the string using recursion
def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
s="Geeksforgeeks"
print(reverse(s))

#****************Reverse The String Using Stack*********************
#initializes size of stack as 0
def createStack():
    stack=[]
    return stack

#function to determine the size of the stack
def size(stack):
    return len(stack)

#Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack)==0:
        return True
    
#function to add an item to stack . it
#increases size by 1
def push(stack,item):
    stack.append(item)

#Function to remove an item from stack.
#It decreases size by 1
def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

#A stack based function to reverse a string
def reverse(string):
    n=len(string)
    #Create a empty stack
    stack = createStack()

    #Push all characters of string to stack
    for i in range(0,n,1):
        push(stack, string[i])
    
    
    # Making the string empty since all
    # characters are saved in stack
    string = ""


    # Pop all characters of string and put
    # them back to string
    for i in range(0, n, 1):
        string += pop(stack)
 
    return string

# Driver code
s = "Geeksforgeeks"
print("The original string is : ", end="")
print(s)
print("The reversed string(using stack) is : ", end="")
print(reverse(s))

 
#normal function using slicing
def reverse(string):
    for i in s:
        string = string[::-1]
        return string
s="GeekyShoow"
print(reverse(s))


#Reverse the string using join function
def reverse(string):
    for i in s:
        string = "".join(string)
        return string
s="Love you"
print(reveres(s)) 




