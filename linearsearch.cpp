#include<bits/stdc++.h>
using namespace std;
int n;
int linear(int arr[],int k){
    for(int i=0;i<n;i++){
        if(arr[i]==k){
            return i;
        }
    }
     return -1;
}
int main(){
    int n;
    cin>>n;
    int k;
    cin>>k;
    int arr[k];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int res=linear(arr,k);
    cout<<res;
    return 0;

}