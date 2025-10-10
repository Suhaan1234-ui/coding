#include <iostream>
using namespace std;
long long sum(int array[], int size){
    int sum =0;
    for(int j=0; j<size; j++){
        sum = sum + array[j];
    }
    return sum;
}
int main(){
   unsigned int n;
   cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cout<<"enter the "<<i<< "th number of the sum you need";
        cin>>arr[i];
        
    }
    cout<<sum(arr , n);
    return 0;
    
    
}