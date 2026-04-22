from collections import deque
import sys

# 1. BINARY SEARCH TREE (BST)
class BSTNode:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Case 1: Leaf
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children
            successor = self._find_min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# 2. GRAPH (Adjacency List)
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dst, weight):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        self.adj_list[src].append((dst, weight))

    def print_adjacency_list(self):
        print("Adjacency List:")
        for node in self.adj_list:
            edges = ", ".join(f"{n}({w})" for n, w in self.adj_list[node])
            print(f"{node} -> [{edges}]")

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("BFS Traversal:", end=" ")

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor, _ in self.adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    def dfs(self, start):
        visited = set()
        print("DFS Traversal:", end=" ")
        self._dfs(start, visited)
        print()

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor, _ in self.adj_list[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)


# 3. HASH TABLE (Separate Chaining)
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return True
        return False

    def print_table(self):
        print("Hash Table:")
        for i, bucket in enumerate(self.table):
            content = " -> ".join(f"({k},{v})" for k, v in bucket) if bucket else "EMPTY"
            print(f"Bucket[{i}]: {content}")


# MAIN PROGRAM
def main():

    #BST
    print("===== BST OPERATIONS =====")
    bst = BST()

    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Inorder:", bst.inorder_traversal())

    print("Search 20:", bst.search(20))
    print("Search 90:", bst.search(90))

    bst.delete(20)
    print("After deleting 20:", bst.inorder_traversal())

    bst.insert(65)
    bst.delete(60)
    print("After deleting 60:", bst.inorder_traversal())

    bst.delete(50)
    print("After deleting 50:", bst.inorder_traversal())

    #GRAPH
    print("\n===== GRAPH =====")
    g = Graph()

    edges = [
        ('A','B',2), ('A','C',4),
        ('B','D',7), ('B','E',3),
        ('C','E',1), ('C','F',8),
        ('D','F',5),
        ('E','D',2), ('E','F',6)
    ]

    for u, v, w in edges:
        g.add_edge(u, v, w)

    g.print_adjacency_list()
    g.bfs('A')
    g.dfs('A')

    #HASH TABLE
    print("\n===== HASH TABLE =====")
    ht = HashTable(5)

    keys = [10, 15, 20, 7, 12]
    for k in keys:
        ht.insert(k, f"Value{k}")

    ht.print_table()

    print("Get 10:", ht.get(10))
    print("Get 15:", ht.get(15))
    print("Get 7:", ht.get(7))

    ht.delete(15)
    print("After deleting 15:")
    ht.print_table()


# Run
if __name__ == "__main__":
    main()