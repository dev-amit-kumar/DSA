# def fib(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return (fib(n-1) + fib(n-2))


# if __name__ == "__main__":
#     series = int(input())
#     for i in range(series):
#         print(fib(i), end=" ")


# sum of array


def sum_arr(arr, sum, size):
    if size == 0:
        return sum
    return sum_arr(arr, sum + arr[size-1], size-1)


if __name__ == "__main__":
    arr = [2, 3, 5, 2, 3, 5, 4]
    print(sum_arr(arr, 0, len(arr)))
