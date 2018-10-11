#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")



'''x = ['a','b','c']
print(x[0])'''

'''x = ["apple", "banana", "cherry"]
x.pop()
print(x)'''

'''thistuple = ("apple", "banana", "cherry")
print(thistuple)'''

'''y=(1,2,3)
if 2 in y:
    print("2 is present")'''

'''y=('a','b','c')
if 'b' in y:
    print(len(y))'''

'''x=[]
for i in 'siva':
    x.append(i)
print(x)'''


'''x=[i for i in ('a','b')]
print(x)'''
     
'''x=[i for i in 'anjali']
print(x)'''

'''x=(i for i in 'anjali')
print(x)'''



'''x = [1,2,3,4,5,6,7]
z = lambda x:(x%2==0)
print(z(6))'''


'''print ('Filter')
x = [1,2,3,4,5,6,7]
z = list(filter(lambda x:(x%2==0), x ))
print(z)'''

'''print ('Filter')
#x = [1,2,3,4,5,6,7]
z =lambda x:(x%2==0)
print(z(1,2,3,4,5,6,7))
#print(z)'''




'''x = [1,2,3,4,5,6,7]
z = filter(lambda x:(x%2==0), x )
print(list(z))'''


'''x = [1,2,3,4,5,6,7]
z = list(map(lambda x:(x%2==0), x ))
print(z)'''

'''print ('Map')
x = [1,2,3,4,5,6,7]
z = list(map(lambda x:x*2, x ))
print(z)'''


'''x = [1,2,3,4,5,6,7]
z = (lambda x:x*2, x) 
print(list(z))'''


'''print('map')
a = list(map(lambda x:x,'kavitha'))
print(a)'''


'''x = list(i for i in range(10))
print(x)'''

'''x = [i for i in range(10) if x%2==0]
print(x)'''


'''number_list = [ x for x in range(10) if x % 2 == 0]
print(number_list)'''


'''x = list(i for i in range(20))
print(x)'''


'''x = list(i for i in range(20) if i%2==0 if i%3==0)
print(x)'''



x = ["even" if i%2==0 else "odd" for i in range(10) ]
print(x)





import random
print (random.randint(0,10))
print (random.random()*100)





