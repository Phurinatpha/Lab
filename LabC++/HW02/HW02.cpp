#include <iostream>
#include <string>
#include "station.cpp"
using namespace std;

class Trip {

public:
     Station* header = new Station;
     Station* trailer = new Station;
     Trip(){
        header -> next = trailer;
        trailer -> prev = header;
     }

     void printList(){
          cout << "[ ";
          Station* ptr = header->next;
          while (ptr != trailer) {
               cout << ptr->name << " ";
               ptr = ptr->next;
          }
          cout << "]\n";
     }

     void insert_front(string newItem){
          Station *nsta = new Station;
          Station *curr = header->next;
          nsta -> name = newItem;

          nsta->prev = header;
          nsta->next = curr;

          header->next = nsta;
          curr->prev = nsta;
     }

     void insert_back(string newItem){
          Station *nsta = new Station;
          Station *curr = trailer->prev;
          nsta -> name = newItem;

          nsta->next = trailer;
          nsta->prev = curr;

          curr->next = nsta;
          trailer->prev = nsta;
          
     }
     
     void remove_front(){
          Station *curr = header->next;
          curr->next->prev = header;
          header->next = curr->next;
          delete curr;
     }

     void remove_back(){
          Station *curr = trailer->prev; 
          curr->prev->next = trailer;
          trailer->prev = curr->prev;
          delete curr;
     }

     Station* visit(int nStep, string stepText,int i=0){
          Station *curr = header->next;
          while(i < nStep){
               if (stepText[i] == 'R'){
                    if (curr->next != trailer){
                         curr = curr->next;
                    }
               } else if (curr->prev != header){
                    curr = curr->prev;
               }
               i++;
          }
          return curr;
     }
};