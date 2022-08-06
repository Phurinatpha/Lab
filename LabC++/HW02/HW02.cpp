#include <iostream>
#include <string>
#include "station.cpp"
using namespace std;

class Trip {

public:
     int size = 0;
     Station* header = new Station;
     Station* trailer = new Station;
     Trip(){
        header -> next = trailer;
        header -> prev = NULL;
        trailer -> next = NULL;
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
          size ++;
          Station *nsta = new Station;
          nsta -> name = newItem;

          Station *curr = new Station;
          curr = header->next;

          nsta->prev = header;
          nsta->next = curr;

          header->next = nsta;
          curr->prev = nsta;
     }

     void insert_back(string newItem){
          size ++;
          Station *nsta = new Station;
          nsta -> name = newItem;
          
          Station *curr;
          curr = trailer->prev;

          nsta->next = trailer;
          nsta->prev = curr;

          curr->next = nsta;
          trailer->prev = nsta;
          
     }
     
     void remove_front(){
          Station *curr;
          curr = header->next;

          curr->next->prev = header;
          header->next = curr->next;

          size--;
          delete curr;
     }

     void remove_back(){
          Station *curr ; 
          curr = trailer->prev;

          curr->prev->next = trailer;
          trailer->prev = curr->prev;

          size--;
          delete curr;
     }

     Station* visit(int nStep, string stepText){
          Station *curr;
          curr = header->next;
          for (int i = 0; i < stepText.length(); i++){
               if (stepText[i] == 'R'){
                    if (curr->next != trailer){
                    curr = curr->next;
                    }
               } else {
                    if (curr->prev != header){
                    curr = curr->prev;
                    }
               }
          }
          return curr;
     }
};