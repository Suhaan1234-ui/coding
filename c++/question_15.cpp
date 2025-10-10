#include <iostream>
using namespace std;
int main(){
    int size;
    cin>>size;
    int arr[size];
    for(int i=0;i<size; i++){
        cin>>arr[i];
    }
    int a;
    if(size%2==0)
       int a=size;
    else
        int a=(size-1);
    for(int j=0; j<a; j++){
        arr[j]=arr[j+1];
        cout<<arr[j];
        j+=1;
    }
    return 0;
}