# Python program that finds simple interest.
# Principal amount, time, and rate of interest
# taken from user.

def simple_interest(p, t, r):
    print("The principal is:              $", p)
    print("The time period is:           ", t, "months")
    print("The interest rate is:         ", r,"%")

    si = (p * t * r)/100

    print("The simple interest rate is:  ", si, "%")

# Driver code
P = int(input("Enter the principal amount: "))
T = int(input("Enter the time period: "))
R = int(input("Enter the interest rate: "))
simple_interest(P,T,R)


# Time complexity: O(1)
# Auxiliary Space: O(1) 