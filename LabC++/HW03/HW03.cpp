#include <iostream>
#include "term.cpp"
using namespace std;
class Polynomial{
public:
    Poly_node* head;
    Polynomial(){
        head = NULL;
    }
    void addTerm(int coef, int exponent){
        Poly_node *newPtr = new Poly_node;
        newPtr->coef = coef;
        newPtr->exponent = exponent;
        //newPtr->next = NULL;
        Poly_node* curr = head;

        if (head == NULL){
            head = newPtr;
        }else{   
            if(curr->exponent == newPtr->exponent){   
                curr->coef += newPtr->coef;        
            } else if (curr->exponent < newPtr->exponent) {
                newPtr->next = curr;
                curr = newPtr;                          
             }else{  
                while (curr->next != NULL && curr->next->exponent > newPtr->exponent)
                {
                    curr = curr->next;
                    if (curr->next->exponent == newPtr->exponent){
                        curr->next->coef += newPtr->coef;
                    }else{
                        newPtr->next = curr->next;
                        curr->next = newPtr;
                    }
                }    
            }
        }    
    }
    
    void printPolynomial(){
        cout<<"[ ";
        Poly_node* ptr = head;
        while(ptr!=NULL){
            if(ptr->coef==0){

            }else{
                cout<< ptr->coef<<"X^{"<<ptr->exponent<<"} ";
            }
            ptr = ptr->next;
        }
        cout<<"]\n";
    }
    void plus(Polynomial f2){
        /*
         WRITE YOUR CODE HERE
         */
    }
    void minus(Polynomial f2){
        /*
         WRITE YOUR CODE HERE
         */
    }
};



