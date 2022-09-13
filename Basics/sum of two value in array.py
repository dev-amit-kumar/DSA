# Ques https://leetcode.com/problems/two-sum/

# def brute_ans(arr, sum):
#     for i in range(0, len(arr), 1):
#         for j in range(i+1, len(arr), 1):
#             if (arr[i]+arr[j] == sum):
#                 print(arr[i], arr[j])
#                 return


def logn_ans(arr, sum):
    for i in range(0, len(arr), 1):
        for j in range(i+1, len(arr), 1):
            if (arr[i]+arr[j] == sum):
                print(arr[i], arr[j])
                return


# def n_ans(arr, sum):
#     for i in range(0, len(arr), 1):
#         for j in range(i+1, len(arr), 1):
#             if (arr[i]+arr[j] == sum):
#                 print(arr[i], arr[j])
#                 return


if __name__ == "__main__":
    arr = [1, 5, 3, 4, 6, 2]
    sum = 10
    # brute_ans(arr,sum)
    logn_ans(arr, sum)
    # n_ans(arr, sum)
