#include <iostream>
#include <climits>
using namespace std;

void inputarr(int arr[][1000], int row, int col) {
    cout << "Enter the elements of the array:\n";
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> arr[i][j];
        }
    }
}

void rowisesum(int arr[][1000], int row, int col) {
    int maxSum = INT_MIN;
int index;
    for (int i = 0; i < row; i++) {
        int sum = 0; 
        for (int j = 0; j < col; j++) {
            sum += arr[i][j];
        }
        cout << "Row " << i << " sum = " << sum << endl;

        if (sum > maxSum) {
            maxSum = sum;
            index = i;
        }
    }

    cout << "The largest row-wise sum is " << maxSum 
         << " (at row " << rowIndex << ")" << endl;
}

int main() {
    int row, col;
    cout << "Enter the size of the array (rows and columns): ";
    cin >> row >> col;

    int arr[1000][1000]; 

    inputarr(arr, row, col);
    rowisesum(arr, row, col);

    return 0;
}
