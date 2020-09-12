def binary_search(elements,search_no):
    start = 0
    end = len(elements)-1
    mid = (start+end)//2
    found = -1
    while(start <= end):
        if(elements[mid] == search_no):
            found = 1
            break
        elif(elements[mid] < search_no):
            start = mid + 1
            mid = (start+end)//2
        elif(elements[mid] > search_no):
            end = mid-1
            mid = (start+end)//2
    return found

if __name__ == "__main__":
    testcase = int(input())
    result = []
    for i in range(0,testcase):
        no = int(input())
        search = int(input())
        elements = list(map(int,input().split()))
        result.append(binary_search(elements, search_no))
    for i in result:
        print(i)