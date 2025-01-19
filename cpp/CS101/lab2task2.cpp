#include <simplecpp>
int main()
{ 
    int score;
    cout << "enter score here ";
    cin >> score;
    if (score>=90)
    {
        cout << "A";
    }
    else if (score>=80 && score<90)
    {
        cout << "B";
    }
    else if (score>=70 && score<80)
    {
        cout << "C";
    }
    else if (score>=60 && score<70)
    {
        cout << "D";
    }
    else if (score>=50 && score<60)
    {
        cout << "E";
    }
    else if (score<50 && score>=0)
    {
        cout << "F \n";
    }
    else  
        cout << "why would you do this to me \n";
        cout << "you were out of bounds";
}
