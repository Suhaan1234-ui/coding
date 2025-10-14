#include <iostream>
#include <string>
#include <cctype>  // for isalpha and tolower
using namespace std;

bool removeCharAndLowercaseAlsoCheckPalindrome(string s) {
    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (isalpha(s[i])) {
            temp += tolower(s[i]);
        }
    }
    int start = 0;
    int end = temp.length() - 1;

    while (start < end) {
        if (temp[start] != temp[end]) {
            return false;
        }
        start++;
        end--;
    }

    return true;
}
