#include <iostream>
#include <string>
#include "station.cpp"
using namespace std;

class Trip {

public:
     int size = 0;
     Station* header = new Station;
     Station* trailer = new Station;
     Trip()
     {
        header -> next = trailer;
        header -> prev = NULL;
        trailer -> next = NULL;
        trailer -> prev = header;
     }

     void printList()
     {
          cout << "[ ";
          Station* ptr = header->next;
          while (ptr != trailer) {
               cout << ptr->name << " ";
               ptr = ptr->next;
          }
          cout << "]\n";
     }


     void insert_front(string newItem)
     {
          size ++;
          Station *nsta = new Station;
          nsta -> name = newItem;
          

          nsta->prev = header;
          nsta->next = header->next;

          header->next = nsta;
          header->next->prev =nsta;
     }
     void insert_back(string newItem)
     {
          /*
          WRITE YOUR CODE HERE
          */
     }

     void remove_front()
     {
          /*
          WRITE YOUR CODE HERE
          */
     }
     void remove_back()
     {
          /*
          WRITE YOUR CODE HERE
          */
     }

     Station* visit(int nStep, string stepText)
     {
          /*
          WRITE YOUR CODE HERE
          */
         return 0;
     }
};