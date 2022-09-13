def find_upper_bound(A, search_element):
    start = 0
    end = len(A)-1
    mid = (start + end)//2
    upper_bound_idx = -1
    while (start <= end):
        mid = (start+end)//2
        if (A[mid] == search_element):
            upper_bound_idx = mid
            if (mid+1 <= end and A[mid] == A[mid+1]):
                start = mid + 1
            else:
                break
        elif (A[mid] > search_element):
            end = mid-1
        elif (A[mid] < search_element):
            start = mid + 1
    return upper_bound_idx


def find_lower_bound(A, search_element):
    start = 0
    end = len(A)-1
    mid = (start + end)//2
    lower_bound_idx = -1
    while (start <= end):
        mid = (start+end)//2
        if (A[mid] == search_element):
            lower_bound_idx = mid
            if (mid-1 >= start and A[mid] == A[mid-1]):
                end = mid - 1
            else:
                break
        elif (A[mid] > search_element):
            end = mid-1
        elif (A[mid] < search_element):
            start = mid + 1
    return lower_bound_idx


if __name__ == "__main__":
    testcase = int(input())
    for i in range(testcase):
        n = list(map(int, input().split()))
        A_list = list(map(int, input().split()))
        search_no = n[1]
        upper = find_upper_bound(A_list, search_no)
        lower = find_lower_bound(A_list, search_no)
        if (upper == -1 and lower == -1):
            print("-1")
        else:
            print(lower, upper)
