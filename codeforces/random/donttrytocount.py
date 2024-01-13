
def countTillSub(x: str, n: str, xlen: int, nlen: int, count: int) -> int:

    if xlen >= nlen:
        if n in x:
            return count
    

    count += 1
    x += x
    xlen = len(x)
    xlen += xlen
    return countTillSub(x, n, xlen, nlen, count)



    

if __name__ == "__main__":

    test_cases = int(input())

    for _ in range(test_cases):

        xlen, nlen = map(int, input().split())
        x = input()
        n = input()

        count = 0

        print(countTillSub(x, n, xlen, nlen, count))