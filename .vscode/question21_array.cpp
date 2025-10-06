#include <iostream>
using namespace std;

bool isPowerOfTwo(long long n) {
  
    if (n <= 0) return false;

    int count = 0;
    while (n != 0) {
        if (n & 1) count++;
        n = n >> 1;
    }
    return count == 1;
}

int main() {
    long long n;
    cin >> n;
    cout << isPowerOfTwo(n);
    return 0;
}