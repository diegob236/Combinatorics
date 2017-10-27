import os


class NegException(Exception): pass


def numnine(n):
    if n == 0 : return 0
    else: return numnine(n-1)*9 + 10**(n-1)


if __name__ == '__main__':
    RESET = '\x1b[1A'+'\x1b[2K'
    while True:
        print("---------NUMNINE---------")
        print("calculates numbers containing digit '9' between 0 and 10 ^ n - 1\n")
        print("Enter a number:")
        while True:
            try:
                n = int(input())
                if n < 0: raise NegException
                while n > 997:
                    print(2*RESET + "Please enter a smaller number:")
                    n = int(input())
                break
            except NegException: print(2*RESET+"Enter a positive number:")
            except: print(2*RESET+"Enter a valid number:")
        if n < 15:
            print("Numbers containing digit 9 in range 0 to", 10**n - 1, ":", numnine(n))
        else:
            print("Numbers containing digit 9 in range 0 to 10 ^", n, "- 1:", numnine(n))
        print("Ratio: ",  numnine(n) / (10**n - 1))
        print("Percent: ", "%.2f" % (numnine(n) / (10**n - 1) * 100), "%")
        c = ''
        print("\n\n")
        while c != 'y' and c != 'n':
            print(2*RESET+"Try again? (y/n):")
            c = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        if c == 'y': print("")
        if c == 'n': break
