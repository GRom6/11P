#include <iostream>
using namespace std;

bool f(short s, short count, short count_max){

    if (s>=37)
         return (((count-1)%2) == (count_max%2));

    if ((count-1) >= count_max)
        return false;

    else{
        if ((count%2) == (count_max%2))
          return((f(s+1, count+1, count_max)) || (f(s+2, count+1, count_max)) || (f(s*3, count+1, count_max)));
        else
           return (f(s+1, count+1, count_max) && f(s+2, count+1, count_max) && f(s*3, count+1, count_max));
    }
}

int main(){

    short s19 = 1000, s120 = 1000, s220 = 1000, s21 = 1000;

    for (short i = 1; i<36; i++) {

        if (f(i, 1, 2) && s19>i){
            s19 = i;
        }

        if (f(i, 1, 3) && !(f(i, 1, 1))){
            if (i<s120){
                s120 = i;
            }
            else if (i < s220){
                s220 = i;
            }
        }

        if ((f(i, 1, 4)) && !(f(i, 1, 2))){
            cout<<1<<endl;
            s21 = i;
        }
    }

    cout << s19 << ", " << s120<<", "<<s220<<", " << s21<< endl;
    return 0;
}
