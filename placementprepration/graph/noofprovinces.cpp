#include <iostream>
#include <vector>
using namespace std;

void dfs(int node, vector<int> adjls[], vector<int>& vis) {
    vis[node] = 1;
    for (auto it : adjls[node]) {
        if (!vis[it]) {
            dfs(it, adjls, vis);
        }
    }
}
int noofprovinces(vector<vector<int>>& adj) {
    int v = adj.size();
    vector<int> adjls[v];

    for (int i = 0; i < v; i++) {
        for (int j = 0; j < v; j++) {
            if (adj[i][j] == 1 && i != j) {
                adjls[i].push_back(j);
            }
        }
    }

    vector<int> vis(v, 0);
    int ct = 0;
    for (int i = 0; i < v; i++) {
        if (!vis[i]) {
            ct++;
            dfs(i, adjls, vis);
        }
    }
    return ct;
}
int main() {
    vector<vector<int>> adj = {
        {1, 1, 0},
        {1, 1, 0},
        {0, 0, 1}
    };

    cout << "Number of Provinces: " << noofprovinces(adj) << endl;
    return 0;
}
