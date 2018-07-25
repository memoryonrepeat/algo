INPUT = "input.txt"


class Solver():
    def __init__(self, file):
        self.file = file

    # Parse input file into list of separate test cases
    def parse(self):
        tests = []
        input = open(self.file, "r").read().strip().split("\n")
        i = 0
        line = [int(x) for x in input[i].split()]
        while line != [0, 0, 0]:
            case = {
                "C": line[1],
                "D": line[2],
                "M": []
            }
            j = 0
            while j < line[0]:
                j += 1
                case["M"].append([int(x) for x in input[i + j].split()])
            case['M'].sort(key=lambda machine: machine[0])
            tests.append(case)
            i += j + 1
            line = [int(x) for x in input[i].split()]
        return tests

    # Solve a single test
    # The machines are previously sorted based on available days
    # Then go down the decision tree starting from earliest machines in a depth-first manner
    # The path that yields max revenue in the end will be returned
    #
    # NOTE:
    # I know that this solution has big complexity - O(2^N), and probably can be optimized
    # further by treating the prospected revenues on different machines as linear functions
    # and narrow down the search space, but since I don't have a clear proof and the naive
    # function is more comprehensive, I settled down with it.
    def solveCase(self, C, D, M, currentMachine, lastRevenueAccountingDay):
        if not M:
            if not currentMachine:
                return C
            return C + currentMachine[3] * (D - lastRevenueAccountingDay) + currentMachine[2]
        if currentMachine:
            latestRevenue = C + currentMachine[3] * (M[0][0] - lastRevenueAccountingDay - 1) + currentMachine[2]
            # not enough fund -> have to skip next machine
            if latestRevenue < M[0][1]:
                return self.solveCase(C, D, M[1:], currentMachine, lastRevenueAccountingDay)
            else:
                # go to the next level of the decision tree
                # the decision (buy/skip) that yields max revenue will be chosen
                return max(self.solveCase(C, D, M[1:], currentMachine, lastRevenueAccountingDay),
                           self.solveCase(latestRevenue - M[0][1], D, M[1:], M[0], M[0][0]))
        else:
            # not enough fund -> have to skip next machine
            if C < M[0][1]:
                return self.solveCase(C, D, M[1:], currentMachine, lastRevenueAccountingDay)
            # go to the next level of the decision tree
            # the decision (buy/skip) that yields max revenue will be chosen
            return max(self.solveCase(C, D, M[1:], currentMachine, lastRevenueAccountingDay),
                       self.solveCase(C - M[0][1], D, M[1:], M[0], M[0][0]))

    def solve(self):
        self.tests = self.parse()
        results = []
        for test in self.tests:
            results.append(self.solveCase(test['C'], test['D'], test['M'], [], 1))
        return results


if __name__ == "__main__":
    # All development and testing done on Python 3.6.1
    solver = Solver(INPUT)
    results = solver.solve()
    for result in results:
        print(result)
