s = {23,4,353,35}
print(s)# {353, 35, 4, 23}
s.add(32) # {32, 353, 35, 4,23}
s.remove(23) # {32, 353, 35, 4}
s.discard(10) # No error if element not found n    
# s.pop() # Removes random element 
print(s) 