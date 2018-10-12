'''print('pop up')
import ctypes  # An included library with Python install.   
ctypes.windll.user32.MessageBoxW(0,"Would you like to continue?","Virus Detected !",1)'''

'''import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET','USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

requests.get(url, auth=auth)'''


'''for i in range(100,200):
    if (i%2==0) and (i%5!=0):
        print(i)'''



'''l=[]
for i in range(100, 200):
    if (i%7!=0) and (i%5!=0):
        l.append(str(i))
print(l)'''



'''import re
xx = "guru99,education is fun"
z = re.findall(r"^\w+",xx)
print(z)'''


'''import re
xx = "guru99 education is fun"
z = re.split(r"\s",xx)
print(z)'''


'''import re
xx = "guru99s education is fun"
z = re.split(r"s",xx)
print(z)'''


'''import re
xx = "guru99 education is fun"
z = re.split(r"^/w+",xx)
print(z)'''



'''num_set = [0, 1, 2, 3, 4, 5]
for n in num_set:
  print(n)'''



'''x = set()
x.add("a")
print(x)
x.update("b","c")
print(x)'''



'''x={"a":"b","c":"d","e":"f"}
del x["a"]
print(x)'''



'''thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)'''


'''x = ("a","b")
z =  iter(x)
print(next(z))
print(next(z))'''


'''import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%B"))
print(x.strftime("%c"))'''


x = "hello hi"[::-1]
print(x)




    








    
