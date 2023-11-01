
def sortingpossible(len, arr):
    
    if arr == sorted(arr):
        return "YES"
    
    ptr = len - 1
    while ptr > 0 and arr[ptr] >= arr[ptr - 1]:
        ptr -= 1

    if (ptr & (ptr - 1)) == 0:
        return "YES"

    return "NO"
    

if __name__ == '__main__':

    testcases = int(input())

    for _ in range(testcases):
        length = int(input())
        arr = list(map(int, input().split()))
        print(sortingpossible(length, arr))