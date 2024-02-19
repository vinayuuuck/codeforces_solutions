# input is nxn matrix of 0s and 1s
# output is "SQUARE" or "TRIANGLE"
# find first occurence of 1 in the matrix and the last occurence of 1 in the matrix, if there are other ones in the first row and last row, then it is a square, otherwise it is a triangle
from collections import Counter

def findShape(matrix: list[list[int]]) -> str:
    n = len(matrix)
    firstflag = False
    firstcheck = False
    lastflag = False
    lastcheck = False
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "1":
                firstcheck = True
                rowcount = Counter(matrix[i])
                if rowcount["1"] > 1:
                    firstflag = True
                    break
                break
        if firstcheck:
            break
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if matrix[i][j] == "1":
                lastcheck = True
                rowcount = Counter(matrix[i])
                if rowcount["1"] > 1:
                    lastflag = True
                    break
                break
        if lastcheck:
            break
    if firstflag and lastflag:
        return "SQUARE"
    return "TRIANGLE"

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        matrix = []
        for _ in range(n):
            row = list(input())
            matrix.append(row)
        print(findShape(matrix))
