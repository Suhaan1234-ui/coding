#include <iostream>
using namespace std;

void inputarr(int arr[][1000], int rows, int col) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < col; j++) {
            cin >> arr[i][j]; // row-wise input
        }
        /*for(int j=0; j<col; j++){
        for(int i=0; i<rows ; j++){
            cin>>arr[j][i];
            column wise input*/
    }
}

int linearsearch(int arr[][1000], int rows, int col, int target) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < col; j++) {
            if (arr[i][j] == target) {
                return 1; 
            }
        }
    }
    return 0; 
}

int main() {
    int arr[3][1000];  
    int rows = 3, col = 4;

    cout << "Enter elements (" << rows << "x" << col << "):\n";
    inputarr(arr, rows, col);

    cout << "Enter the number you want to find: ";
    int target;
    cin >> target;

    if (linearsearch(arr, rows, col, target))
        cout << target << " found in the array.\n";
    else
        cout << target << " not found in the array.\n";

    return 0;
}

