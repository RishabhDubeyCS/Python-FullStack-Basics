"""
if condition1
# Code to execute if conditional is True 
Elif condition2
# Code to execute if condition2 is True

else : 
# Code to execute if all conditions are False 


"""
# Example 1
name = input("What is your name? ")
age = int(input("What is your age? "))

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")


# Example 2
number = int (input("Enter a number: "))
if number >0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:   print("The number is zero.")


# Example 3
temperature = float (input ("Enter the temprature"))
if temperature >30:
    print("it is hot outside .")
elif temperature>20:
    print("it is warm outside .")
else :
    print("it is cold outside .")

