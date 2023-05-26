#Python Program To Calculate Electricity Bill
#using and oprator
u=int(input('enter the units :'))
if u<=100:
    bill=u*4
    print(bill)
elif u>100 and u<=200:
    bill=u*5
    print(bill)
elif u>200 and u<300:
    bill=u*6
    print(bill)
elif u>300 and u<400:
    bill=u*7
    print(bill)
else:
    print('Hello')