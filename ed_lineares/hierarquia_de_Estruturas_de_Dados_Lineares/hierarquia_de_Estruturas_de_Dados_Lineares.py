from abc import ABC, abstractmethod
from collections import deque

# Classe abstrata para as estruturas de dados lineares
class LinearStructure(ABC):
    @abstractmethod
    def length(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def is_full(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def retrieve(self):
        pass

# Implementação de uma Sequência Indexada (array)
class IndexedSequence(LinearStructure):
    def __init__(self, capacity=10):
        self.data = [None] * capacity
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == len(self.data)

    def insert(self, data, index=None):
        if self.is_full():
            raise Exception("Overflow")
        if index is None:
            index = self.size
        if index < 0 or index > self.size:
            raise Exception("Index out of bound")
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = data
        self.size += 1

    def remove(self, index=None):
        if self.is_empty():
            raise Exception("Underflow")
        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            raise Exception("Index out of bound")
        removed_data = self.data[index]
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1
        return removed_data

    def retrieve(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bound")
        return self.data[index]

# Implementação de uma Lista Encadeada Simples
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SimpleLinkedList(LinearStructure):
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        # Como é uma lista encadeada, assumimos que nunca estará "cheia"
        return False

    def insert(self, data, position=0):
        if position < 0 or position > self.size:
            raise Exception("Index out of bound")
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            previous_node = self.head
            for _ in range(position - 1):
                previous_node = previous_node.next
            new_node.next = previous_node.next
            previous_node.next = new_node
        self.size += 1

    def remove(self, position=0):
        if self.is_empty():
            raise Exception("Underflow")
        if position < 0 or position >= self.size:
            raise Exception("Index out of bound")
        if position == 0:
            removed_data = self.head.data
            self.head = self.head.next
        else:
            previous_node = self.head
            for _ in range(position - 1):
                previous_node = previous_node.next
            removed_data = previous_node.next.data
            previous_node.next = previous_node.next.next
        self.size -= 1
        return removed_data

    def retrieve(self, position):
        if position < 0 or position >= self.size:
            raise Exception("Index out of bound")
        current_node = self.head
        for _ in range(position):
            current_node = current_node.next
        return current_node.data

# Implementação de uma Pilha (stack)
class Stack(LinearStructure):
    def __init__(self):
        self.data = SimpleLinkedList()

    def length(self):
        return self.data.length()

    def is_empty(self):
        return self.data.is_empty()

    def is_full(self):
        return self.data.is_full()

    def insert(self, data):
        self.data.insert(data)

    def remove(self):
        return self.data.remove(0)

    def retrieve(self):
        return self.data.retrieve(0)

# Implementação de uma Fila Simples (queue)
class Queue(LinearStructure):
    def __init__(self):
        self.data = deque()

    def length(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def is_full(self):
        # Como é uma fila implementada com deque, assumimos que nunca estará "cheia"
        return False

    def insert(self, data):
        self.data.append(data)

    def remove(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.data.popleft()

    def retrieve(self):
        if self.is_empty():
            raise Exception("Underflow")
        return self.data[0]

# Aqui você pode adicionar mais implementações conforme necessário...

# Testes simples para verificar as implementações
def test_structures():
    # Testando IndexedSequence
    array = IndexedSequence(5)
    array.insert(1)
    array.insert(2, 1)
    array.insert(3, 2)
    print("Array content:", [array.retrieve(i) for i in range(array.length())])

    # Testando SimpleLinkedList
    linked_list = SimpleLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3, 1)
    print("Linked List content:", [linked_list.retrieve(i) for i in range(linked_list.length())])

    # Testando Stack
    stack = Stack()
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)
    print("Stack top:", stack.retrieve())

    # Testando Queue
    queue = Queue()
    queue.insert(1)
    queue.insert(2)
    queue.insert(3)
    print("Queue front:", queue.retrieve())

test_structures()
