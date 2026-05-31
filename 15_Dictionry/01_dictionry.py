# Dictionaries and Dictionary Methods
# Dictionaries store key-value pairs and allow fast lookup.

# Creating a Dictionary
# Dictionaries in Python
# Dictionaries store key-value pairs and allow fast lookup.

# Creating a Dictionary
student = {
    "name": "Alice",
    "age": 21,
    "grade": "A",
    "city": "Chhindwara"
}

# Display the dictionary and its type
print(student, type(student))

# Accessing dictionary values
print(student["name"])
print(student["age"])

# Updating a value
student["age"] = 22

# Display updated dictionary
print(student)
print(student["age"])

# Accessing another value
print(student["city"])

# Updating city
student["city"] = "New York"

# Display updated city and dictionary
print(student["city"])
print(student)