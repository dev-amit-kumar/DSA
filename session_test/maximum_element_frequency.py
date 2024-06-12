n = 5
a = [5,5,5,5,5,5,5]
def maxElementFrequency(n, a):
    hash_map = {}
    max_num = float("-inf")
    for i in a:
        if(i in hash_map):
            hash_map[i] += 1
        else:
            hash_map[i] = 1
        max_num = max(i, max_num)
    return hash_map[max_num]
print(maxElementFrequency(n, a))