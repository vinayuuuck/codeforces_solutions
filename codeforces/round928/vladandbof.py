from collections import Counter

def mostFrequentCharacter(instr: str) -> str:
    strcount = Counter(instr)
    return strcount.most_common(1)[0][0]

if __name__ == "__main__":
    for _ in range(int(input())):
        print(mostFrequentCharacter(input()))
