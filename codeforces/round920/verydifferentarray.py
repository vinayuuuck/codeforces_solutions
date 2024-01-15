# Given array of n integers: a1, a2, ..., an
# Given another array of m ints: b1, b2, ..., bm and m >= n
# Find array of n ints: c1, c2, ..., cn from second array such that the difference ai - ci is maximised

def maxDiff(a, b):
    a.sort()
    b.sort(reverse=True)
    
    # If len(a) == len(b): then we can just return the sum of the differences between a and b
    if len(a) == len(b):
        return sum([abs(a[i] - b[i]) for i in range(len(a))])

    # That leaves the case where len(a) < len(b).
    # If len(a) is even then we map the first half of a, i.e., a[0] to b[0], a[1] to b[1], etc. till a[n/2] to b[n/2]
    # and the second half of a, i.e., a[-1] to b[-1], a[-2] to b[-2], etc. till a[-n/2] to b[-n/2]

    # If len(a) is odd then we map the first half of a, i.e., a[0] to b[0], a[1] to b[1], etc. till a[n/2] to b[n/2]
    # and the second half of a, i.e., a[-1] to b[-1], a[-2] to b[-2], etc. till a[-n/2] to b[-n/2]
    # and then find the best possible remaining value from b to map to the middle element of a
    
    if len(a) % 2 == 0:
        return sum([abs(a[i] - b[i]) for i in range(len(a) // 2)]) + sum([abs(a[-i-1] - b[-i-1]) for i in range(len(a) // 2)])
    else:
        maxdiff = 0
        for i in range(len(a) // 2):
            maxdiff += abs(a[i] - b[i]) + abs(a[-i-1] - b[-i-1])
   
        aval = a[len(a) // 2]
        possiblemax = 0
        for i in range(len(a) // 2, len(b) - len(a) // 2):
            possiblemax = max(possiblemax, abs(aval - b[i]))

        return maxdiff + possiblemax

if __name__ == '__main__':

    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        print(maxDiff(a, b))

# Wrong answer on test 2. Need to fix.
