#include<iostream>
#include<queue>
using namespace std;
struct Node{
    int data;
    Node*left;
    Node*right;
    Node(int val){
        data=val;
        left=NULL;
        right=NULL;
    }
};
Node*buildtree(Node*root){
    cout<<"Enter the data "<<endl;
    int data;
    cin>>data;
    root=new Node(data);
    if(data==-1){
        return NULL;
    }
    cout<<"Inserting data in left of "<<data<<endl;
    root->left=buildtree(root->left);
    cout<<"Inserting data in right of "<<data<<endl;
    root->right=buildtree(root->right);
    return root;
}
int height(Node*root){
    queue<Node*>q;
    q.push(root);
    int level=0;
    while(!q.empty()){
        int size=q.size();
        level++;
        for(int i=0;i<size;i++){
            Node*temp=q.front();
            q.pop();
            if(temp->left!=NULL){
                q.push(temp->left);
            }
            if(temp->right!=NULL){
                q.push(temp->right);
            }
        }

    }
    return level;

}
int main(){
    Node*root=NULL;
    root=buildtree(root);
    cout<<height(root);
    return 0;

}