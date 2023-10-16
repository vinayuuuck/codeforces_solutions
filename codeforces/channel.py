def channelsolve(userStats: list, notifs: list) -> str:
    
    if userStats[0] == userStats[1]:
        return "YES"
    
    if userStats[2] == 0:
        return "NO"
    
    readers = userStats[1]

    return "NO"

if __name__ == "__main__":

    testcases = int(input())

    for _ in range(testcases):

        inputStats = list(map(int, input().split()))

        inputNotifs = list(input())

        print(channelsolve(inputStats, inputNotifs))
