# given old cat row with 1s and 0s, desired new cat row with 1s and 0s

def numMoves(oldCatRow, newCatRow):
    changeoldcat = 0
    changenewcat = 0

    for i, e in enumerate(oldCatRow):
        if e == "1" and oldCatRow[i] != newCatRow[i]:
            changeoldcat += 1
        elif e == "0" and oldCatRow[i] != newCatRow[i]:
            changenewcat += 1

    return max(changeoldcat, changenewcat)

if __name__ == "__main__":
    for _ in range(int(input())):
        numboxes = int(input())
        oldCatRow = [*input()]
        newCatRow = [*input()]
        # print(oldCatRow, newCatRow)
        print(numMoves(oldCatRow, newCatRow))
