"""
def  sum (a, b):
    #a and b are local variables 
    c = a + b 
    # print(z) # z is a global variable
    z = 1;  # It creates a local variable called z which is destroyed  after this  function returns 

    return c 
z= 10
def greet ():
    z = 32 # Local variable 
    print ("Hello World")

print(sum(2, 3))    
print(z)


"""


x = 8  # Global variable
def func1 ():
    x = 20  # Local variable
    print(x) # output: 20
    
    func1();

print(x) # output: 8