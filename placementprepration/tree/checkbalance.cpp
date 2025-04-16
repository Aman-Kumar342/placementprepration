#include<iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        this->data = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* BuildTree(Node* root) {
    int data;
    cout << "Enter the data: ";
    cin >> data;

    if (data == -1) {
        return NULL; 
    }

    root = new Node(data);

    cout << "Enter the data in left of " << data << endl;
    root->left = BuildTree(root->left);
    cout << "Enter the data in right of " << data << endl;
    root->right = BuildTree(root->right);

    return root;
}

int height(Node* root, bool &balanced) {
    if (root == NULL) {
        return 0; 
    }

    int lh = height(root->left, balanced);
    int rh = height(root->right, balanced);

    if (abs(lh - rh) > 1) {
        balanced = false;
    }

    return max(lh, rh) + 1;
}

bool isBalanced(Node* root) {
    bool balanced = true;
    height(root, balanced);
    return balanced;
}

int main() {
    Node* root = NULL;
    root = BuildTree(root);

    if (isBalanced(root)) {
        cout << "The tree is balanced." << endl;
    } else {
        cout << "The tree is NOT balanced." << endl;
    }
    return 0;
}
