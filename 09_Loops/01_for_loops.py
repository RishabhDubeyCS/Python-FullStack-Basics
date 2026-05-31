# print (1)
# print (2)
# print (3)
# print (4)
# print (5)
# This is a lot of code to print the numbers 1 to 5. We can use a for loop to make it easier.
for number in range(1, 6): #range function goes from 1 to 5 in this case
    print (number)
    # The range function generates a sequence of numbers. In this case, it generates the numbers from 1 to 5 (the second argument is exclusive).

for i in range(5): # This will generate numbers from 0 to 4
    print (5*(i)) # This will print the multiples of 5 from 0 to 20 (0, 5, 10, 15, 20)


lists = ['cat', 'dog', 'rabbit']
for list in lists:
    print (list)
    # This for loop iterates over the list of lists and prints each one. The variable 'list' takes on the value of each item in the list during each iteration of the loop.

fruits  = ["apple", "banana", "cherry"]
print (fruits[0]) # prints the first item in the list
print (fruits[1]) # prints the second item in the list
print (fruits[2]) # prints the third item in the list
# We can also use a for loop to iterate over the list of fruits and print each one.
for fruit in fruits:
    print (fruit)
