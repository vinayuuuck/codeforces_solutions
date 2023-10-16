


if __name__ == '__main__':

    testcases = int(input())

    for _ in range(testcases):

        arr_size = int(input()) 
        arr = list(map(int, input().split()))

        if arr == sorted(arr):
            print(0)
            continue
        
        maxnum = 0
        sorted_arr = sorted(arr)

        for i, e in enumerate(arr):
            if abs(e - sorted_arr[i]) == 0:
                continue
            else:
                if e > maxnum:
                    maxnum = e

        print(maxnum)