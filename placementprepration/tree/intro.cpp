#include<iostream>
#include<queue>
using namespace std;
struct Node{
    int data;
    struct Node*left;
    struct Node*right;
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
void levelordertraversal(Node*root){
    queue<Node*>q;
    q.push(root);
    while(!q.empty()){
        Node*temp=q.front();
        cout<<temp->data;
        q.pop();
        if(temp->left!=NULL){
            q.push(temp->left);
        }
        if(temp->right!=NULL){
            q.push(temp->right);
        }

    }

}
void inorder(Node*root){
    if(root==NULL){
        return;
    }
    inorder(root->left);
    cout<<(root->data)<<" ";
    inorder(root->right);
}
void preorder(Node*root){
    if(root==NULL){
        return;
    }
    cout<<root->data<<" ";
    preorder(root->left);
    preorder(root->right);
}
void postorder(Node*root){
    if(root==NULL){
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout<<root->data<<" ";
}

int main(){
    Node*root= NULL;
    root=buildtree(root);
    cout<<"The inorder is "<<endl;
    inorder(root);
    cout<<"the preorder is "<<endl;
    preorder(root);
    cout<<"the post order is "<<endl;
    postorder(root);
    return 0;

}