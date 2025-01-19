#include <simplecpp>
int main()
{
    double kilos;
    cout << "";
    cin >> kilos;
    double pounds = 2.2*kilos;
    string str=to_string(kilos) + " Kg = " + to_string(pounds) + " lbs";
    cout << str;
}
