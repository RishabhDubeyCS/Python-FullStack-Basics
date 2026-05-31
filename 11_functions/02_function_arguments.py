def add (a, b ):
    # return a + b
    x = a + b
    return x

c = add(3, 5)
print(c)


def employee_info (name , age , department   ):
    data = "Name: " + name + ", Age: " + str(age) + ", Department: " + department 
    return data
info = employee_info("Rishabh ", 30, "IT")
info1 = employee_info("Alice ", 25, "HR")   

print(info)
print(info1)


