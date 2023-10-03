// https://leetcode.com/problems/set-matrix-zeroes/

// Step1: Take a note of row an col with 0's in the first loop
// Step2: Now update the values of indexes to 0 where rows and cols are 1

using namespace std;
class Solution
{
public:
    void zeroMatrix(vector<vector<int>> &matrix, int n, int m)
    {
        vector<int> row(n);
        vector<int> col(m);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (matrix[i][j] == 0)
                {
                    row[i] = 1;
                    col[j] = 1;
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (row[i] || col[j])
                {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    void setZeroes(vector<vector<int>> &matrix)
    {
        int row = matrix.size();
        int col = matrix[0].size();

        zeroMatrix(matrix, row, col);
    }
};