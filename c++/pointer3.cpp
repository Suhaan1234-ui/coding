#include<iostream>
using namespace std;

int main() {
    //in char entire content is printed

    int arr[5] = {1,2,3,4,5};
    char ch[6] = "abcde";


    cout << arr << endl;
    //attention here
    cout << ch << endl;
    
    char *c = &ch[0];
    //prints entire string
    //initializes from c and stops until null char found are found
     //stops until null character is found both in char arrays and char
    cout << c << endl;

    char temp = 'z';
    //implementation of cout is different with char arrays thats why pointers doesnt work on them
    //keeps going to next memory block and stops until null ch is found
   
    char *p = &temp;

    cout << p << endl;


    return 0;
}
