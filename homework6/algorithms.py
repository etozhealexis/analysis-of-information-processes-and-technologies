# класс односвязного списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# класс Односвязный список
class LinkedList:
    def __init__(self, *values):
        self.head = None
        self.tail = None
        self.len = 0
        for value in values:
            self.insert_in_tail(value)

    def __len__(self):
        return self.len

    def prepend_value(self, data):
        new_node = Node(data)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            self.head = new_node
            new_node.next = tmp
        self.len += 1

    def insert_in_tail(self, data):
        new_node = Node(data)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.tail
            self.tail = new_node
            tmp.next = new_node
        self.len += 1

    def insert(self, index, data):
        if index < 0 or index >= len(self):
            raise IndexError
        elif index == 0:
            self.prepend_value(data)
        elif index == len(self)-1:
            self.insert_in_tail(data)
        else:
            new_node = Node(data)
            current = self.head
            for i in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.len += 1

    def remove(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        elif index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
        self.len -= 1

    def find_value(self, data):
        pos = 0
        for item in self:
            if item == data:
                return pos
            pos += 1
        return -1
    
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current.data
    
    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    def split(self):
        middle = len(self) // 2
        current = self.head
        for i in range(middle):
            current = current.next

        second = LinkedList()
        second.head = current
        second.tail = self.tail
        second.len = len(self) - middle
        
        self.tail = current
        self.len = middle
        return second

    def __repr__(self):
        return f'[{", ".join([str(item) for item in self])}]'

    def merge_sorted_lists(list1, list2):
        if len(list1) == 0:
            return list2
        elif len(list2) == 0:
            return list1
        else:
            result = LinkedList()
            i = 0
            j = 0
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    result.insert_in_tail(list1[i])
                    i += 1
                else:
                    result.insert_in_tail(list2[j])
                    j += 1
            while i < len(list1):
                result.insert_in_tail(list1[i])
                i += 1
            while j < len(list2):
                result.insert_in_tail(list2[j])
                j += 1
            return result


# класс узла бинарного дерева
class TreeNode:
  def __init__(self, value = None, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def set_children(self, left = None, right = None):
    if left is not None:
      self.left = left
    if right is not None:
      self.right = right


# класс бинарного дерева
class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def print_tree_90(self, node = None, depth = 0):
        if node == None:
            self.print_tree_90(self.root, 0)
        else:
            if node.right != None:
                self.print_tree_90(node.right, depth+1)
            print(depth*'    ' + str(node.value))
            if node.left != None:
                self.print_tree_90(node.left, depth+1)

    def find_in_bst(self, value):
        def recursive(value, path=None, node=None):
            if node is None:
                return recursive(value, [], self.root)
            else:
                path.append(node.value)
                if node.value == value:
                    return path
                elif node.value > value:
                    if node.left is None:
                        print("Узел не найден")
                        return None
                    return recursive(value, path, node.left)
                else:
                    if node.right is None:
                        print("Узел не найден")
                        return None
                    return recursive(value, path, node.right)

        return recursive(value)
    
    def sorted_list_to_bst(lst):
        if len(lst) == 0:
            return None

        middle_index = len(lst) // 2 if len(lst) % 2 == 1 else len(lst) // 2 - 1
        root = TreeNode(lst[middle_index])
        root.left = BinaryTree.sorted_list_to_bst(lst[ : middle_index])
        root.right = BinaryTree.sorted_list_to_bst(lst[(middle_index + 1) : ])
        return root
    

# Алгоритм подсчета воды
def calc_capacity(heights: list) -> int:
    ans = 0
    maxHeight = max(heights)
    firstPossibleMax = 0
    secondPossibleMax = 0

    i = 1
    while i < len(heights):
        currentHeight = i - 1
        while heights[currentHeight] > heights[i]:
            i += 1

        ans += (i - currentHeight) * heights[currentHeight]

        if heights[i] == maxHeight:
            firstPossibleMax = i
            break
        i += 1

    i = len(heights) - 2
    while i > 1:
        currentHeight = i + 1
        while heights[currentHeight] > heights[i]:
            i -= 1

        ans += (currentHeight - i) * heights[currentHeight]

        if heights[i] == maxHeight:
            secondPossibleMax = i
            break
        i -= 1

    if firstPossibleMax != secondPossibleMax:
        ans += abs(secondPossibleMax - firstPossibleMax) * maxHeight

    return ans