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
        Poly_node *n_poly = new Poly_node;
        n_poly->coef = coef;
        n_poly->exponent = exponent;
       
        if (head == NULL){                                  
            head = n_poly;
        }else if(head->exponent <= exponent){ 
            if(head->exponent == exponent){   
                head->coef += coef;                 
            } else if (head->exponent < exponent) {        
                n_poly->next = head;                       
                head = n_poly;
            }
        } else{  
            Poly_node* curr = head;
            while (curr->next != NULL && curr->next->exponent > exponent) 
            {
                curr = curr->next;
            }

            if(curr->next == NULL)
                curr->next = n_poly;
            else{
                if(curr->next->exponent < exponent){
                    n_poly->next = curr->next;
                    curr->next = n_poly;
                } else if (curr->next->exponent == exponent){
                    curr->next->coef += coef;
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
        for (Poly_node *curf2 = f2.head; curf2!=NULL; curf2=curf2->next){
            int n_expo = curf2->exponent;
            int n_coef = curf2->coef;
            addTerm(n_coef, n_expo);
        }
    }

    void minus(Polynomial f2){
        for (Poly_node *curf2 = f2.head; curf2!=NULL; curf2=curf2->next){
            int n_expo = curf2->exponent;
            int n_coef = curf2->coef;
            addTerm((-1)*n_coef, n_expo);
        }
    }
};



