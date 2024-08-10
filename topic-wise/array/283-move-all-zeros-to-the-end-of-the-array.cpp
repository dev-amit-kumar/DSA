// https://leetcode.com/problems/move-zeroes/
// Link: https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/
#include <iostream>
using namespace std;

void code(int arr[], int n)
{
    int temp[n];
    int k = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 0)
        {
            k++;
            temp[n - k] = arr[i];
        }
        else
            temp[i - k] = arr[i];
    }
    for (int i = 0; i < n; i++)
        cout << temp[i] << " ";
    cout << endl;
}

int main()
{
    int arr[] = {1, 2, 0, 1, 0, 4, 0};
    int n = sizeof(arr) / sizeof(arr[0]);
    code(arr, n);
}