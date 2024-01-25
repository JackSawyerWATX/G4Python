# Python program to find factorial of a given number
# Example of a factorial of 6 is 6*5*4*3*2*1 which is 720

def factorial(n):

    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

# Driver code
num = 10
print("Factorial of", num, "is", factorial(num))

# Time Complexity: O(n)
# Auxiliary Space: O(n)