

#include <iostream>
using namespace std;
class queuet
{
public:
virtual bool isEmptyQueue() const = 0;
virtual bool isFullQueue() const = 0;
virtual void initializeQueue() = 0;
virtual int front() const = 0;
virtual int back() const = 0;
virtual void addQueue(const int& queueElement) = 0;
virtual void deleteQueue() = 0;
};

class QeueArrays : public queuet
{
	private:
	int maxQueueSize;
	int count;
	int queueFront;
	int queueRear;
    int *list;

	public:

	const QeueArrays & operator=(const QeueArrays &);
	bool isEmptyQueue() const
	{
		return (count == 0);
	}
	bool isFullQueue() const
	{
		return (count == maxQueueSize);
	}
	void initializeQueue()
	{
		queueFront = 0;
		queueRear = maxQueueSize - 1;
		count = 0;
	}
	int front() const
	{
		if(!isEmptyQueue())
		return list[queueFront];
	}
	int back() const
	{
		if(!isEmptyQueue());
		return list[queueRear];
	}
	void addQueue(const int& newElement)
	{
		if (!isFullQueue())
		{
			queueRear = (queueRear + 1) % maxQueueSize;
			count++;
			list[queueRear] = newElement;
		}
		else
			cout << "Cannot add to a full queue " << endl;
	}
	void deleteQueue()
	{
		if (!isEmptyQueue())
		{
			count--;
			queueFront = (queueFront + 1) % maxQueueSize;
		}
		else
			cout << "Cannot remove from an empty queue " << endl;
	}

	QeueArrays(int queueSize = 100)
	{
		if (queueSize <= 0)
		{
			cout << "Size of the array to hold the queue must be positive " << endl;
			cout << "Creating an array of size 100 " << endl;
			maxQueueSize = 100;
		}
		else
			maxQueueSize = queueSize;

			queueFront = 0;
			queueRear = maxQueueSize - 1;
			count = 0;
			list = new int[maxQueueSize];
	}


	~QeueArrays()
	{
		delete [] list;
	}
};


struct Node
{
	int info;
	Node *link;
};

class Qeuelist : public queuet
{
	private:
	Node *queueFront;
	Node *queueRear;

	public:
	const Qeuelist & operator=(const Qeuelist &);
	bool isEmptyQueue() const
	{
		return (queueFront == 0);
	}
	bool isFullQueue() const
	{
		return false;
	}

	void initializeQueue()
	{
		Node *temp;
		while (queueFront!= 0)
		{
		temp = queueFront;
		queueFront = queueFront->link;
		delete temp;
		}
		queueRear = 0;
	}

	int front() const
	{
		if(queueFront != 0)
		return queueFront->info;
	}
	int back() const
	{
		if(queueRear!= 0)
		return queueRear->info;
	}
	void addQueue(const int& newElement)
	{
		Node *newNode;
		newNode = new Node;
		newNode->info = newElement;
		newNode->link = 0;
		if (queueFront == 0)
		{
			queueFront = newNode;
			queueRear = newNode;
		}
		else
		{
			queueRear->link = newNode;
			queueRear = queueRear->link;
		}

	}

	void deleteQueue()
	{
		Node *temp;
		if (!isEmptyQueue())
		{
			temp = queueFront;
			queueFront = queueFront->link;
			delete temp;
		if (queueFront == 0)
			queueRear = 0;
		}
		else
			cout << "Cannot remove from an empty queue" << endl;
		}

	Qeuelist()
	{
		queueFront = 0;
		queueRear = 0;
	}

	~Qeuelist()
	{
		initializeQueue();
	}

};
int main()
{
    QeueArrays qarr;

    qarr.addQueue(10);
    qarr.addQueue(20);
    qarr.addQueue(30);
    qarr.addQueue(40);
    qarr.addQueue(50);
    qarr.addQueue(60);

    qarr.deleteQueue();
    qarr.deleteQueue();


    cout<<qarr.front()<<"\n";
    cout<<qarr.back()<<endl;

    Qeuelist  qlist;

    qlist.addQueue(10);
    qlist.addQueue(20);
    qlist.addQueue(30);
    qlist.addQueue(40);
    qlist.addQueue(50);
    qlist.addQueue(60);

    qlist.deleteQueue();
    qlist.deleteQueue();


    cout<<qlist.front()<<"\n";
    cout<<qlist.back()<<"\n";

}

