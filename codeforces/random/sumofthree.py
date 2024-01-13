
def sumofthree(n):
    if n <= 6:
        return None

    returnval = []

    if n % 3 != 0:
        returnval.append(1)
        returnval.append(2)
        returnval.append(n-3)

        return returnval

    else:
        if n == 9:
            return None
        
        else:
            returnval.append(1)
            returnval.append(4)
            returnval.append(n-5)
            return returnval

if __name__ == "__main__":


    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())

        returnval = sumofthree(n)

        if returnval:
            print("YES")
            for i, e  in enumerate(returnval):
                if i != len(returnval) - 1:
                    print(e, end=" ")
                
                else:
                    print(e)

        else:
            print("NO")