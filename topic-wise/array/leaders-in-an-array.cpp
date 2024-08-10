// Link: https://takeuforward.org/data-structure/leaders-in-an-array/
#include <iostream>
using namespace std;

void sol(int arr[], int n)
{
    int max = arr[n - 1];
    cout << max << " ";
    for (int i = n - 2; i >= 0; i--)
    {
        if (arr[i] > max)
        {
            max = arr[i];
            cout << max << " ";
        }
    }
    cout << endl;
}

int main()
{
    int arr[] = {10, 22, 12, 3, 0, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    sol(arr, n);
}