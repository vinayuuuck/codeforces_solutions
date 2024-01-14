# Solved after looking at: https://www.youtube.com/watch?v=-kLUFQZhth0h
# Given: array a1, a2, ..., an
# First player: wants to maximise sum and removes at most k elements
# Second player: wants to minimise sum and multiplies at most x elements by -1
# Find the maximum possible sum of the resulting array

def maxSum(arr, n, k, x):
    arr.sort(reverse=True)
    
    # sum from arr[x till n] and subtract sum from arr[0 till x]
    ans = sum(arr[x:]) - sum(arr[:x])
    best = ans

    for i in range(k):
        ans += arr[i]
        if i+x < n:
            ans -= 2*(arr[i+x])
        best = max(best, ans)

    return best

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        arr = list(map(int, input().split()))
        print(maxSum(arr, n, k, x))
