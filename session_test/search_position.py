arr = [1,3,5,6]
target = 2
def search_position(arr, target):
    left = 0
    right = len(arr) - 1
    pos = left
    while(left <= right):
        mid = (left + right) // 2
        if(arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return left

print(search_position(arr, target))