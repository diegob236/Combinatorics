'''
"NUMNINE"

Calculates numbers containing digit '9' between 0 and (10 ^ n) - 1
Ex. n = 3 results in a range 0 - 999

Author: Diego Batres
Last updated: 11/12/17
'''

# NegException
#   - handles invalid negative numbers.
class NegException(Exception): pass

# Numnine
#   - input: 0 <= n <= 996 (maximum recursion)
#   - formula: numnine(n-1)*9 + 10^(n-1)
#   - returns: amount of numbers containing 9
def numnine(n):

    # Base case : return 0
    if n == 0 : return 0

    # Recursive case : use the formula N*9 + 10^(n-1) where N is numnine(n-1)
    else: return numnine(n-1)*9 + 10**(n-1)

# Main method
#   - input: 0 <= n <= 996
#   - calculates the amount of numbers containing a digit '9' between 0 and (10 ^ n) - 1
if __name__ == '__main__':

    # RESET : Erases a line of terminal output
    #   - used for changing messages when an invalid input is given
    RESET = '\x1b[1A'+'\x1b[2K'

    # Print header
    print("---------NUMNINE---------")
    print("calculates numbers containing digit '9' between 0 and (10 ^ n) - 1\n")
    print("Enter a number:")

    # Check for input until a valid number is given
    while True:

        # Get input from user
        try:
            n = int(input())

            # Handle invalid input
            if n < 0: raise NegException
            while n > 997:
                print(2*RESET + "Please enter a smaller number:")
                n = int(input())
            break

        # Prompt user for a positive number if a negative value is given
        except NegException: print(2*RESET+"Enter a positive number:")

        # Prompt user for a number if the wrong input is given
        except: print(2*RESET+"Enter a valid number:")

    # Print out the entire range
    if n < 15:
        print("Numbers containing digit 9 in range 0 to", 10**n - 1, ":", numnine(n))

    # Print as a power of 10
    else:
        print("Numbers containing digit 9 in range 0 to ( 10 ^", n, ") - 1:", numnine(n))

    # Print ratio of numbers containing 9
    print("Ratio: ",  numnine(n) / (10**n - 1))

    # Print percent of numbers containing 9
    print("Percent: ", "%.2f" % (numnine(n) / (10**n - 1) * 100), "%")
