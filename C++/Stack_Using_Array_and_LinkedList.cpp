#include <iostream>
using namespace std;
class stackclass
 {
public:
virtual void initializeStack() = 0;
virtual bool isEmptyStack() const = 0;
virtual bool isFullStack() const = 0;
virtual void push(const int& newItem) = 0;
virtual int top() const = 0;
virtual void pop() = 0;
 };


class stackArray: public stackclass
{
public:

void initializeStack()
{
	stackTop = 0;
}
bool isEmptyStack() const
{
	return(stackTop == 0);
}

bool isFullStack() const
{
	return (stackTop == maxStackSize);
}

void push(const int& newItem)
{
	if (!isFullStack())
	{
		list[stackTop] = newItem;
		stackTop++;
	}
	else
  		cout << "Cannot add to a full stack." << endl;
}

int top() const
{
	if(stackTop != 0)
	return list[stackTop - 1];
}

void pop()
{
	if (!isEmptyStack())
		stackTop--;
	else
		cout << "Cannot remove from an empty stack." << endl;
}
void print()
{
     cout<<"[";
    for(int i=stackTop-1; i>=0; i--)
    {
        cout<<list[i]<<",";
    }
    cout<<"]"<<endl;
}

stackArray(int stackSize = 10)
{
	if (stackSize <= 0)
	{
		cout<<"Size of the array to hold the stack must be positive." << endl;
		cout << "Creating an array of size 100." << endl;
		maxStackSize = 10;
	}
	else
		maxStackSize = stackSize;
		stackTop = 0;
		list = new int[maxStackSize];
}

stackArray(const stackArray& otherStack)
{
	list = 0;
	copyStack(otherStack);
}

~stackArray()
{
	delete [] list;
}
private:
int maxStackSize;
int stackTop;
int *list;

void copyStack(const stackArray& otherStack)
	{
	delete [] list;
	maxStackSize = otherStack.maxStackSize;
	stackTop = otherStack.stackTop;
	list = new int[maxStackSize];
	for (int j = 0; j < stackTop; j++)
	 list[j] = otherStack.list[j];
	}

};


struct Node
{
	int info;
	Node *link;
};

class StackLinkedList : public stackclass
{

public:
     void initializeStack()
     {   Node  *temp;
			while (first != 0)
				{
					temp = first;
					first = first->link;
					delete temp;
				}
				last = 0;
				count = 0;
     }

	 bool isEmptyStack() const
	 {
           return (first==0);
	 }

	 bool isFullStack() const
	 {
         return true;
	 }
	 void print()
	 {
	     Node *current;
	     current = new Node;
	     current = first;
	     cout<<"[";
	     for(int i=0; i<count; i++)
         {
             cout<<current->info<<",";
             current = current->link;
         }
         cout<<"]"<<endl;
	 }
	 void push(const int& newItem)
	 {
            Node  *newNode;
            newNode = new Node ;
            newNode->info = newItem;
            newNode->link = first;
            first = newNode;
            count++;

            if (last == 0)
                last = newNode;
	 }

	 int top() const
	 {
          return first->info;
	 }
	 void pop()
	 {
           if (first != 0 )
            {
            first= first->link;
            count--;
            }
           else
           	cout<<"Stack is empty "<<endl;
	 }

	StackLinkedList()
	{
		last = 0;
		first =0;
		count=0;
	}

	~StackLinkedList()
	{
		initializeStack();
	}
  private:
  Node *last;
  Node *first;
  int count;
};



int main()
{
    stackArray arrays;

    arrays.initializeStack();
    arrays.push(20);
    arrays.push(30);
    arrays.push(40);
    arrays.push(50);
    arrays.push(60);
    arrays.push(70);

    arrays.print();

    cout<<"Top is  "<<arrays.top()<<"\n";

    arrays.pop();
    arrays.pop();

    arrays.print();

    cout<<"Top is  "<<arrays.top()<<"\n";

    StackLinkedList lists;

    lists.push(30);
    lists.push(40);
    lists.push(50);
    lists.push(60);
    lists.push(70);
    lists.push(80);
    lists.pop();
    lists.pop();

    lists.print();
    cout<<"Top is  "<<lists.top()<<"\n";

    return 0;
}
