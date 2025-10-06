#include <iostream>
using namespace std;

void addressarr(int array[], int size) {
    int *ptr=array;
    for(int j = 0; j < size; j++) {
        cout<<ptr;
        cout<<*(ptr);
        ptr =ptr +1;
        
        
       
    }
}

void inputarr(int array[], int size) {
    for(int i = 0; i < size; i++) {
        cin >> array[i];
    }
}

int main() {
    cout << "Enter the size of the array: ";
    int n;
    cin >> n;

    int arr[n]; // Variable Length Array (VLA) - OK in some compilers like GCC, but not standard in C++

    inputarr(arr, n);
    addressarr(arr, n);

    return 0;
}