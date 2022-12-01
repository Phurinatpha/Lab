#include "BSTNode.cpp"
#include <iostream>
// ศึกษาจาก https://www.youtube.com/watch?v=twXZzk3Np-A&ab_channel=NoobCoder

class BST {

    public:
        BSTNode* root;

    BST() {
        root = NULL;
    }

    void insert(int value) {
        BSTNode *p = new BSTNode;
        BSTNode *prev = new BSTNode;
        BSTNode *newNode = new BSTNode;

        newNode->value = value; 
        newNode->left = NULL;
        newNode->right = NULL;

        if (root == NULL){  //ไม่มีสักตัว
            root = newNode;
        }else{
            p = root;
            while(p != NULL){
            prev = p;
                if (p->value > newNode->value){
                    p = p->left;
                }else {
                    p = p->right;
                }
            }

            if (prev->value > newNode->value){
                prev->left = newNode;
            } else{
                prev->right = newNode;
            }
        }
    }

    void remove(int value) {
        remove1(value,root);
    }

    void remove1(int value,BSTNode *&root){
        BSTNode *temp = new BSTNode;

        if(root == NULL){
            return;
        }else if (value > root -> value){
            remove1(value,root->right);
        }else if (value < root -> value){
            remove1(value,root->left);
        }else{
            if (root->left == NULL && root->right == NULL){
                delete root;
                root = NULL;
            }else if(root->right == NULL){
                temp = root;
                root = root -> left;
                delete temp;
            }else if (root->left == NULL){
                temp = root;
                root = root -> right;
                delete temp;
            }else {
                temp = min(root->right);
                root -> value = temp -> value;
                remove1(temp->value,root->right);
            }
        }
  }

    BSTNode* min(BSTNode * root){
        while(root->left != NULL)
            root = root -> left;
            return root;
        }
   

    

    int get_depth(int value) {
        int depth = 0;
        BSTNode *p;

        if (root == NULL){
            return 0;
        }

        p = root;
        while (p != NULL){
            if (p->value != value){
                if (p->value <= value){ //g
                    p = p->right;}
                else{
                    p = p->left;
                }
            depth++;
            }
            else {
                break;        //g
            }
        }

        if (p == NULL){
            return -1;
        }else{
            return depth;
        }
    }

};
