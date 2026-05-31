a = 34 ;
b  = "34" ;
d = 223; 

print(a) # 34
print(type(a)) # <class 'int'>

print(b) # 34
print(type(b)) # <class 'str'>

# Convert b to an integer
c = int(b) ;
print(c) # 34
print(type(c)) # <class 'int'>

e = str (d);
print(e) # 223
print(type(e)) # <class 'str'>

# Convert string to integer
num_str = 54;
num_int = int (int(num_str));
print(num_int) # 54
print(type(num_int));

# Convert integer to string 
num = 25 ;
num_str = str(num);
print(num_str) # 25
print(type(num_str)) # <class 'str'>

#Convert float to integer 
pi = 3.14 ;
pi_int = int(pi);
print(pi_int) # 3
print(type(pi_int)) # <class 'int'>