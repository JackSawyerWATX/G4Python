# Python3 program to add two numbers

num1 = input("\n1st number? ")
num2 = input("\n2nd number? ")

# Add the two numbers taking into account that 
# the user may input 2 numbers with a decimal.
sum = float(num1) + float(num2)

# Display the sum and print the value in as a float
print("\nThe sum of {0} and {1} is {2}" .format(num1, num2, sum))