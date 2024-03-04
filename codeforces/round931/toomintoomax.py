
def maxval(arr: list[int]) -> int:
    arr = sorted(arr)
    ai = arr[-1]
    aj= arr[0]
    ak = arr[-2]
    al = arr[1]

    return abs(ai-aj) + abs(aj-ak) + abs(ak-al) + abs(al-ai)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(maxval(arr))
