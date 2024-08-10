elements = [10, 12, 15, 17, 19, 22, 25, 32, 34, 36, 39, 41, 50]
search_no = int(input("Enter the no you want to search: "))
start = 0
end = len(elements)
mid = (start+end)//2
found = False
while (start <= end):
    if (elements[mid] == search_no):
        found = True
        break
    elif (elements[mid] < search_no):
        start = mid + 1
        mid = (start+end)//2
    elif (elements[mid] > search_no):
        end = mid-1
        mid = (start+end)//2
print(found)
