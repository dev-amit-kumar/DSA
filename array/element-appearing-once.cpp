// Link: https://practice.geeksforgeeks.org/problems/element-appearing-once2552/0

#include <iostream>
using namespace std;

int sol(int arr[], int n)
{
    int h = n - 1;
    int l = 0;
    int mid;
    while (l != h)
    {
        mid = (l + h) / 2;
        cout << l << " " << mid << " " << h << endl;
        if (mid % 2 == 0)
        {
            if (arr[mid] == arr[mid + 1])
                l = mid + 2;
            else
                h = mid;
        }
        else
        {
            if (arr[mid] == arr[mid - 1])
                l = mid + 1;
            else
                h = mid - 1;
        }
        cout << l << " " << mid << " " << h << endl
             << endl;
        ;
    }
    return arr[l];
}

int main()
{
    int arr[] = {1, 1, 2, 2, 4, 4, 5, 6, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = sol(arr, n);
    cout << result << endl;
}