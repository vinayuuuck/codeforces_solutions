#TLE

def constructStr(trace: list[int]) -> str:
    res = ""
    countmap = {}
    apoint = 97
    for i in range(len(trace)):
        if trace[i] == 0:
            res += chr(apoint)
            if 0 in countmap:
                countmap[0].append(chr(apoint))
            else:
                countmap[0] = [chr(apoint)]
            apoint += 1
        else:
            if trace[i]-1 in countmap:
                res += countmap[trace[i]-1].pop()
                if trace[i] in countmap:
                    countmap[trace[i]].append(res[-1])
                else:
                    countmap[trace[i]] = [res[-1]]
            else:
                return "-1"
    return res

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        trace = list(map(int, input().split()))
        print(constructStr(trace))
