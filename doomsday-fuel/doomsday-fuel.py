from fractions import Fraction


def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeterminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    d = 0
    for c in range(len(m)):
        d += ((-1)**c)*m[0][c]*getMatrixDeterminant(getMatrixMinor(m, 0, c))

    return d


def getMatrixInverse(m):
    d = getMatrixDeterminant(m)

    if d == 0:
        raise Exception("Cannot get inverse of matrix with zero determinant")

    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/d, -1*m[0][1]/d],
                [-1*m[1][0]/d, m[0][0]/d]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/d
    return cofactors


def identity(t):
    m = []
    for i in range(t):
        r = [int(i == j) for j in range(t)]
        m.append(r)
    return m


def multiply(a, b):
    m = []
    rows = len(a)
    cols = len(b[0])
    iters = len(a[0])

    for r in range(rows):
        mRow = []
        for c in range(cols):
            sum = 0
            for i in range(iters):
                sum += a[r][i]*b[i][c]
            mRow.append(sum)
        m.append(mRow)
    return m


def subtract(i, q):
    s = []
    for r in range(len(i)):
        sRow = [i[r][c] - q[r][c] for c in range(len(i[r]))]
        s.append(sRow)
    return s


def solution(m):
    # Edge Case
    if len(m) == 1:
        return [1, 1]

    vertices = len(m)

    terminal_states = [i for i, v in enumerate(m) if v == [0]*vertices]

    if len(terminal_states) == vertices:
        return [1]+[0]*(vertices - 1)+[1]

    all_states = set(range(vertices))
    t_s = set(terminal_states)
    transient_states = list(all_states.difference(t_s))
    transient_arrays = [m[i] for i in transient_states]
    transient_arrays = [[Fraction(j, sum(i)) for j in i]
                        for i in transient_arrays]

    # Make the markov chain cannonical
    q = [[i[j] for j in transient_states] for i in transient_arrays]
    id_ = identity(len(q))
    r = [[i[j] for j in terminal_states] for i in transient_arrays]

    # For the case of only one non terminal state
    if len(transient_states) == 1:
        all_states = set(range(vertices))
        terminal_set = set(terminal_states)
        # difference will give the one non terminal state
        non_terminal_state = list(all_states.difference(terminal_set))[0]
        out = m[non_terminal_state]
        out.pop(non_terminal_state)
        out.append(sum(out))
        return out

    n = subtract(id_, q)
    n = getMatrixInverse(n)
    # t = np.dot(n, [1, 1])
    # [Fraction(i).limit_denominator(50000)for i in multiply(n, r)[0]]
    raw_output = multiply(n, r)[0]

    max_ = max(i.denominator for i in raw_output)

    output = [int(max_*i) for i in raw_output]
    output.append(max_)
    return output


if __name__ == "__main__":

    print("The outcome thing looks like this:" + str(solution([
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]])))
