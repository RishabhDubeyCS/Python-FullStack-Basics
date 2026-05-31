"""
match value :
 case pattern1:
    # code to execute if pattern1 matches value
    case pattern2:
    # code to execute if pattern2 matches value
    case _:
    # default case (if no patterns match value)


"""

#Example 1



from unittest import case


a  = int (input("Enter a number: "))
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("Better luck next time!")
#Example 2
day = input ('enter a day of the week:         ')
match day:
    case"Monday":
        print("Today is Monday.")
    case "Tuesday":
        print("Today is Tuesday.")
    case "Wednesday":

        print("Today is Wednesday.")
    case "Thursday":
        print("Today is Thursday.")
    case "Friday":
        print("Today is Friday.")
    case "Saturday":
        print("Today is Saturday.")
    case "Sunday":
        print("Today is Sunday.")   
    case _:
        print("Invalid day of the week.")
# example 3
b = int (input ("Enter a number between 1 and 5:    "))
match b:
    case 1:
        print("you won a charger ")
    case 2:
        print("you won a phone ")
    case 3:
        print("you won a laptop ")
    case 4:
        print("you won a tablet ")
    case 5:
        print("you won a smartwatch ")
    case _:
        print("Invalid number. Please enter a number between 1 and 5.")

    #example 4
status = 404

match status:
    case 200:
        print("Success!")
    case 404:
        print("Not Found")
    case _:
        print("Unknown Status")