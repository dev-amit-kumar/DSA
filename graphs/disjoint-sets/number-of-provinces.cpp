// https://leetcode.com/problems/number-of-provinces/

#include <iostream>
#include <vector>
using namespace std;

class DisjointSet
{
public:
    vector<int> parent, size;
    DisjointSet(int n)
    {
        parent.resize(n + 1);
        size.resize(n + 1);
        for (int i = 0; i <= n; i++)
        {
            parent[i] = i;
            size[i] = i;
        }
    }

    int findUPar(int node)
    {
        if (node == parent[node])
            return node;
        return parent[node] = findUPar(parent[node]);
    }

    void unionBySize(int u, int v)
    {
        int ulp_u = findUPar(u);
        int ulp_v = findUPar(v);
        if (ulp_u == ulp_v)
            return;
        if (size[ulp_u] < size[ulp_v])
        {
            parent[ulp_u] = ulp_v;
            size[ulp_v] += size[ulp_u];
        }
        else
        {
            parent[ulp_v] = ulp_u;
            size[ulp_u] += size[ulp_v];
        }
    }
};

int findCircleNum(vector<vector<int>> &isConnected)
{
    int n = isConnected.size();
    DisjointSet dsu(n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            if (isConnected[i][j] == 1)
                dsu.unionBySize(i, j);

    int count = 0;
    for (int i = 0; i < n; i++)
        if (dsu.parent[i] == i)
            count++;
    return count;
}

int main()
{
    vector<vector<int>> isConnected = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
    int result = findCircleNum(isConnected);
    cout << result << endl;
}