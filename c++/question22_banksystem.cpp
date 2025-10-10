#include <iostream>
#include <string>

using namespace std;

class banksystem {
    static int totalmember;
    static int totalbalance;
    float balance;
    string name;
    string password;

public:
    banksystem(string n, string p, float balance) {
        name = n;
        password = p;
        this->balance = balance;
        totalmember++;
        totalbalance += balance;
    }

    void deposit(float amount) {
        balance += amount;
        totalbalance += amount;
        cout << "Balance updated: " << balance << endl;
    }

    void withdraw(float amount) {
        if (amount > balance) {
            cout << "Your account does not have the required amount" << endl;
            return;
        } else {
            balance -= amount;
            totalbalance -= amount;
            cout << "Balance updated: " << balance << endl;
        }
    }

    static void show() {
        cout << "Total members: " << totalmember << endl;
        cout << "Total balance: " << totalbalance << endl;
    }

    void showdetails() {
        cout << "Balance: " << balance << endl;
    }

    ~banksystem() {
        cout << "Thank you " << name << endl;
    }
};

int banksystem::totalmember = 0;
int banksystem::totalbalance = 0;

int main() {
    banksystem c1("suhaan", "1234", 4000);
    c1.withdraw(500);
    c1.showdetails();
    banksystem::show();
    return 0;
}