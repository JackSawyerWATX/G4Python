# Python program to find compound interest
# from user input using pow() function

def compound_interest(principal, rate, time):

    # Calculates the compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is: ", CI)

# Driver code
# Takes input from user
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter the interest rate: "))
time = int(input("Enter the amount of time in years: "))

# Function call
compound_interest(principal, rate, time)