# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 == 0:
    print("Cannot divide by 0")
else:
    # Dividing the numbers
    division = num1 / num2
    # Display the result
    print("The result of division is: ", int(division))
