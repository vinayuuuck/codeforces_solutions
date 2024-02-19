# a is 1, b is 2, ... z is 26
# given int n return lexicographically smallest string of length 3 with sum of corresponding numbers equal to n

def recoversmallstring(n: int) -> str:
    pos1 = 1
    pos2 = 1
    pos3 = n-2
    while pos3 > 26:
        pos2 += 1
        pos3 -= 1
    while pos2 > 26:
        pos1 += 1
        pos2 -= 1
    return chr(pos1 + 96) + chr(pos2 + 96) + chr(pos3 + 96)

if __name__ == "__main__":
    for _ in range(int(input())):
        print(recoversmallstring(int(input())))
