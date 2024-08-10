arr = [13, 46, 24, 52, 20, 9]
def bubble_sort(arr):
    steps = 0
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if(arr[j+1] < arr[j]):
                arr[j+1], arr[j] = arr[j], arr[j+1]
                steps += 1
    return steps

print(bubble_sort(arr))