from fractions import Fraction
import numpy as np
#Expected [4, 5, 5, 4, 2, 20]


def hcfnaive(a, b):
    if(b == 0):
        return a
    else:
        return hcfnaive(b, a % b)


def lcm(x):
    lcm = x[0]
    for i in x[1:]:
        lcm = lcm*i/hcfnaive(lcm, i)
    return lcm


def solution(m):
    # Edge Case

    if len(m) == 1:
        return [1, 1]

    vertices = len(m)
    # [1, 0, 0, 1]

    terminal_states = [i for i, v in enumerate(m) if v == [0]*vertices]

    if m[0] == [0]*vertices:
        return [1]+[0]*(len(terminal_states)-1)+[1]

    if len(terminal_states) == vertices:
        return [1]+[0]*(vertices - 1)+[1]

    all_states = set(range(vertices))
    t_s = set(terminal_states)
    transient_states = list(all_states.difference(t_s))
    transient_arrays = [m[i] for i in transient_states]
    transient_arrays = [[float(j)/sum(i) for j in i]
                        for i in transient_arrays]

    # Make the markov chain cannonical
    q = [[i[j] for j in transient_states] for i in transient_arrays]
    id_ = np.eye(len(q))
    r = [[i[j] for j in terminal_states] for i in transient_arrays]

    # For the case of only one transient state
    if len(transient_states) == 1:
        terminal_set = set(terminal_states)
        # difference will give the one non terminal state
        non_terminal_state = list(all_states.difference(terminal_set))[0]
        out = m[non_terminal_state]
        out.pop(non_terminal_state)
        out.append(sum(out))
        return out

    n = np.subtract(id_, q)
    n = np.linalg.inv(np.array(n))
    """n = subtract(id_, q)
    n = getMatrixInverse(n)"""
    # raw_output = np.matmul(n, np.array(r))
    # t = np.dot(n, [1, 1])
    raw_output = [Fraction(i).limit_denominator(2147483647)
                  for i in np.matmul(n, r)[0]]
    #raw_output = multiply(n, r)[0]

    max_ = lcm([i.denominator for i in raw_output])

    output = [int(max_*i) for i in raw_output]
    output.append(max_)
    return output


if __name__ == "__main__":

    print("The outcome thing looks like this:" + str(solution([
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])))
