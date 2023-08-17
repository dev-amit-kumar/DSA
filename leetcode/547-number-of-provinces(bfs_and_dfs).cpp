// https://leetcode.com/problems/number-of-provinces/

#include <iostream>
#include <vector>
using namespace std;

void dfs(int node, vector<vector<int>> &graph, vector<int> &isVisited)
{
    isVisited[node] = 1;
    for (int i = 0; i <= graph.size(); i++)
        if (graph[node][i] && !isVisited[i])
            dfs(i, graph, isVisited);
}

int findCircleNum(vector<vector<int>> &graph)
{
    int len = graph.size();
    int count = 0;
    vector<int> isVisited(len, 0);
    for (int i = 0; i < len; i++)
    {
        if (isVisited[i])
            continue;
        count++;
        dfs(i, graph, isVisited);
    }
    return count;
}

int main()
{
    vector<vector<int>> graph = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    int result = findCircleNum(graph);
    cout << result << endl;
}