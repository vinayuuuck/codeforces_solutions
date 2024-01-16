# Solved after contest end after reading an explanation!

# Given: array a of n ints: a1, a2, ..., an
# Also given: array b of m ints: b1, b2, ..., bm where m >= n
# Return: array c of n ints such that the difference between c1 a1, c2 a2, ..., cn an is maximized

def maxDiff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    maxdiff = 0
    for i in range(len(arr1)):
        maxdiff += max(arr1[i] - arr2[len(arr1)-i-1], arr2[len(arr2)-i-1] - arr1[i])
    return maxdiff

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        print(maxDiff(arr1, arr2))
