#pragma once


struct listNode {
	int num;
	std::shared_ptr<listNode> next;
	listNode() = default;
	listNode(int vNum) :num(vNum), next(nullptr) {}
	void show() {
		std::cout << num << " ";
	}
};


struct llist {
	llist() = default;
	void insert(int v) {
		listNode tmpNode(v);
		if (head == nullptr)
		{
			head = std::make_shared<listNode>(tmpNode);
			return;
		}
			
		auto curr = head;
		while (curr->next != nullptr)
			curr = curr->next;
		curr->next = std::make_shared<listNode>(tmpNode);
	}

	void reverse()
	{
		std::shared_ptr<listNode> prev = nullptr;
		auto curr = head;
		while (true)
		{
			auto next = curr->next;
			if (curr == nullptr)
				break;
			curr->next = prev;
			prev = curr;
			curr = next;
			//next->next = 

		}
	}


	void show() {
		auto curr = head;
		while (curr != nullptr)
		{
			curr->show();
			curr = curr->next;
		}	
		std::cout << "\n";
	}
	std::shared_ptr<listNode> head;
};

void TestLL() {
	llist l;
	for (int i = 0; i < 10; i++) {
		l.insert(genRandomInRange());
	}
	
	l.show();
}