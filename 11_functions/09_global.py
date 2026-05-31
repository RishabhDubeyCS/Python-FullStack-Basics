def sum (a , b ):
    print("Hey i am summing ")
    c = a + b
    global z  # plz modify global z 
    z = 12  # This will refer to global z and  not create a local variable 
    
    return c
z = 33

print (sum(2, 3))
print(z);