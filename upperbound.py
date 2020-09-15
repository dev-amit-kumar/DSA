def find_upper_bound(A, search_element):
    start = 0
    end = len(A)-1
    mid = (start + end)//2
    upper_bound_idx = -1
    while(start <= end):
        mid = (start+end)//2
        if(A[mid] == search_element):
            upper_bound_idx = mid
            if(mid+1 <= end and A[mid] == A[mid+1]):
                start = mid + 1
            else:
                break
        elif(A[mid] > search_element):
            upper_bound_idx = mid
            end = mid-1
        elif(A[mid] < search_element):
            start = mid + 1
    print(A[upper_bound_idx])
    return upper_bound_idx

def find_lower_bound(A, search_element):
    start = 0
    end = len(A)-1
    mid = (start + end)//2
    upper_bound_idx = -1
    while(start <= end):
        mid = (start+end)//2
        if(A[mid] == search_element):
            upper_bound_idx = mid
            if(mid-1 >= start and A[mid] == A[mid-1]):
                end = mid - 1
            else:
                break
        elif(A[mid] > search_element):
            end = mid-1
        elif(A[mid] < search_element):
            upper_bound_idx = mid
            start = mid + 1
    print(A[upper_bound_idx])        
    return upper_bound_idx

if __name__ == "__main__":
    A_list = [1,1,1,2,2,2,2,4,5,6]
    search_no = 2
    print("Upper Bound Value idx is = ", find_upper_bound(A_list, search_no))
    print("Lower Bound Value idx is = ", find_lower_bound(A_list, search_no))