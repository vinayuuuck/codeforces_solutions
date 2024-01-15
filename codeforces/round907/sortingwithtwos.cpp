
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){

    int testcases;

    cin >> testcases;

    for(int i = 0; i < testcases; ++i){
        int n;
        cin >> n;
        vector<int> v;
        for(int j = 0; j < n; ++j){
            int temp;
            cin >> temp;
            v.push_back(temp);
        }

        int m = 0;
        bool yesflag = true;

        for(int j = 1; j < n; ++j){
            if(v[j] < v[j-1]){
                if (j == pow(2, m)){
                    m++;
                }
                else{
                    cout << "NO" << endl;
                    yesflag = false;
                    break;
                }
            }

            if (j == pow(2, m)){
                m++;
            }
        }

        if(yesflag){
            cout << "YES" << endl;
        }
    }
}