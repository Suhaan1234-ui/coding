#include <iostream>
#include <algorithm> //to use swap function
using namespace std;

void alternate(int arr[], int size) {
    int i = 0;
    while (i + 1 < size) {
        swap(arr[i], arr[i + 1]);
        i += 2;
    }
    for (int j = 0; j < size; j++)
        cout << arr[j] << endl;
}

int main() {
    int arr[1000];
    int size;
    cout << "Enter the size of the array: ";
    cin >> size;

    cout << "Enter " << size << " elements:" << endl;
    for (int i = 0; i < size; i++) {
        cin >> arr[i];  // Input array elements
    }

    alternate(arr, size);

    return 0;
}
