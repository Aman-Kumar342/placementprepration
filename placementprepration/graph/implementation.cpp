#include<iostream>
using namespace std;

int main(){
    int n;
    cout<<"Enter the number of nodes ";
    cin>>n;
    int m;
    cout<<"enter the number of edge ";
    cin>>m;
    int arr [n+1][n+1];
    for(int i=0;i<m;i++){
        int u , v;
        cin>> u, v;
        arr[u][v]=1;
        arr[v][u]=1;
    }
    return 0;
}