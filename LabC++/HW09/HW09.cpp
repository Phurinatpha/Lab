#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

struct Frequency {
public:
	vector<char> c; // ตัวอักษร
	vector<int> f;  // ความถี่
	int numChar; // จำนวนตัวอักษรทั้งหมด
};

class treeNode {
public:
	char character;
	int frequency;
	treeNode *leftChild;
	treeNode *rightChild;

};

class HuffmanTree {
private:
	treeNode *root;

public:
	HuffmanTree() {
		root = nullptr;
	}
	queue<treeNode*> single_q;
	queue<treeNode*> merge_q;

	void buildTree(Frequency *freq) {
		

		for (int i = 0; i < freq->numChar; i++){
			treeNode *qt = new treeNode;
			qt -> character = freq -> c[i];
			qt -> frequency = freq -> f[i];
			qt -> leftChild = NULL;
			qt -> rightChild = NULL;
      		single_q.push(qt); 
    	}
		
		while (single_q.size() + merge_q.size() > 1){
			treeNode *left, *right,*parent = new treeNode;
			if (!single_q.empty() && merge_q.empty()){
				left = single_q.front();
				single_q.pop();
			} else if (single_q.empty() && !merge_q.empty()){
				left = merge_q.front();
				merge_q.pop();
			} else if (!single_q.empty() && !merge_q.empty()){
				if (single_q.front() -> frequency > merge_q.front() -> frequency){
					left = merge_q.front();
					merge_q.pop();
				} else {
					left = single_q.front();
					single_q.pop();
				}
			}

			
			if (!single_q.empty() && merge_q.empty()){
				right = single_q.front();
				single_q.pop();
			} else if (single_q.empty() && !merge_q.empty()){
				right = merge_q.front();
				merge_q.pop();
			} else if (!single_q.empty() && !merge_q.empty()){
				if (single_q.front() -> frequency > merge_q.front() -> frequency){
					right = merge_q.front();
					merge_q.pop();
				} else {
					right = single_q.front();
					single_q.pop();
				}
			}
			
					
			parent-> frequency = left->frequency + right-> frequency;
			parent-> character = left->character + right-> character;
			parent-> leftChild = left;
			parent-> rightChild = right;

			merge_q.push(parent);
		}
		root = merge_q.front();
	}

	void decode(string code) {
		string text_out = "";
		treeNode *cur = root;
		for (int i = 0; i < code.size(); i++) {

			
			if (code[i] == '0'){ 
				cur = cur -> leftChild;
			} else {
				cur = cur -> rightChild;
			}

			if (cur -> leftChild == nullptr && cur -> rightChild == nullptr) {
				text_out += cur -> character;
				cur = root;
			}
		}
		cout << text_out << endl;
	}
};
