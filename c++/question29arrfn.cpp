#include<iostream>
using namespace std;
int main(){
        int arr[1000];
  cout<<"enter the size of the array";
    int size;
    cin>>size;
    for(int i=0; i<size; i++){
        cin>>arr[i];
    }   
   
   for(int i=0; i<size; i++){
     int count=0;
      for(int j=0 ;j<size ; j++){
        if(arr[i]==arr[j] && i!=j){
            count++;
        }
    }
    if(count==0)
        cout<<arr[i]<<" ";
}
}
       