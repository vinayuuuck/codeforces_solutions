
def walletexchange(acoin: int, bcoin: int) -> str:
    
    if abs(acoin - bcoin) % 2 == 1:
        return "Alice"
    return "Bob"

if __name__ == "__main__":
    for _ in range(int(input())):
        i, j = map(int, input().split())
        print(walletexchange(i, j))

