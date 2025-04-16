#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class solution {
    public:
    vector<int>BFS(vector<vector<int>>adj){
       int v=adj.size();
       int vis[v]={0};
       vis[0]=1;
       queue<int>q;
       vector<int>res;
       q.push(0);
       while(!q.empty()){
            int node=q.front();
            q.pop();
            res.push_back(node);
            for(auto it : adj[node]){
                if(!vis[it]){
                    vis[it]=1;
                    q.push(it);
                }
            }
        }
       return res;
    }
    void addEdge(vector<int> adj[], int u, int v){
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    void printans(vector<int>&ans){
        for(int i=0;i<ans.size();i++){
            cout<<ans[i]<<" ";
        }
    }

};
int main(){
    vector<int>adj[6];
    

}