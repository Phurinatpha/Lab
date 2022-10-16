class CharStack {

public:
  char charac[10];
  int s_top;
  CharStack() { // constructor
    s_top = -1;
  }

  void push(char new_item) {
    s_top++;
    charac[s_top] = new_item;
  }

  char pop() {
    charac[s_top] = ' ';
    s_top--;
    return charac[s_top];
  }

  char top() {
    return charac[s_top];
  }

  bool isEmpty() {
    return s_top == -1;
  }
};
