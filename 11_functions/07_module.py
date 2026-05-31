"""
Two types of modules in Python: 
Build in  Modules 
External Modules 

 list of all the built-in modules:  https://docs.python.org/3/py-modindex.html
 

"""


import math 
import os
import mymodule
import requests #https://pypi.org/project/requests/
print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com") 
# print(r.text)
print(r.headers)
print(r.status_code)
