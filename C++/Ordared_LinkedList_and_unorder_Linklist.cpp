

#include <iostream>
using namespace std;

struct Node
{
	int info;
	Node *link;
};

class linkedListIterator
{
	private:
	Node  *current;
	public:
	linkedListIterator()
	{
		current = 0;
	}
	linkedListIterator(Node  *ptr)
	{
		current = ptr;
	}
	int operator*()
	{
		return current->info;
	}
	linkedListIterator  operator++()
	{
		current = current->link;
		return *this;
	}
	bool operator==(const linkedListIterator & right) const
	{
		return (current==right.current);
	}
	bool operator!=(const linkedListIterator & right) const
     {
		return (current != right.current);
	 }

};

class linkedList
{
		protected:

		int count;
		Node  *first;
		Node  *last;

		private:

		void copyList(const linkedList & otherList)
		{
			Node  *newNode;
			Node  *current;
			if (first != 0)
				destroyList();

			if (otherList.first == 0)
				{
					first = 0;
					last = 0;
					count = 0;
				}
			else
				{
			current = otherList.first;
			count = otherList.count;
			first = new Node ;
			first->info = current->info;
			first->link = 0;
			last = first;
			current = current->link;
			while (current != 0)
				{
			newNode = new Node ;
			newNode->info = current->info;
			newNode->link = 0;
			last->link = newNode;
			last = newNode;
			current = current->link;
				}
			}
		}

		public:

		const linkedList & operator=(const linkedList  & otherList)
		{
			if (this != &otherList)
				{
					copyList(otherList);
				}
			return *this;
		}

		void initializeList()
		{
			destroyList();
		}

		bool isEmptyList() const
		{
			return (first == 0);
		}

		void print() const
		{
			Node  *current;
			current = first;
			while (current != 0)
				{
				cout << current->info << " ";
				current = current->link;
				}
		}

		int length() const
		{
			return count;
		}

		void destroyList()
		{
			Node  *temp;

			while (first != 0)
				{
					temp = first;
					first = first->link;
					delete temp;
				}
				last = 0;
				count = 0;
		}

		int front() const
		{
			if(first != 0)
  			return first->info;
		}

		int back() const
		{
			if(last != 0)
			return last->info;
		}

		linkedListIterator begin()
		{
			linkedListIterator  temp(first);
			return temp;
		}
		linkedListIterator  end()
		{
			linkedListIterator  temp(0);
			return temp;
		}
		linkedList()
		{
			first = 0;
			last = 0;
			count = 0;
		}
		linkedList(const linkedList & otherList)
		{
			first = 0;
			copyList(otherList);
		}
		~linkedList()
		{
			destroyList();
		}

		virtual void insertFirst(const int& newItem) = 0;
		virtual void insertLast(const int& newItem) = 0;
		virtual void deleteNode(const int& deleteItem) = 0;
};

class unorderedLinkedList: public linkedList
{
public:

bool search(const int& searchItem) const
{
	Node  *current;
	bool found = false;
	current = first;
	while (current != 0 && !found)
		if (current->info == searchItem)
		found = true;
		else
		current = current->link;
		return found;
}

void insertFirst(const int& newItem)
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

void insertLast(const int& newItem)
{
	Node  *newNode;
	newNode = new Node ;
	newNode->info = newItem;
	newNode->link = 0;

	if (first == 0)
	{
	first = newNode;
	last = newNode;
	count++;
	}
	else
	{
	last->link = newNode;
	last = newNode;
	count++;
	}
}

void deleteNode(const int& deleteItem)
{
 	Node  *current;
	Node  *trailCurrent;
	bool found;
	if (first == 0)
		cout << "Cannot delete from an empty list."<< endl;
		else
			{
				if (first->info == deleteItem)
					{
						current = first;
						first = first->link;
						count--;
				if (first == 0)
						last = 0;
						delete current;
					}
				else
					{
						found = false;
						trailCurrent = first;
						current = first->link;
						while (current != 0 && !found)
							{
								if (current->info != deleteItem)
									{
										trailCurrent = current;
										current = current-> link;
									}
								else
										found = true;
							}
								if (found)
									{
										trailCurrent->link = current->link;
										count--;

										if (last == current)

											last = trailCurrent;
											delete current;
									}
								else
									cout<<"The item to be deleted is not in the list." << endl;
			}
		}
	}

};

class orderedLinkedList: public linkedList
{
public:
bool search(const int& searchItem) const
{
	bool found = false;
	Node  *current;
	current = first;
	while (current != 0 && !found)
		if (current->info >= searchItem)
			found = true;
		else
			current = current->link;
		if (found)
			found = (current->info == searchItem);
			return found;
}

void insert(const int& newItem)
{
	Node  *current;
	Node  *trailCurrent;
	Node  *newNode;

	bool found;
	newNode = new Node ;
	newNode->info = newItem;
	newNode->link = 0;
	if (first == 0)
		{
			first = newNode;
			last = newNode;
			count++;
		}
	else
		{
			current = first;
			found = false;
				while (current != 0 && !found)

					if (current->info >= newItem)
						found = true;
						else
						{

							trailCurrent = current;
							current = current->link;
						}
						if (current == first)
						{
							newNode->link = first;
							first = newNode;
							count++;
						}
						else
						{
							trailCurrent->link = newNode;
							newNode->link = current;

							if (current == 0)
								last = newNode;
								count++;
						}
		}
}

void insertFirst(const int& newItem)
{
	insert(newItem);
}
void insertLast(const  int& newItem)
{
	insert(newItem);
}
void deleteNode(const  int& deleteItem)
{
	Node  *current;
	Node  *trailCurrent;
	bool found;
	if (first == 0)
		cout << "Cannot delete from an empty list." << endl;
	else
	{
		current = first;
		found = false;

		while (current != 0 && !found)

		if (current->info >= deleteItem)
			found = true;
		else
		{
			trailCurrent = current;
			current = current->link;
		}
		if (current == 0)

			 cout<<"The item to be deleted is not in the list." << endl;
		else

			if (current->info == deleteItem)
			{
				if (first == current)
				{
					first = first->link;

					if (first == 0)
						last = 0;

						delete current;
				}
				else
				{
					trailCurrent->link = current->link;

					if (current == last)
						last = trailCurrent;

						delete current;
				}
				count--;
			}

			else

			cout << "The item to be deleted is not in the list." << endl;
	}
}
};


int main()
{
    orderedLinkedList orlist;
    unorderedLinkedList unlist;
    linkedListIterator atratot;
   cout<<"we insert this number into unorder Linkedlist  fallow this number \n";
    unlist.insertFirst(10);
    unlist.insertFirst(100);
    unlist.insertFirst(5);
    unlist.insertFirst(1);
    unlist.insertFirst(8);
    unlist.insertFirst(9);
    unlist.insertFirst(0);
    unlist.insertFirst(1000);
    unlist.insertFirst(53);


    unlist.print();
    cout<<"\n";
    cout<<"We insert this number to order linked list fallow this number \n";
    orlist.insertFirst(10);
    orlist.insertFirst(100);
    orlist.insertFirst(5);
    orlist.insertFirst(1);
    orlist.insertFirst(8);
    orlist.insertFirst(9);
    orlist.insertFirst(0);
    orlist.insertFirst(1000);
    orlist.insertFirst(53);

    orlist.print();

    orlist.deleteNode(1000);

    cout<<orlist.front()<<"\n";

    atratot = orlist.begin();

    while(atratot != 0)
    {
        cout<<*atratot<<",";

        ++atratot;
    }

    return 0;
}
