# Python program to find
# the factorial of a given number 2

# Function to find the factorial
def factorial(n):

    res = 1

    for i in range(2, n + 1):
        res *= i
    return res

#Driver code
num = 16
print("Factorial of", num, "is", factorial(num))

# Time Complexity: O(n)
# Auxiliary Space: O(n)