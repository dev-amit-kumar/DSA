def binary_search(all_item, search_no, start, end):
    mid = (start+end)//2
    if(start > end):
        return False
    elif(all_item[mid] == search_no):
        return True
    elif(all_item[mid] < search_no):
        return binary_search(all_item, search_no, mid + 1, end)
    elif(all_item[mid] > search_no):
        return binary_search(all_item, search_no, start, mid-1)

if __name__ == "__main__":
    search = int(input())
    all_item = list(map(int,input().split()))
    print(binary_search(all_item, search, 0, len(all_item)-1))