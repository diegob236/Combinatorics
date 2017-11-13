'''
ERDOS-GALLAI

Checks whether a list of numbers is a valid degree sequence using the Erdos-Gallai theorem.

Author: Diego Batres
Last updated: 11/12/17
'''


# NegException
#   - handles negative numbers, which are invalid degrees.
class NegException(Exception): pass


# Erdos-Gallai
#   - parameter: a list of positive degrees (ex. [2, 2, 2, 2, 2, 2])
#   - uses Erdos-Gallai theorem to validate if these numbers form a degree sequence.
#   - prints terms for each iteration
#   - returns: true if the given input is a valid degree sequence
def erdosgallai(inp):

    # k : k=1 to n
    k = 1
    # n : total number of degrees
    n = len(inp)

    # degseq : stores return value
    degseq = True

    # sumdi : sum of every degree di from i=1 to k
    # summin : sum of min(di, k) from i=k+1 to n
    sumdi, summin = 0, 0

    # For each degree di in the given degree list
    for di in inp:

        # Add di to the total sum
        sumdi += di

        # Calculate sum of min(di, k) from i=k+1 to n
        for i in range(k + 1, n + 1):
            summin += min(inp[i - 1], k)

        # Calculate k(k - 1)
        kk = k * (k - 1)

        # Print the values of each term
        print("k:", k, "=", di, "    Sum(di)i->k  = ", sumdi,
              "     k(k-1) + Sum(min(di,k))i=k+1->n  = ", kk, "+", summin, "=", kk + summin,
              "   ", sumdi, "≤", kk + summin, ":", bool(sumdi <= (kk + summin)))

        # Check if di satisfies the conditions of Erdos-Gallai
        if sumdi > (kk + summin):
            degseq = False

        # Increment k and reset value of summin
        k += 1
        summin = 0

    # Return true if input is a valid degree sequence
    return degseq


# Main method
#   - input: nonnegative numbers separated by spaces (Ex. 2 2 2 2 2 2)
#   - uses the Erdos-Gallai theorem to check if these numbers are a degree sequence
#   - prints result
if __name__ == "__main__":

    # RESET: Erases a line of terminal output
    #   - used for changing messages when an invalid input is given
    RESET = '\x1b[1A' + '\x1b[2K'

    # Print header
    print("---------ERDOS-GALLAI---------")
    print("checks whether a list of numbers is a valid degree sequence using the Erdos-Gallai theorem.\n")
    print("Enter degrees separated by spaces:")

    # Check for input until a valid sequence of numbers is given
    while True:

        # Store numbers in a list if valid
        try:
            inp = list(map(int, input().split()))
            for i in inp:
                if i < 0: raise NegException
            break

        # Prompt user for only positive numbers if a negative value is given
        except NegException:
            print(2 * RESET + "Enter only positive numbers:")

        # Prompt user for only numbers separated by spaces if the wrong input is given
        except ValueError:
            print(2 * RESET + "Enter only numbers separated by spaces:")

    # Sort degrees from highest to lowest
    inp = sorted(inp, key=int, reverse=True)

    # Print sorted list of numbers
    print(inp, "\n")

    # Check if the degree sequence is valid
    degseq = erdosgallai(inp)

    # Print results
    print("\n", inp, ("is" if degseq else "is not"), "a degree sequence" + ("!" if degseq else "."))
