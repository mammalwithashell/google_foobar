import itertools

def solution(time, time_limit):
    rows = len(time)
    bc = rows - 2

    # Floyd Warshal algorithm to detect negative cycles
    for i in range(rows):
        for j in range(rows):
            for k in range(rows):
                time[j][k] = min(time[j][k], time[j][i] + time[i][k])

    # if any diagonal values have a value less than 0
    for r in range(rows):
        if time[r][r] < 0:
            return [i for i in range(bc)]

    # walu through every permutation until we find one that can pass under the time limit
    for i in reversed(range(bc + 1)):
        for perm in itertools.permutations(range(1, bc + 1), i):
            perm = list(perm)
            perm = [0] + perm + [-1]
            path = [(perm[i - 1], perm[i]) for i in range(1, len(perm))]
            total_time = sum(time[start][end] for start, end in path)
            if total_time <= time_limit:
                perm.pop(0)
                perm.pop()
                return sorted([i - 1 for i in perm])
    return None

if __name__ == '__main__':
    print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))