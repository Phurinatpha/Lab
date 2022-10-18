#include<iostream>
using namespace std;
class Router
{

	int capacity; // maximum possible size of min heap
	int heap_size; // Current number of elements in min heap
public:
    int *data; // pointer to array of elements in heap
	Router(int cap){
        heap_size = 0;
        capacity = cap;
        data = new int[cap];
    }
	int parent(int i) { return (i-1)/2; }
	int left(int i) { return (2*i + 1); }
	int right(int i) { return (2*i + 2); }
	int removeMin(){
        if (heap_size <= 0){
            return 0;
        } if (heap_size == 1){
            heap_size--;
            return data[0];
        }

        int root = data[0];
        data[0] = data[heap_size - 1];
        heap_size--;
        downHeap(0);
        return root;
    }

	int min() {
        if (heap_size == 0){
            return 0;
        }
        return data[0];
	}

	void insert(int k){
        if (heap_size == capacity){
            return;
        }
        heap_size++;
        int i = heap_size - 1;
        data[i] = k;
        while (i != 0 && data[parent(i)] > data[i]){
            swap(data[i], data[parent(i)]);
            i = parent(i);
        }
    }

	void downHeap(int i){
        int left_n = left(i);
        int right_n = right(i);
        int smallest = i;
        if (left_n < heap_size && data[left_n] < data[i])
        {
            smallest = left_n;
        }
        if (right_n < heap_size && data[right_n] < data[smallest])
        {
            smallest = right_n;
        }
        if (smallest != i)
        {
            swap(data[i], data[smallest]);
            downHeap(smallest);
        }
    }

	void reset(int k){
        if (heap_size >= 1){
            data[0] = k;
            downHeap(0);
        }
    }
};

