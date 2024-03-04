
def coinsneeded(coins: list[int], amount: int) -> int:
    return 0

if __name__ == "__main__":
    coins = [1, 3, 6, 10, 15]
    for _ in range(int(input())):
        print(coinsneeded(coins, int(input())))
