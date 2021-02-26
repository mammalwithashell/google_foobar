from decimal import getcontext, Decimal
from sys import setrecursionlimit
setrecursionlimit(10**7)
getcontext().prec = 100
memo = {0:0, 1:0, 2:1, 3:2}
def solution(b):
    b = Decimal(b)
    try:
        return memo[int(b)]
    except KeyError:
        if int(b)%2 == 0:
            memo[int(b)] = solution(b/Decimal(2)) + 1
        else:
            memo[int(b)] = min(solution(b-Decimal(1)), solution(b+Decimal(1))) + 1
        return memo[int(b)]

if __name__ == "__main__":
    print(solution(170074246395587102010262162311239610835104933121033118035535176239518682102210950188070227104781548037710010210514868710669819055022064800471233833439176458238850362598407948105854744718702780537106108163682107703516311096183790032053750873713085910327612814359004643083835410630890605568147534997737823811010053168485106894298103))
    print(memo)