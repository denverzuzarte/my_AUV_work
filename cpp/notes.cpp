//these are used for making understandable notes for cpp 

//pointers are references to memory pointers

#include <iostream>
using namespace std;
//Function arguments by reference used for control over variables using pointers in functions
int addone(int *n)
{
        (*n)++;
	return 0;
}
//linked lists

int main()
{
	int a = 5;
	int *pa =0;	//this sets the pointer pa to the memory adress 0
	pa=&a; 		//this sets the pointer to the memory adress of a
	*pa=*pa+1;
	cout << a << endl;
	addone(pa);	//this calls addone and sends the value of pa 
	cout << a << endl;
}

//structures gay

/*Function arguments by reference used for control over variables using pointers in functions

int addone(int *n)
{
	*n++;
}*/
	
