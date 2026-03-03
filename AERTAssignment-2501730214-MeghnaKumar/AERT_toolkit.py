# PART A: STACK ADT (ADT+OPERATIONS)

class StackADT:
    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
# PART B: FACTORIAL AND FIBONACCI (RECURSION + COMPLEXITY)

# Factorial function using recursion
def factorial(n):
    if n<0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

# Fibonacci (Naive)
naive_calls = 0
def fib_naive(n):
    global naive_calls
    naive_calls +=1
    if n <=1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Fibonacci (Memoization)
memo_calls = 0
def fib_memo(n, memo={}):
    global memo_calls
    memo_calls +=1
    if n in memo:
        return memo[n]
    if n <=1:
        return n
    memo[n] = fib_memo(n-1,memo) + fib_memo(n-2,memo)
    return memo[n]

# PART C:TOWER OF HANOI (RECURSION + TRACE)

def hanoi(n, source, auxiliary, destination, stack):
    if n ==1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        stack.push(move)
        return
    hanoi(n-1, source, destination, auxiliary, stack)
    move= f"Move disk {n} from {source} to {destination}"
    print(move)
    stack.push(move)
    hanoi(n-1, auxiliary, source, destination, stack)

# PART D: RECURSIVE BINARY SEARCH (DIVIDE & CONQUER + RECURRENCE)

def binary_search(arr, key, low, high):
    if low> high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid-1)
    else:
        return binary_search(arr, key, mid+1, high)
    

## MAIN FUNCTION TO TEST ALL PARTS

if __name__ == "__main__":

    print ("Testing Stack ADT:")
    s = StackADT()
    s.push(10)
    s.push(20)
    print("Stack size:", s.size())
    print("Top element:", s.peek())
    print("Popped element:", s.pop())
    print("Stack empty?", s.is_empty())

    print("\nTesting Factorial:") 
    for n in [0,1,5,10]:
        print(f"factorial of {n} is {factorial(n)}")

    print("Testing Fibonacci:")
    for n in [5,10,20,30]:
        naive_calls = 0
        memo_calls = 0
        memo = {}
        print(f"\nFibonacci({n})") 
        print(f"Navive Result:", fib_naive(n))
        print(f"Naive calls:", naive_calls)        
        print(f"Memoized Result:", fib_memo(n, memo))
        print(f"Memoized calls:", memo_calls)

    print("\nTesting Tower of Hanoi(n=3):")
    hanoi_stack = StackADT()
    hanoi(3, 'A', 'B', 'C', hanoi_stack)

    print("\nTesting Binary Search:")
    arr = [1,2,3,4,5,6]
    keys = [3,6,7]
    for key in keys:
        result = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key}: Index=", result)
    empty_arr = []
    print("Search in empty array:", binary_search(empty_arr, 5, 0, -1))
    