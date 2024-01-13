   
if __name__ == '__main__':

    testcases = int(input())
    
    for _ in range(testcases):

        arr_size = int(input())
        arr = list(map(int, input().split()))

        min_diff = abs(arr[0] - arr[1])

        if arr != sorted(arr):
            print(0)
            continue

        for i in range(arr_size-1):
            diff = abs(arr[i] - arr[i+1])
            if diff < min_diff:
                min_diff = diff

        if min_diff == 0:
            print(1)
        else:
            print((min_diff//2) + 1)
