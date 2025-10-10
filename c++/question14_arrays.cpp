

#include <iostream>

using namespace std;

void inputarray(int name[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << "Enter the " << i << "th number of the array: ";
        cin >> name[i];
    }
}

int main()
{
    cout << "Enter the size: ";
    int a;
    cin >> a;

    int j[a];
    inputarray(j, a);

    int b = j[0];
    for (int i = 1; i < a; i++)
    {
        if (j[i] > b)
        {
            b = j[i];
        }
    }

    cout << "Biggest number in the array is: " << b << endl;

    return 0;
}