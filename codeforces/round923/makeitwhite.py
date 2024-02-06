
def minLen(cells):
    if cells.find('B') == -1:
        return 0
    return cells.rfind('B') - cells.find('B') + 1

if __name__ == "__main__":
    for _ in range(int(input())):
        celllen = int(input())
        cells = input()
        print(minLen(cells))
