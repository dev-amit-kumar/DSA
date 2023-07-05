// https://leetcode.com/problems/search-a-2d-matrix/

#include <iostream>
#include <vector>
using namespace std;

bool searchMatrix(vector<vector<int>> &matrix, int target)
{
    int row = matrix.size();
    int col = matrix[0].size();
    int start = 0;
    int end = (row * col) - 1;
    while (start <= end)
    {
        int mid = (start + end) / 2;
        int val = matrix[mid / col][mid % col];
        if (val == target)
            return true;
        else if (val < target)
            start = mid + 1;
        else
            end = mid - 1;
    }
    return false;
}

int main()
{
    vector<vector<int>> matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};
    int target = 24;
    bool result = searchMatrix(matrix, target);
    cout << "result: " << result;
}