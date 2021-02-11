"""Find the max product of some non-empty subset of the list xs
        Idk if anyone reads this but I found the max product of subset problem solved on geeks for geeks
        I understood it before 
        We stand on the shoulders of giants am I right?
    Args:
        xs (list): input list
    """


def solution(xs):
    if len(xs) == 1:
        return str(xs[0])

    mn = -999999  # max negative
    nn, nz = [0]*2  # nn = number of negatives
    product = 1
    for x in xs:
        if x == 0:
            nz += 1
            continue
        if x < 0:
            nn += 1
            mn = max(mn, x)  # maybe use the absolute value here
        product *= x

    if nz == len(xs):
        return str(0)

    if nn & 1:  # If number negative is odd
        if nn == 1 and nz > 0 and nn + nz == len(xs):
            return 0
        product = int(product/mn)
    return str(product)


if __name__ == "__main__":
    print("The solution is:", solution([999, -999, -5, -2, 4, -7]))
