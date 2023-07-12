// https://leetcode.com/problems/surrounded-regions

//      0    1    2    3
// 0 [ "X", "X", "X", "X" ],
// 1 [ "X", "O", "O", "X" ],
// 2 [ "X", "X", "O", "X" ],
// 3 [ "X", "O", "X", "X" ]
class Solution
{
private:
    void dfs(vector<vector<char>> &board, int i, int j, int rows, int cols)
    {
        if (i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O')
            return;
        board[i][j] = '#';
        dfs(board, i, j + 1, rows, cols);
        dfs(board, i, j - 1, rows, cols);
        dfs(board, i + 1, j, rows, cols);
        dfs(board, i - 1, j, rows, cols);
    }

public:
    void solve(vector<vector<char>> &board)
    {
        int rows = board.size();
        int cols = board[0].size();

        // first row and last row
        for (int j = 0; j < cols; j++)
        {
            if (board[0][j] == 'O')
                dfs(board, 0, j, rows, cols);
            if (board[rows - 1][j] == 'O')
                dfs(board, rows - 1, j, rows, cols);
        }

        // first cols and last cols
        for (int i = 0; i < rows; i++)
        {
            if (board[i][0] == 'O')
                dfs(board, i, 0, rows, cols);
            if (board[i][cols - 1] == 'O')
                dfs(board, i, cols - 1, rows, cols);
        }

        for (int i = 0; i < rows; i++)
            for (int j = 0; j < cols; j++)
            {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                if (board[i][j] == '#')
                    board[i][j] = 'O';
            }
    }
};