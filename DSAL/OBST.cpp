#include<iostream>
using namespace std;
#define MAX 10

int find(int, int);
void print(int, int);

int p[MAX], q[MAX], w[10][10], c[10][10], r[10][10], n;

int main() {
    cout << "Enter the number of identifiers: ";
    cin >> n;

    cout << "Enter identifiers: ";
    for (int i = 1; i <= n; i++)
        cin >> p[i];

    cout << "Enter search probabilities for identifiers: ";
    for (int i = 1; i <= n; i++)
        cin >> q[i];

    cout << "\nWeight    Cost    Root\n";

    for (int i = 0; i <= n; i++) {
        w[i][i] = q[i];
        c[i][i] = r[i][i] = 0;
        cout << w[i][i] << "    " << c[i][i] << "    " << r[i][i] << endl;
    }

    for (int i = 0; i < n; i++) {
        int j = i + 1;
        w[i][j] = p[j] + q[j] + q[i];
        c[i][j] = w[i][j];
        r[i][j] = j;
        cout << w[i][j] << "    " << c[i][j] << "    " << r[i][j] << endl;
    }

    for (int m = 2; m <= n; m++) {
        for (int i = 0; i <= n - m; i++) {
            int j = i + m;
            w[i][j] = w[i][j - 1] + p[j] + q[j];
            c[i][j] = INT_MAX;

            for (int k = i + 1; k <= j; k++) {
                int cost = c[i][k - 1] + c[k][j];
                if (cost < c[i][j]) {
                    c[i][j] = cost;
                    r[i][j] = k;
                }
            }

            c[i][j] += w[i][j];
            cout << w[i][j] << "    " << c[i][j] << "    " << r[i][j] << endl;
        }
    }

    cout << "\nTHE FINAL OBST IS:\n";
    print(0, n);

    return 0;
}

int find(int i, int j) {
    int minCost = INT_MAX;
    int minIndex = -1;

    for (int k = i + 1; k <= j; k++) {
        int cost = c[i][k - 1] + c[k][j];
        if (cost < minCost) {
            minCost = cost;
            minIndex = k;
        }
    }

    return minIndex;
}

void print(int i, int j) {
    if (i < j) {
        cout << "Identifier: " << r[i][j] << endl;
        print(i, r[i][j] - 1);
        print(r[i][j], j);
    }
}
