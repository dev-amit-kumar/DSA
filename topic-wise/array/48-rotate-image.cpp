// https://leetcode.com/problems/rotate-image/

#include <iostream>
#include <vector>

using namespace std;

// Complexity Analysis
// Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.
// Space Complexity: O(N*N) to copy it into some other matrix.
vector<vector<int>> rotateBruteForce(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    vector<vector<int>> rotated(n, vector<int>(n, 0));
    for(int i = 0; i < n ; i++){
        for(int j = 0; j < n;j++){
            rotated[j][n-i-1] = matrix[i][j];
        }
    }
    return rotated;
}

void rotateOptimal(vector<vector<int>> &matrix)
{
    int n = matrix.size();
    for(int i = 0; i < n ; i++){
        for(int j = 0; j < i;j++){
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    for (int i = 0; i < n; i++)
    {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}

int main()
{
    vector<vector<int>> matrix = { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } };
    vector<vector<int>> result = rotateBruteForce(matrix);
    int n = matrix.size();
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }
    cout << "\n";

    rotateOptimal(matrix);
    for (int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << matrix[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}