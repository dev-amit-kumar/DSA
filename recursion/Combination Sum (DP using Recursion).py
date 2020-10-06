def combination_sum(all_item, idx, res, total):
    if(total == 0):
        print(res)
        return
    if(total <0):
        return
    if(idx == len(all_item)):
        return

    res.append(all_item[idx])
    total -= all_item[idx]
    combination_sum(all_item, idx, res, total)

    total += all_item[idx]
    res.pop()
    combination_sum(all_item, idx+1, res, total)

if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        n = int(input())
        all_item = list(map(int, input().split()))
        total = int(input())
        print("------------------------")
        if(len(all_item) == n):
            combination_sum(all_item, 0, [], total)