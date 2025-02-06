import random
import time

class Node:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def _init_(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if key < current.val:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def find(self, key):
        current = self.root
        while current:
            if current.val == key:
                return True
            elif key < current.val:
                current = current.left
            else:
                current = current.right
        return False

def create_skewed_bst(x):
    bst = BinarySearchTree()
    for i in range(1, x + 1):
        bst.insert(i)
    return bst

def create_random_bst(x):
    bst = BinarySearchTree()
    values = random.sample(range(1, x * 10), x)  # Generate random integers
    for val in values:
        bst.insert(val)
    return bst

def measure_search_time(bst, key):
    start_time = time.time_ns()  # Record time in nanoseconds
    bst.find(key)
    end_time = time.time_ns()
    return end_time - start_time

# Values of n to test
n_values = [10*3, 104, 105, 106, 10*7]
times_skewed = []
times_balanced = []

print(f"{'n':>8} {'Skewed BST':>15} {'Balanced BST':>15}")

for n in n_values:
    # Create skewed BST
    skewed_bst = create_skewed_bst(n)
    # Create balanced BST
    balanced_bst = create_random_bst(n)
    
    # Measure search time for a number not in skewed BST (e.g., n + 1)
    time_skewed = measure_search_time(skewed_bst, n + 1)
    
    # Measure search time for a random number not in balanced BST (e.g., a large random number)
    time_balanced = measure_search_time(balanced_bst, n * 10 + 1)
    
    times_skewed.append(time_skewed)
    times_balanced.append(time_balanced)

    # Print the results in nanoseconds
    print(f"{n:>8} {time_skewed:>15} {time_balanced:>15}")
