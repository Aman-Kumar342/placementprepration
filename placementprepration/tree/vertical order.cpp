#include<iostream>
#include <map>
#include <queue>
#include <vector>
#include <algorithm>
#include<set>
using namespace std;
struct Node{
    int data;
    Node*left;
    Node*right;
    Node(int val){
        this->data=val;
        this->left=NULL;
        this->right=NULL;
    }
};
Node*BuildTree(Node*root){
    int data;
    cout<<"Enter the value of data";
    cin>>data;
    if(data==-1){
        return NULL;
    }
    Node*root=new Node(data);
    cout<<"Enter the value of data in left of "<<data<<endl;
    root->left=BuildTree(root->left);
    cout<<"Enter the value of data in right of "<<data<<endl;
    root->right=BuildTree(root->right);
    return root;
}
vector<vector<int>>verticalTraversal(Node*root){
    map<int,map<int,multiset<int>>>node;
    queue<pair<Node*,pair<int,int>>>q;
    q.push({root,{0,0}});
    while(!q.empty()){
        auto p=q.front();
        q.pop();
        Node*node=p.first;
        int x=p.second.first,y=p.second.second;
        node[x][y].insert(node->data);
        if(node->left){
            q.push({node->left,{x-1,y+1}});
        }
        if(node->right){
            q.push({node->right,{x+1,y+1}});
        }
    }
    vector<vector<int>>ans;
    for(auto p:node){
        vector<int>col;
        for(auto q:p.second){
            for(auto it:q.second){
                col.push_back(it);
            }
        }
        ans.push_back(col);
    }
    return ans;

}

int main(){
    Node*root=NULL:
    root=BuildTree(root);
    

}