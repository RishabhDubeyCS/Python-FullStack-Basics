print("Simple Calculator")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == "1":
    result = num1 + num2
    operator = "+"
elif choice == "2":
    result = num1 - num2
    operator = "-"
elif choice == "3":
    result = num1 * num2
    operator = "*"
elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
        raise SystemExit
    result = num1 / num2
    operator = "/"
else:
    print("Invalid choice. Please run the program again and select 1, 2, 3, or 4.")
    raise SystemExit

print(f"{num1} {operator} {num2} = {result}")
