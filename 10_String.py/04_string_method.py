# -----------------------------------
# Python String Methods Example
# -----------------------------------

name = "hello world"   # Strings are immutable

# name[0] = "R"
# You cannot change string characters directly


# -----------------------------------
# len() -> Find length of string
# -----------------------------------
a = len(name)

print("Length of string :", a)


# -----------------------------------
# upper() -> Convert to uppercase
# -----------------------------------
print("\nupper()")
print(name.upper(), "-> Original :", name)


# -----------------------------------
# lower() -> Convert to lowercase
# -----------------------------------
print("\nlower()")
print(name.lower(), "-> Original :", name)


# -----------------------------------
# title() -> First letter of each word capital
# -----------------------------------
print("\ntitle()")
print(name.title(), "-> Original :", name)


# -----------------------------------
# capitalize() -> First letter capital
# -----------------------------------
print("\ncapitalize()")
print(name.capitalize(), "-> Original :", name)


# -----------------------------------
# replace() -> Replace word/character
# -----------------------------------
print("\nreplace()")
print(name.replace("world", "Python"))


# -----------------------------------
# find() -> Find position of word
# -----------------------------------
print("\nfind()")
print(name.find("world"))


# -----------------------------------
# count() -> Count characters
# -----------------------------------
print("\ncount()")
print(name.count("l"))


# -----------------------------------
# startswith() -> Check starting text
# -----------------------------------
print("\nstartswith()")
print(name.startswith("hello"))


# -----------------------------------
# endswith() -> Check ending text
# -----------------------------------
print("\nendswith()")
print(name.endswith("world"))


# -----------------------------------
# split() -> Convert string into list
# -----------------------------------
print("\nsplit()")
print(name.split())


# -----------------------------------
# strip() -> Remove extra spaces
# -----------------------------------
text = "   Python Programming   "

print("\nstrip()")
print(text.strip())


#Removing Whitespace
print("\n")
text = "  hello world  "
print(text.strip())  # Output: "hello world"
print(text.lstrip()) # Output: "hello world  "
print(text.rstrip()) # Output: "  hello world"
