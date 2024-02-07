
def constructStr(trace: list[int]) -> str:
    countmap = {}
    apointer = 0
    for i, e in enumerate(trace):
        if e == 0:
            trace[i] = chr(97+apointer)
            apointer = apointer+1
    for i, e in enumerate(trace):
        if type(e) == int:
            for k, v in countmap.items():
                if v == e:
                    trace[i] = k
                    countmap[k] += 1
                    break
        else:
            if e not in countmap:
                countmap[e] = 0
            countmap[e] += 1
    return "".join(trace)

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        trace = list(map(int, input().split()))
        print(constructStr(trace))
