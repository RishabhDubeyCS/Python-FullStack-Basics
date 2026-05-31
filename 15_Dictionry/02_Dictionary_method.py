# Common Dictionary Methods

student = {
    "name": "Alice",
    "age": 22,
    "grade": "A",
    "city": "New York"
}

# keys() - Returns all keys
print(student.keys())      # dict_keys(['name', 'age', 'grade', 'city'])

# values() - Returns all values
print(student.values())    # dict_values(['Alice', 22, 'A', 'New York'])

# items() - Returns all key-value pairs as tuples
print(student.items())     # dict_items([('name', 'Alice'), ('age', 22), ...])

# pop() - Removes a specified key
student.pop("age")
print(student)

# clear() - Removes all items from the dictionary
student.clear()
print(student)