// https://leetcode.com/problems/snakes-and-ladders/

// board =
//     [      0   1   2   3   4   5
//     0   [ -1, -1, -1, -1, -1, -1 ],
//     1   [ -1, -1, -1, -1, -1, -1 ],
//     2   [ -1, -1, -1, -1, -1, -1 ],
//     3   [ -1, 35, -1, -1, 13, -1 ],
//     4   [ -1, -1, -1, -1, -1, -1 ],
//     5   [ -1, 15, -1, -1, -1, -1 ]
//     ];
#include <iostream>
#include <vector>

using namespace std;

int finalAns = INT_MAX;
vector<int> visited;
void dfs(vector<vector<int>> &board, int &currPos, int &maxItems, int &currAns)
{
    if (currPos > maxItems)
        return;
    cout << "currPos " << currPos << endl;
    if (currPos == maxItems)
    {
        cout << "here" << finalAns << " " << currAns << endl;
        finalAns = min(finalAns, currAns);
        return;
    }
    int row = board.size();
    int col = board[0].size();
    int i = (currPos - 1) / row;
    int j = (currPos - 1) % col;
    if (i % 2)
        j = row - 1 - i;
    cout << "currPos:" << currPos
         << " i:"
         << i << " j:" << j << " currAns:" << currAns << endl;
    if (i < 0 and j < 0)
        return;
    if (board[i][j] != -1)
        currPos = board[i][j];
    for (int m = 1; m < 7; m++)
    {
        int newCurr = currPos + m;
        if (find(visited.begin(), visited.end(), newCurr) != visited.end())
        {
            cout << newCurr << "found" << endl;
            continue;
        }
        visited.push_back(newCurr);
        int newAns = currAns + 1;
        dfs(board, newCurr, maxItems, newAns);
    }
}
int snakesAndLadders(vector<vector<int>> &board)
{
    int row = board.size();
    int col = board[0].size();
    int maxItems = row * col;
    cout << row << " " << col << " " << maxItems << endl;
    int currPos = 1;
    int currAns = 1;
    reverse(board.begin(), board.end());
    dfs(board, currPos, maxItems, currAns);
    return finalAns;
}

int main()
{
    vector<vector<int>> board = {{-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1}, {-1, 35, -1, -1, 13, -1}, {-1, -1, -1, -1, -1, -1}, {-1, 15, -1, -1, -1, -1}};
    int result = snakesAndLadders(board);
    cout << result << endl;
}