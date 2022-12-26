#include <iostream>
using namespace std;

// kadane's algorithm
int maxSubArraySum(int arr[], int n)
{
    int currMax = 0;
    int maxSoFar = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] < currMax + arr[i])
            currMax += arr[i];
        else
            currMax = arr[i];
        if (currMax > maxSoFar)
            maxSoFar = currMax;
    }
    return maxSoFar;
}

int main()
{
    int arr[] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int size = sizeof(arr) / sizeof(arr[0]);
    int result = maxSubArraySum(arr, size);
    cout << result << endl;
}