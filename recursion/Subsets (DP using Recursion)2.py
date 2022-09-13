def sub_set(a, idx, res):
    if ((idx == len(a))):
        # if (len(res) == 0):
        #     print("(", end="")
        #     print(end=")")
        # else:
        #     for j in range(0, len(res)):
        #         if (len(res) == 1):
        #             print("(", end="")
        #             print(res[j], end="")
        #             print(end=")")
        #         elif (j == 0):
        #             print("(", end="")
        #             print(res[j], end=" ")
        #         elif (j == (len(res)-1)):
        #             print(res[j], end=")")
        #         else:
        #             print(res[j], end=" ")
        print(res)
        return
    res.append(a[idx])
    sub_set(a, idx+1, res)
    res.pop()
    sub_set(a, idx+1, res)


if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        n = int(input())
        all = list(map(int, input().split()))
        if (len(all) == n):
            res = []
            sub_set(all, 0, res)
