"""
  0 1 1 2 3 5 8 13 21 34 55 89 144
  
fib (0)=0 
fib (1)=1
fib (2) = fib(0)+ fib(1) = 0 + 1 = 1 
fib (3) = fib(1)+ fib(2) = 1 + 1 = 2
fib (4) = fib(2)+ fib(3) = 1 + 2 = 3
fib (5) = fib(3)+ fib(4) = 2 + 3 = 5
fib (n) = fib(n - 1)+ fib(n - 2) = fib(4)+ fib(5) = 3 + 5
 """

def fib(n):
    #Base case of the recursion 
    if (n == 0 or n == 1):
        return n 
    return fib(n - 2) + fib(n - 1)

print(fib(0)) # 0
print(fib(1)) # 1
print(fib(2)) # 1
print(fib(3)) # 2
print(fib(4)) # 3
print(fib(5)) # 5