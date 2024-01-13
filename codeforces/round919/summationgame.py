# Given: array a1, a2, ..., an
# First player: wants to maximise sum and removes at most k elements
# Second player: wants to minimise sum and multiplies at most x elements by -1
# Find the maximum possible sum of the resulting array

def maxSum(arr, k, x):
    pass

if __name__ == '__main__':

    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(maxSum(arr, k, x))
