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

2.2 Suppose you're building an app for restaurants to take customer orders. Your app needs to store a list of orders. Servers keep adding orders to this list, and chefs take orders off the list and make them. It's an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it.
Would you use an array or linked list to implement this queue?

My answer: Though reality uses an array, because we don't know when enoughs enough at a restaurant (iykyk), I think a linked list would work best. You are tailing onto the end and the sequential access of a linked list allows for smoother insertions to the end of the list. I could also see the argument for an array, because you can tap on to the end with random access, as the array gets deleted from the front.

2.3 Binary search needs random access, as well as sorting, so an array makes the most sense.

2.4 Downsides to the array would be the insertion, and possible deletion, of usernames in the array. When you add new users, they will be tagged onto the end, and you might run out of the memory to hold the users.

2.5 I think that the hybrid data structure (array of linked lists) would be slower at searching, though the letter access is good, the searching of a linked list would not be ideal, however, insertion would be faster. You have 26 items to go through via random access, and tag onto the linked list. It's an ordered linked list, in a way.

3.1 Look at the call stack and address what is going on from what is shown

My Answer: First, there is a name, maggie, that is stored into memory. Then a Greet function is added to the stack. After that, it appears the name maggie is used again while calling a Greet2 function.

3.2 Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

My Answer: It would continually build up functions to call on the stack, as it won't reach the base case to solve those functions