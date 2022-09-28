#include <iostream>
using namespace std;
class Ranking{
private:
    int data[1000];
    int size;
    /*
         WRITE YOUR CODE HERE
    */
public:
    Ranking(int n){
    /*
         WRITE YOUR CODE HERE
    */
    }
    void inputData(){
        for(int i=0;i<size;i++){
            cin>>data[i];
        }
    }
    int binarySearch(int key){
    /*
         WRITE YOUR CODE HERE
    */
    }
    void merge(int left, int mid, int right){
	/*
         WRITE YOUR CODE HERE
    */
    }
    void mergeSort(int left, int right){
    /*
         WRITE YOUR CODE HERE
    */
	}
    int show(int index){
        return data[index-1];
    }
};

