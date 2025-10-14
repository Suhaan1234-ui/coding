#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void reverseWordsInASentence(string s) {
    int start = 0;

    for (int i = 0; i <= s.length(); i++) {
        if (s[i] == ' ' || i == s.length()) {
            int end = i - 1;

            // Reverse the word from 'start' to 'end'
            while (start < end) {
                swap(s[start], s[end]);
                start++;
                end--;
            }

            // Move to the start of the next word
            start = i + 1;
        }
    }

    cout << "Reversed words: " << s << endl;
}


