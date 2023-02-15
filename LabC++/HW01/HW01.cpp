#include <iostream>
#include <string>
#include "card.cpp"

using namespace std;

class CardList{

public:
	Card* head;
    int size = 0;
    CardList(){
        head = NULL;
    }

	void pop_back(){
        Card *cur;
        Card *pre = head;

        if (size == 1){
            size--;
            cur = head;
            head = head->next;
            delete cur;
            cur = NULL;
        } else if (size > 1){
            size--;
            while (pre->next->next != NULL){
                pre = pre -> next;
            }
            cur = pre->next;
            pre->next = NULL;
            delete cur;
            cur = NULL;
        }

	}

    void insert_back(string newItem){
        size ++;
        Card *newcard = new Card;
        Card *cur = head;
        newcard->name = newItem;
        newcard->next = NULL;
        
        if (size ==1){
            head = newcard;
        } else {
            while (cur->next != NULL){
                cur = cur -> next;
            }
            cur->next = newcard;
        }
    }

    void shuffle(int pos){
        Card *cur;
        Card *pre = head;
        Card *first = head;
        Card *Last = head;

      
        if (pos >= 1 && size - 1 >= pos){
           
            int i = 0;
            while (Last->next != NULL){
                Last = Last->next; 
                if (size - 1 == pos){
                    if (i < size - 3){                    
                        pre = pre->next;
                        i++;
                    }
                } else if (i < pos-1){
                    pre = pre->next;
                }
                
                i++;
            }
            
            if (size == 2){
                head = Last;
                head->next = first;
                head->next->next = NULL;
            } else if (size - 1 == pos) {   
               
                head = Last;
                cur = Last;
                cur->next = first;
                if (pos >= 4) { 
                    pre = pre->next;
                    for ( i = 0; i < pos-4; i++);
                    {
                        pre = pre->next;
                    }
                    pre->next = NULL;
                    
                } else {
                    pre->next->next = NULL;
                }
                
            } else {
                cur = pre->next;
                head = cur;
                pre->next = NULL;
                Last->next = first;
            } 
        }

    }
    
    void printCardList(){
        /*
         DO NOT DELETE OR EDIT
         */
        cout << "[ ";
        Card* ptr = head;
        while(ptr!=NULL){
            cout << ptr->name << " ";
            ptr = ptr->next;
        }
        cout << "]\n";
    }
};
