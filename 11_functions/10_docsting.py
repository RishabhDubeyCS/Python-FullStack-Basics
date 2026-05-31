def employee(name, age, salary):

    """
    This function takes three parameters: name, age, and salary.
    It prints out the employee's information in a formatted string.
    """

    print(f"Employee Name: {name}, Age: {age}, Salary: ${salary:.2f}")
    print(employee.__doc__)   # Print docstring


# Function call OUTSIDE the function
employee("Rishabh Dubey", 30, 75000.00)




 # ---------------------------Example 2---------------------------
def sum (a, b):
    """
    This function takes two parameters, a and b, and returns their sum.
    """
    c = a + b
    return c

print(sum.__doc__)  # Print docstring
print(sum(5, 7))

def add (x ,y):
    """
    Returns the sum of x and y.
    Parameters:
    x(int): The first number to add.
    y(int ): The second number to add.
    Returns:
    int:  The sum of the two numbers.
    
    
"""
    return x + y  
print(add.__doc__)  # Print docstring
print(add(5, 7))