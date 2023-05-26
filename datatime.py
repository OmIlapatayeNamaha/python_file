import datetime 
'''
x = datetime.datetime.now()
print(x)
'''
#Example2
'''
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
'''
#Example3

'''x = datetime.datetime(2023,5,23)
print(x)
'''
#example4
#coverte the string formate date to datetime 
'''
input='2023/3/12'
format='%Y/%m/%d'
datet=datetime.datetime.strptime(input,format)
print(datet.date())
'''
