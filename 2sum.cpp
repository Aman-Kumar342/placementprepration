#include<bits/stdc++.h>
using namespace std;
int n;
bool found(int arr[], int k){
    for(int i=0;i<n;i++){
        if(arr[i]==k){
            return true;
        }
    }
    return false;
}
bool twosum(int arr[],int k){
    for(int i=0;i<n;i++){
        int num=arr[i];
        for(int j=0;j<n;j++){
            if(found(arr,(k-num))){
                return true;
            }
        }
    }
    return false;

}
int main(){
    int n;
    cin>>n;
    int k;
    cin>>k;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    if(twosum(arr,k)){
        cout<<"the two sum exit in the array ";
    }
    else{
        cout<<"The two not exist in the array ";
    }
    return 0;

}