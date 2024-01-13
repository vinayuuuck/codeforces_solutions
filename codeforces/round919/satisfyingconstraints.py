# Constraint of the form (1 x): return all integers >= x
# Constraint of the form (2 x): return all integers <= x
# Constraint of the form (3 x): return all integers != x
# We have to return the number of integers that satisfy all constraints

def possibleInts(constraints):
    '''
    Return the abs value of the difference between lower and upper bounds
    of the constraints subtracted by the number of integers that are in the 3rd type of constraint
    '''
    
    lowerBound = -1000000000
    upperBound = 1000000000
    forbidden = []

    for constraint in constraints:
        if constraint[0] == '1':
            lowerBound = max(lowerBound, int(constraint[1]))
        elif constraint[0] == '2':
            upperBound = min(upperBound, int(constraint[1]))
        else:
            forbidden.append(int(constraint[1]))

    # if the lower bound is greater than the upper bound, there are no possible integers
    if lowerBound > upperBound:
        return 0

    numForbidden = 0
    for i, e in enumerate(forbidden):
        if e >= lowerBound and e <= upperBound:
            numForbidden += 1

    return abs(upperBound - lowerBound) + 1 - numForbidden # +1 because we have to include the upper bound

if __name__ == '__main__':
    
    for i in range(int(input())):
        
        # first line is number of constraints
        numConstraints = int(input())
        constraints = []
        # the constraints are in the form: x, y

        for j in range(numConstraints):
            constraints.append(input().split())

        print(possibleInts(constraints))
