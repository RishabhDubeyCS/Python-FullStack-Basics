# Simple Python examples for escape sequences

print("Hello\nWorld")          # \n new line
print("1\t2\t3")              # \t tab spacing
print("She said, \"Hello!\"")  # \" double quote inside string
print('It\'s easy to learn.')     # \' single quote inside string
print("C:\\Users\\Public")     # \\ backslash in path
print("First line\rSecond")      # \r carriage return (overwrites beginning on some consoles)
print("Oops\b!")                # \b backspace removes previous character
print("Bell sound\a")           # \a alert/bell (may not sound in all terminals)

# raw string keeps backslashes as literal characters
print(r"Raw string: C:\Users\Public\Documents")