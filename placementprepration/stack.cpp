#include<iostream>
using namespace std;

class Stack {
private:
    int top;
    int maxSize;
    int* array;

public:
    Stack(int size) {
        maxSize = size;
        array = new int[maxSize];
        top = -1;
    }

    bool isEmpty() {
        return (top == -1);
    }

    bool isFull() {
        return (top == maxSize - 1);
    }

    void push(int value) {
        if (isFull()) {
            cout << "Stack Overflow! Cannot push " << value << endl;
            return;
        }
        array[++top] = value;
        cout << value << " pushed to stack" << endl;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack Underflow! Cannot pop from empty stack" << endl;
            return -1;
        }
        int value = array[top--];
        return value;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return array[top];
    }

    ~Stack() {
        delete[] array;
    }
};

int main() {
    Stack s(5);  
    s.push(10);
    s.push(20);
    s.push(30);
    
    cout << "Top element is: " << s.peek() << endl;
    
    cout << s.pop() << " popped from stack" << endl;
    cout << s.pop() << " popped from stack" << endl;
    
    cout << "Is stack empty? " << (s.isEmpty() ? "Yes" : "No") << endl;
    
    return 0;
}