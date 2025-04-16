#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node *left, *right;
    Node(int val) {
        this->data = val;
        this->left = NULL;
        this->right = NULL;
    }
};

Node* BuildTree() {
    int data;
    cout << "Enter the data ";
    cin >> data;
    
    if (data == -1) return NULL;
    
    Node* root = new Node(data);
    cout << "Enter data for left child of " << data << endl;
    root->left = BuildTree();
    
    cout << "Enter data for right child of " << data << endl;
    root->right = BuildTree();
    
    return root;
}

bool isleaf(Node* root) {
    return (root && !root->left && !root->right);
}

void addleft(Node* root, vector<int>& res) {
    Node* temp = root->left;
    while (temp) {
        if (!isleaf(temp)) res.push_back(temp->data);
        if (temp->left) temp = temp->left;
        else temp = temp->right;
    }
}

void addright(Node* root, vector<int>& res) {
    Node* temp = root->right;
    vector<int> tempres;
    while (temp) {
        if (!isleaf(temp)) tempres.push_back(temp->data);
        if (temp->right) temp = temp->right;
        else temp = temp->left;
    }
    for (int i = tempres.size() - 1; i >= 0; --i) {
        res.push_back(tempres[i]);
    }
}

void addleaf(Node* root, vector<int>& res) {
    if (!root) return;
    if (isleaf(root)) {
        res.push_back(root->data);
        return;
    }
    addleaf(root->left, res);
    addleaf(root->right, res);
}

vector<int> boundarytraversal(Node* root) {
    vector<int> res;
    if (!root) return res;
    
    if (!isleaf(root)) res.push_back(root->data);
    
    addleft(root, res);
    addleaf(root, res);
    addright(root, res);
    
    return res;
}

void printres(vector<int>& res) {
    for (int val : res) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    Node* root = BuildTree();
    vector<int> res = boundarytraversal(root);
    cout << "Boundary Traversal: ";
    printres(res);
    return 0;
}
