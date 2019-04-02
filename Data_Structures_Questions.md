Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
   Linked List solution: O(c)
   Array solution: O(c)

2. What is the runtime complexity of `dequeue`?
   Linked List solution: O(c)
   Array solution: O(n), since with the removal of the first item in the list everything else now has to be shifted up by one index

3. What is the runtime complexity of `len`?
   Linked List solution: O(c)
   Array solution: O(c)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

   O (c)

2. What is the runtime complexity of `ListNode.insert_before`?

   O (c)

3. What is the runtime complexity of `ListNode.delete`?

   O (c)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

   O (c)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

   O (c)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

   O (c)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

   O (c)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

   O (c)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

   O (c)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    O (c)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The runtime of the doubly linked list's `delete` method is O (c), while the runtime of `Array.splice` is O (n). This means that the `delete` method performs better.
