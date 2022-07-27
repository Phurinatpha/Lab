#include <iostream>
#include "HW06.cpp"
using namespace std;


int main()
{
    Ranking r(10);
    r.inputData();
	//input your data
    r.mergeSort(0,9);
    cout<<r.binarySearch(7)<<"\n";
    for(int i=1;i<=10;i++)
        cout<<r.show(i);
    return 0;
}
