import os


class NegException(Exception): pass


def erdosgallai(inp):
    k = 1
    n = len(inp)
    degseq = True
    sumdi, summin, term2 = 0, 0, 0
    for di in inp:
        sumdi += di
        for i in range(k + 1, n + 1):
            # print("di,k =", inp[i-1], k)
            # print("min(di,k)=", min(inp[i-1], k))
            summin += min(inp[i - 1], k)
        # print("summin:", summin)
        kk = k * (k - 1)
        print("k:", k, "=", di, "    Sum(di)i->k  = ", sumdi,
              "     k(k-1) + Sum(min(di,k))i=k+1->n  = ", kk, "+", summin, "=", kk + summin,
              "   ", sumdi, "≤", kk + summin, ":", bool(sumdi <= (kk + summin)))
        if sumdi > (kk + summin):
            degseq = False
        k += 1
        summin = 0
    return degseq

if __name__ == "__main__":
    RESET = '\x1b[1A' + '\x1b[2K'
    while True:
        print("---------ERDOS-GALLAI---------")
        print("checks whether a list of numbers is a valid degree sequence using the Erdos-Gallai theorem.\n")
        print("Enter degrees separated by spaces:")
        while True:
            try:
                inp = list(map(int, input().split()))
                for i in inp:
                    if i < 0: raise NegException
                break
            except NegException:
                print(2*RESET+"Enter only positive numbers:")
            except ValueError:
                print(2*RESET+"Enter only numbers separated by spaces:")
        inp = sorted(inp, key=int, reverse=True)
        print(inp, "\n")
        degseq = erdosgallai(inp)
        print("")
        print(inp, ("is" if degseq else "is not"), "a degree sequence"+("!" if degseq else "."))
        c = ''
        print("\n\n")
        while c != 'y' and c != 'n':
            print(2 * RESET + "Try again? (y/n):")
            c = input()
        os.system('cls' if os.name == 'nt' else 'clear')
        if c == 'y': print("")
        if c == 'n': break
