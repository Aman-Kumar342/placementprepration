#include<iostream>
#include<algorithm>
using namespace std;
bool sorted(int arr[],int n){
    for(int i=0;i<n;i++){
        if(arr[i]>arr[i+1]){
            return false;
        }
        else{
            return true;
        }
    }
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    if(sorted(arr,n)){
        cout<<"the array is sorted";
    }
    else{
        cout<<"the array is not sorted";
    }
    return 0;
}