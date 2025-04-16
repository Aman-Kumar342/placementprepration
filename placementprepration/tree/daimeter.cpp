#include<iostream>
using namespace std;
struct Node{
    int data;
    struct Node*right;
    struct Node*left;
    Node(int val){
        this->data=val;
        this->left=NULL;
        this->right=NULL;
    }
};
Node*BuildTree(Node*root){
    int data;
    cout<<"Enetr the data "<<endl;
    cin>>data;
    root=new Node(data);
    if(root==NULL){
        return ;
    }
    cout<<"Enter the data in left of "<<data<<endl;
    root->left=BuildTree(root->left);
    cout<<"enetr the data in right of "<<data<<endl;
    root->right=BuildTree(root->right);
    return root;
}
int daimeter(Node*root){
    
}
int main(){
    Node*root=NULL;
    root=BuildTree(root);


    return 0;

}