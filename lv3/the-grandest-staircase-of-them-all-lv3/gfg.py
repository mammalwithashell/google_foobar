def print1(idx):
    for i in range(1, idx, 1):
        print(dp[i], end=" ")
    print("\n", end="")

# Function to find all the unique partitions
# remSum = remaining sum to form
# maxVal is the maximum number that
# can be used to make the partition


dp = [0 for _ in range(200)]


def solve(remSum, maxVal, idx, count):
    # If remSum == 0 that means the sum
    # is achieved so print the array
    if (remSum == 0):
        # print1(idx)
        count += 1
        return count
    # i will begin from maxVal which is the
    # maximum value which can be used to form the sum
    i = maxVal
    while (i >= 1):
        if (i > remSum):
            i -= 1
            continue
        else:
            # Store the number used in forming
            # sum gradually in the array
            dp[idx] = i

            # Since i used the rest of partition
            # cant have any number greater than i
            # hence second parameter is i
            solve(remSum - i, i, idx + 1, count)
            i -= 1


if __name__ == "__main__":
    count = 0
    print(solve(40, 40, 1, count))
