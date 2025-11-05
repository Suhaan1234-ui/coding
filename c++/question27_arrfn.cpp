
#include <iostream>
#include<algorithm>
using namespace std;
void reversearray(int arr[], int size){
    int start =0;
   int end = size-1;
    while(start<end){
        swap(arr[start],arr[end]);
        start++;
        end--;
    }
    for(int i=0; i<size; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
int main(){
  int arr[1000];
  cout<<"enter the size of the array";
    int size;
    cin>>size;
    for(int i=0; i<size; i++){
        cin>>arr[i];
    }   
     reversearray(arr,size);
}
