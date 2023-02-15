#include "BSTNode.cpp"
#include <iostream>
class BST {

public:
  BSTNode* root;

  BST() {
    root = nullptr;
  }

  void insert(int value) {
    BSTNode *p, *previous, *new_node = new BSTNode;
    new_node->value = value;
    new_node->left = nullptr;
    new_node->right = nullptr;

    if (root == nullptr){
        root = new_node;
    }else{
      p = root;
      while (p != nullptr){
        previous = p;
        if (p->value > new_node->value){
          p = p->left;
        }else {
          p = p->right;
        }
      }

      if (previous->value > new_node->value){
        previous->left = new_node;
      } else{
        previous->right = new_node;
      }
    }
  }


  void remove(int value) {
    removePri(value,root);
  }

  int get_depth(int value) {
    int depth = 0;
    BSTNode *p;

    if (root == NULL){
        return 0;
    }

    p = root;
    while (p != nullptr){
      if (p->value != value){
        if (p->value > value){
            p = p->left;}
        else{
            p = p->right;
        }
        depth++;
      }else {
        break;
      }
    }
    if (p != nullptr){
      return depth;
    }

    return -1;
  }

  void removePri(int value,BSTNode *&root){
    if(root == NULL){
      return;
    }else if (value < root -> value){
      removePri(value,root->left);
    }else if (value > root -> value){
      removePri(value,root->right);
    }else{
      if (root->left == NULL && root->right == NULL){
        delete root;
        root = NULL;
      }else if (root->left == NULL){
        BSTNode *temp = root;
        root = root -> right;
        delete temp;
      }else if(root->right == NULL){
        BSTNode *temp = root;
        root = root -> left;
        delete temp;
      }else {
        BSTNode *temp = findmin(root->right);
        root -> value = temp -> value;
        removePri(temp->value,root->right);
      }
    }
  }

  BSTNode* findmin(BSTNode * root){
    while(root->left != NULL)
      root = root -> left;
    return root;
  }
    
};
