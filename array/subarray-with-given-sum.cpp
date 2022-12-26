#include <iostream>
using namespace std;

void bruteForce(int arr[], int n, int k)
{
    int start = 0;
    int end = -1;
    int sum = 0;
    while (start < n)
    {
        while (end + 1 < n && (sum + arr[end + 1] <= k))
            sum += arr[++end];
        if (sum == k)
            cout << start << " " << end << endl;
        sum -= arr[start];
        start++;
    }
}

int main()
{
    int arr[] = {1, 3, 7, 9};
    int size = sizeof(arr) / sizeof(arr[0]);
    bruteForce(arr, size, 10);
}