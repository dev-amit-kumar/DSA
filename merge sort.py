def merge_array(a, s1, e1, s2, e2):
        p1 = s1
        p2 = s2
        temp = list()
        while p1 <= e1 and p2 <= e2:
                if a[p1] < a[p2]:
                        temp.append(a[p1])
                        p1 += 1
                else:
                        temp.append(a[p2])
                        p2 += 1
        while p1 <= e1:
                temp.append(a[p1])
                p1 += 1

        while p2 <= e2:
                temp.append(a[p2])
                p2 += 1

        idx = 0
        while idx < len(temp):
                a[s1 + idx] = temp[idx]
                idx += 1

def mergeSort(a, l, r):
        if l >= r:
                return
        mid = (l + r) // 2
        mergeSort(a, l, mid)
        mergeSort(a, mid + 1, r)
        merge_array(a, l, mid, mid + 1, r)

if __name__ == '__main__':
        l = list(map(int, input().split()))
        mergeSort(l, 0, len(l) - 1)
        print(l)