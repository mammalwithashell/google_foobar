def solution(total_lambs):
    #print("Total LAMBS:", total_lambs)
    fib1 = 1
    fib2 = 1
    fib_add = 0
    lamb_sum = 0
    hench_n_stingy, hench_n_generous = -1, 0
    # loop to run stingy (fibonacci)
    #print("Stingy Hench: ", end="")
    while lamb_sum <= total_lambs:
        #print(fib_add, end=" ")
        fib1 = fib2
        fib2 = fib_add
        fib_add = fib1 + fib2
        lamb_sum += fib_add
        hench_n_stingy += 1
    #print("\nStingy Sum: ", lamb_sum - fib_add)
    #print("Stingy N:", hench_n_stingy)

    lamb_sum, x = 0, 1
    #print("Generous Hench: ", end='')
    while lamb_sum + x <= total_lambs:
        #print(x, end=" ")
        hench_n_generous += 1
        lamb_sum += x
        x *= 2
    #print("\nGenerous Sum: ", lamb_sum)
    #print("Generous N:", hench_n_generous)

    return hench_n_stingy - hench_n_generous


if __name__ == "__main__":
    print("The solution is:", solution(51))
