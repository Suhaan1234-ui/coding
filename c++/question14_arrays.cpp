#include <iostream>
#include <climits>
using namespace std;

void inputarr(int arr[], int size) {
    for (int i = 0; i < size; i++)
        cin >> arr[i];
}

int max(int arr[], int size) {
    int a = INT_MIN;
    for (int i = 0; i < size; i++) {
        if (arr[i] > a)  
            a = arr[i];
    }
    return a;
}

int min(int arr[], int size) {
    int a = INT_MAX;  
    for (int i = 0; i < size; i++) {
        if (arr[i] < a)
            a = arr[i];
    }
    return a;
}

int main() {
    int arr[10000];
    cout << "Enter the size of the array: ";
    int size;
    cin >> size;

    inputarr(arr, size);

    cout << "The biggest term is: " << max(arr, size) << endl;
    cout << "The smallest term is: " << min(arr, size) << endl;

    return 0;
}
