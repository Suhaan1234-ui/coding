// Topic: Linear search — check whether a given element exists in an array (function-based)
    

#include <iostream>
using namespace std;
int findelement(int arr[], int size, int key){
    for(int i=0; i<size;     
    #include <iostream>
    using namespace std;
    int findelement(int arr[], int size, int key){
        for(int i=0; i<size; i++){
            if(arr[i]==key)
            return 1;
        }
        return 0;
    }
    int main(){
        int arr[1000];
        cout<<"enter the size of the array";
        int size;
        cin>>size;
        for(int i=0; i<size; i++){
            cin>>arr[i];
        }
        cout<<"enter the element you need to find";
        int element;
        cin>>element;
       bool found= findelement(arr,size,element);
        if(found)
           cout<<"your element was found";
        else
          cout<<"element not found";
    }i++){
        if(arr[i]==key)
        return 1;
    }
    return 0;
}
int main(){
    int arr[1000];
    cout<<"enter the size of the array";
    int size;
    cin>>size;
    for(int i=0; i<size; i++){
        cin>>arr[i];
    }
    cout<<"enter the element you need to find";
    int element;
    cin>>element;
   bool found= findelement(arr,size,element);
    if(found)
       cout<<"your element was found";
    else
      cout<<"element not found";
}