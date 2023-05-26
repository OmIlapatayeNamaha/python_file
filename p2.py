#Lambda Function
b=lambda x:x*x
print(b(5))
#anonymous Function
print((lambda x:x*x)(10))

#Bubble sorted
def bubble_sort(array):
    n=len(array)
    for i in range(n):
        for j in range(n):
            if array[i]>array[j]:
                array[i],array[j]=array[j],array[i]
array=[4,6,-2,0,9,1]
bubble_sort(array)
print(array)

#maximum and minimum No
arr=[4,6,-2,0,9,1]
min=arr[0]
max=arr[0]
for num in arr:
    if num<min:
        min=num
    if num>max:
        max=num
print('minimum number: ',min)
print('maximum number: ',max)

#FizzBuzz
for i in range(1,51):
    if i%15==0:
        print('FizzBuzz')
        continue
    if i%3==0:
        print('Buzz')
        continue
    if i%5==0:
        print('Fizz')
        continue 
    print(i)

#palindrome 
a='15451'
c=a[::-1]
print(c)
if a==c:
    print("string is palindrome")
else:
    print("string is not palindrome")






