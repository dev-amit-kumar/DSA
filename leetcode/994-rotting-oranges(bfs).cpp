// https://leetcode.com/problems/rotting-oranges

class Solution
{
private:
    void dfs(vector<vector<int>> &grid, int rows, int cols, int i, int j, int minutes)
    {
        if (i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (grid[i][j] > 1 && grid[i][j] < minutes))
            return;
        grid[i][j] = minutes;
        dfs(grid, rows, cols, i, j + 1, minutes + 1);
        dfs(grid, rows, cols, i, j - 1, minutes + 1);
        dfs(grid, rows, cols, i - 1, j, minutes + 1);
        dfs(grid, rows, cols, i + 1, j, minutes + 1);
    }

public:
    int orangesRotting(vector<vector<int>> &grid)
    {
        int rows = grid.size();
        if (rows == 0)
            return -1;
        int cols = grid[0].size();

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == 2)
                {
                    dfs(grid, rows, cols, i, j, 2);
                }
            }
        }
        int minutes = 2;
        for (auto &i : grid)
        {
            for (auto &j : i)
            {
                if (j == 1)
                    return -1;
                minutes = max(minutes, j);
            }
        }
        return minutes - 2;
    }
};