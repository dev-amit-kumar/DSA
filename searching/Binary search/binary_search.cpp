#include <iostream>
using namespace std;

int binary_search(int arr[], int len, int search_no)
{
    int start = 0;
    int end = len - 1;
    int mid = (start + end) / 2;
    while (start <= end)
    {
        if (arr[mid] == search_no)
            return mid;
        else if (arr[mid] > search_no)
            end = mid - 1;
        else if (arr[mid] < search_no)
            start = mid + 1;
        mid = (start + end) / 2;
    }
    return -1;
}

int main()
{
    int arr[13] = {10, 12, 15, 17, 19, 22, 25, 32, 34, 36, 39, 41, 50};
    int search_no = 19;
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = binary_search(arr, n, search_no);
    cout << "result -> " << (result == -1 ? "not found" : to_string(result + 1)) << endl;
}