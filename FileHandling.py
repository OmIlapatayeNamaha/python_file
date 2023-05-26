# a=open('abc.txt', 'r')
# print(a.read())
# a.close()

# f=open('xyz.txt','w')
# f.write('I am software developer')
# f.close()


# f=open('xyz.txt','r')
# d = f.read()
# print(d)
# f.close()

with open('xyz.txt','r') as f:
    d = f.read()
print(d)
