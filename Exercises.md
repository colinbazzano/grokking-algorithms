Exercises

## Chapter 1

**_Binary Search_**
1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search.
What's the maximum number of steps it would take?

My Answer: 7

1.2 Suppose you double the size of the list. What's the max number of steps now?

My Answer: 8, maybe 9?

**_Big O_**
Give the run time for each of these scenarios in terms of Big O

1.3 You have a name, and you want to find the person's phone number in the phone book

O(log n) - You have 1 name, and can search it in a sorted phone book

1.4 You have a phone number, and you want to find the person's name in the phone book.

O(n) - The size of the phone book determines the numbers you are to search through.

1.5 You want to read the numbers of every person in the phone book.

O(n) - It's as big as the amount of inputs in the phone book

1.6 You want to read the numbers of just the A's.

O() - Not sure, yet.

## Chapter 2

**_Arrays and linked lists_**

2.1 Suppose you're building an app to keep track of your finances. Every day, you write down everything you spent money on.
At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. Should you use an array or a list?

My answer: A linked list. Lists have a O(1) constant time for insertion, and a O(n) linear time for reading.