
def whoWins(a: int, b: int, c: int) -> str:
    
    if a - b < 0:
        return "Second"
    elif a - b == 0:
        if c % 2 == 0:
            return "Second"
        else:
            return "First"
    else:
        return "First"


if __name__ == "__main__":

    t = int(input())

    for i in range(t):
        a, b, c = map(int, input().split())
        print(whoWins(a, b, c))