def sub_set(a, idx, res):
    if ((idx == len(a))):
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
