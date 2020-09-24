import numpy as np
from fractions import Fraction


def matrix_addition(x, y):
    out = []
    for i, j in zip(x, y):
        inner = [k+l for k, l in zip(i, j)]
        out.append(inner)
    return out


def matrix_subtraction(x, y):
    out = []
    for i, j in zip(x, y):
        inner = [k-l for k, l in zip(i, j)]
        out.append(inner)
    return out


def identity(x):
    """Produce an identity matrix

    Args:
        x (int): the n by n dimension of the identity matrix

    Returns:
        list: A list of lists representing the identity matrix
    """
    # n = len(x)
    n = x
    n_list = list(range(n))
    out = []
    for i in n_list:
        inner = [0]*n
        inner[i] = 1
        out.append(inner)
    return out


class Graph():
    def __init__(self, matrix):
        """Constructor for graph class

        Args:
            matrix (2d list): a list of lists that each represent represent state
        """
        self.matrix = matrix
        self.vertices = len(self.matrix)
        self.edges = 0
        for vertex in self.matrix:
            for edge in vertex:
                if edge > 0:
                    self.edges += 1

        self.terminal_states = []
        for i, v in enumerate(self.matrix):
            if v == [0]*self.vertices:
                self.terminal_states.append(i)

    def breadth_first_search(self):
        """Breadth first search of a graph
        Use to identify unreachable states
        """
        visited = set([0])
        queue = [0]
        while len(queue) != 0:
            x = queue.pop(0)
            for i, j in enumerate(self.matrix[x]):
                if i not in visited and j > 0:
                    visited.add(i)
                    queue.append(i)
        return list(visited)

    def graph_traversal(self):
        x = 0
        # Increase respective index by 1 everytime its visited
        outcome = [0]*self.vertices
        outcome[0] = 1
        prob_0 = 1
        x_history = [0]  # history of visited nodes/states
        vert_array = [i for i in range(self.vertices)]
        while x not in self.terminal_states:
            vertex_denominator = sum(self.matrix[x])
            prob = [i/vertex_denominator for i in self.matrix[x]]
            x = np.random.choice(vert_array, p=prob)
            prob_0 *= prob[x]
            outcome[x] += 1
            x_history.append(x)
        return prob_0.as_integer_ratio(), x_history  # r

    def canonize(self):
        q, r = [], []
        all_states = set(range(self.vertices))
        t_s = set(self.terminal_states)
        transient_states = list(all_states.difference(t_s))
        # select the transient state arrays from the matrix
        transient_arrays = [self.matrix[i] for i in transient_states]
        transient_arrays = [[j/sum(i)
                             for j in i] for i in transient_arrays]
        # build q, grab transient states in the transient arrays
        q = [[i[j] for j in transient_states] for i in transient_arrays]
        i = identity(len(q))
        # build r, grab terminal states from transient arrays
        r = [[i[j] for j in self.terminal_states] for i in transient_arrays]

        return np.array(q), np.array(r), np.array(i)


def solution(m):

    if len(m) == 1:
        return [1, 1]

    g = Graph(m)
    # For the case of only one non terminal state
    if len(g.terminal_states) == len(m) - 1:
        all_states = set(range(len(m)))
        terminal_set = set(g.terminal_states)
        # difference will give the one non terminal state
        non_terminal_set = list(all_states.difference(terminal_set))[0]
        out = m[non_terminal_set]
        out.pop(non_terminal_set)
        out.append(sum(out))
        return out

    q, r, i = g.canonize()
    n = np.subtract(i, q)
    n = np.linalg.inv(n)
    raw_output = [Fraction(i).limit_denominator(100) for i in np.dot(n, r)[0]]

    max_ = -1
    for i in raw_output:
        if i.denominator > max_:
            max_ = i.denominator

    output = []
    for i in raw_output:
        factor = max_/i.denominator
        output.append(int(factor*i.numerator))
    output.append(max_)
    return output
    # return [21*i for i in np.dot(n, r)[0]]


if __name__ == "__main__":

    print("The outcome thing looks like this: ", solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [
          0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
