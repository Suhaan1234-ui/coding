#include <iostream>
using namespace std;

void inputarr(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << "Enter the " << i << "th element of the array: ";
        cin >> array[i];
    }
}

int oddone(int array[], int size) {
    
    for (int i = 0; i < size; i++) {
        int count = 0;
        for (int j = 0; j < size; j++) {
            if (array[i] == array[j]) {
                count++;
            }
        }
        if (count == 1) {
            return array[i];
        }
    }
    return -1; 
}

int main() {
    int size;
    cout << "Enter size of array: ";
    cin >> size;

    int arr[size];  
    inputarr(arr, size);

    int unique = oddone(arr, size);
    if (unique != -1)
        cout << "Unique element: " << unique << endl;
    else
        cout << "No unique element found." << endl;

    return 0;
}