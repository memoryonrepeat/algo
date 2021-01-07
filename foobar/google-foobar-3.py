# gearing-up-for-destruction
def solution(pegs):
    # brute force with upper bound = peg distance - 1, lower bound = 1
    maximum = pegs[1] - pegs[0] - 1
    # r0 = radius of first gear
    for r0 in range(1, maximum):
        eliminated = False
        gear_sizes = [r0]
        for i in range(1, len(pegs)):
            next_gear_size = pegs[i] - (pegs[i-1] + gear_sizes[-1])
            if next_gear_size < 1:
                eliminated = True
                break
            else:
                gear_sizes.append(pegs[i] - (pegs[i-1] + gear_sizes[-1]))
        
        if eliminated:
            continue

        if r0 == 2 * gear_sizes[-1]:
            return [r0, 1]
        if r0+1 == 2 * gear_sizes[-1]:
            return [(r0 * 3) + 1, 3]
        if r0+2 == 2 * gear_sizes[-1]:
            return [(r0 * 3) + 2, 3]

    return [-1, -1]

pegs = [1,3]
print(solution(pegs))