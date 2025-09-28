"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
   seen = set()
   for pid in product_ids:
     if pid in seen:
      return True
     seen.add(pid)
     return False
   
#I used a set because it provides O(1) average-time lookup and insertion. 
#The overall runtime is O(n) with O(n) space, which is efficient for detecting duplicates.


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
from collections import deque

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.queue = deque()

    def add_task(self, task):
         self.queue.append(task)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None 
    
#I used a deque because it allows O(1) insertion at the end and O(1) removal from the front. 
#A regular list would make removing the first element O(n) due to shifting. 
#This data structure is ideal for queue-like behavior where order must be preserved.


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.seen = set()

    def add(self, value):
        self.seen.add(value)

    def get_unique_count(self):
        return len(self.seen)
    
#I used a set to automatically store only unique values, since sets discard duplicates by design. 
#Adding values and checking size are O(1) on average, so I can efficiently track uniqueness over a stream of data. 
#This ensures both correctness and efficiency in counting distinct elements.

