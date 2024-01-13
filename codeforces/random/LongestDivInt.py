
def divisorInterval(num: int) -> int:
    if num == 1:
        return 1
    else:
        intLen = 1
        for i in range(2, num//2+1):
            if num % i == 0:
                intLen += 1
            else:
                intLen = 1
        return intLen
    
if __name__ == '__main__':

    i = int(input())
    testcases = [int(input()) for _ in range(i)]

    for num in testcases:
        print(divisorInterval(num))