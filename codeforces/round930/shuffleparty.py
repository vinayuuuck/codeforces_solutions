if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        # Check the last number which is a power of 2 smaller than or equal to n
        res = 1
        while res * 2 <= n:
            res *= 2
        print(res)
