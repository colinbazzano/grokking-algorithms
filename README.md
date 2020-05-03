# Grokking Algorithms

Code to follow along while reading the book [Grokking Algorithms](https://www.manning.com/books/grokking-algorithms).

The author is Aditya Y. Bhargava, and you can find more about him at [adit.io](adit.io)

## Notes to be recalled on

What is an algorithm?

    An algorithm is a set of instructions for accomplishing a task.

What is a permutation?

    A way, especially one of several possible variations, in which a set or number of things can be ordered or arranged.

What is [logarithm](https://simple.wikipedia.org/wiki/Logarithm)?

    A quantity representing the power to which a fixed number (the base) must be raised to produce a given number. Logs are the flip of exponentials. What number you have to raise to, to get another number

log b (a) = c <<< logarithm || exponential >>> b^c = a

where b is the base, c is the exponent, and a is called the argument

Queues are _FIFO_ (First In, First Out)
Stacks are _LIFO_ (Last In, First Out)

Need to find the shortest path in an unweighted graph? Use breadth-first search
Need to find the shortest path in a weighted graph? Dijkstra's algorithm

## Binary Search

Try to guess what number I'm thinking of, 1-100. You would not be wise to start at 1 and count up, but better off starting at 50, eliminating half the numbers if I say "too low" or "too high" and then cut the next group in half.

Binary Search (when sorted) has a Big O runtime of: `O(log n)`

## Inductive Proofs

    They are one way to prove that your algorithm works. Each inductive proof has two steps:
        1. The base case.
        2. The inductive case
    Can your algorithm hit the base case and perform the work on the half baked functions?
    Can your algorithm grow in input size and still perform the way that you want it to?

## Big O Notation

    In a nutshell: It's not enough to know how long an algorithm takes to run - you need to know how the running time increases as the list size increases. That is where Big O notation comes in.

    Big O notation lets you compare teh number of operations. How fast the algorithm grows.

    Big O is about worst case scenario

### Common Big O run times

    O(log n) - log time, example: binary search

    O(n) - linear time, example: simple search

    O(n * log n) - A fast sorting algorithm, like quick sort

    O(n**2) - a slow sorting algorithm like selection sort

    O(n!) - Factorial - a really slow algorithm, like the traveling salesperson

Algorithm speed isn't measured in seconds, but in growth of the number of operations

Instead, we talk about how quickly the run time of an algorithm increases as the size of the input increases

Run time of algorithms is expressed in Big O notation

O(log n) is faster than O(n), but gets a LOT faster as the list of items grows.

## Arrays and linked lists

### Arrays (random access):

    Reading: O(1)
    Insertion: O(n)
    Deletion: O(n)

### Linked Lists (sequential access):

    Reading: O(n)
    Insertion: O(1)
    Deletion: O(1)

## Recursion

    When you write a recursive function, you have to tell it when to stop recursing.
    That's why every recursive function has two parts: the base case and the recursive case.

    Often, when you're writing a recursive function involving an array, the base case is often an empty array or an array with one element.

## Divide and Conquer

    Divide and Conquer works by breaking a problem down into smaller and smaller pieces.
    If you're using D&C on a list, the base case is probably an empty array or an array with 1 element

    When you approach a problem, you should think,
    "Can I solve this if I use divide and conquer?"

    One example of D&C is quicksort.

Euclid's algorithm is good to know, and you can learn more [here](https://www.khanacademy.org/computing/computer-science/cryptography.modarithmetic/a/the-euclidean-algorithm)

Practical Divide and Conquer tactics:

1. Figure out the base case. This should be the simplest possible case.
2. Divide or decrease your problem until it becomes the base case.

## Hash Tables

    It technical terminology, we'd say that a hash function "maps strings to numbers."

    Hash Tables require a few things:

    1. Consistency. Suppose you put in "apple" and get back "4". You should always get 4 back.
    2. Different words => different numbers. In the best case, every different word should map to a different number.

    Hash function + array = Hash Table!

To avoid collisions in hash tables, you'll need

1. A low load factor - number of items in a hash table OVER total number of slots
2. A good hash function

If you have 1 item in a hash table of 3, that is 1/3! If you are getting close to having a full
hash table, you'll need to do what's called "resizing". A good rule of thumb is to create a hash table that is double the size.
You should resize when your hash table is .7 load factor.

## Graphs (in tandem with breadth-first search)

    A graph, simply put, models a set of connections.

Each graph is made up of:

    Nodes - Think of it as yourself, and your friends are other nodes, and if directed related, are *neighbors*
    Edges - Draws the line from one node to the other

Directed Graph - the relationship is only one way. Say you have a friend, you are connected to them, but there friend's list doesn't extend beyond them.

Undirected Graph - do not have arrows, and the relationship goes both ways.

## Breadth First Search

    BFS is an algorithm for graphs! It allows you to find the shortest distance between two things.

You could:

- Write a checkers AI that calculates the fewest moves to victory
- Write a spell checker
- Find the doctor closest to you in your network

Think of going from one place to the other, and the number of steps you may take to get there.
You could also think of the smallest number of moves to checkmate in a game of chess.

_The algorithm to solve a shortest-path problem is called breadth-first search._

In the book's example of Twin Peaks to Golden Gate Bridge, you have two steps:

    1. Model the problem as a graph
    2. Solve the problem using breadth-first search

A few questions are answered when using BFS

    Is there a path from node A to node B?
    What is the shortest path from node A to node B?

When thinking about the Mango Seller example, use it to remember that first-degree connections are better than second-degree, and second-degree is better than third-degree, etc.

You'll want to search your closest connections first, and to do this we use another data structure, called a _queue_

## Queue

    FIFO - First In First Out
    Video Game queue, when the server's are overloaded and you start up your game, you'll be loaded in in the order in which you showed up.

    You *cannot* access random elements in the queue. You may only enqueue and/or dequeue.

    Enqueue (push) - You add an item to the queue, that item is added to the END of the queue.
    Dequeue (pop) - You are removing an item from the queue, that item was at the FRONT of the queue.

Tree - A special type of graph, where _no edges ever point back_.

## Dijkstra's Algorithm

In short, Dijkstra's Algorithm lets you answer "What's the shortest path to X?" for weighted graphs

Breadth-first search will find the shortest, but if you were to add times to those paths, it may not be the shortest that is the quickest. That is where Dijkstra's algorithm to help find the fastest.

4 Steps to Dijkstra's Algorithm:

    1. Find the 'cheapest' node. This is the node you can get to in the least amount of time.
    2. Check whether there's a cheaper path to the neighbors of the node. Update the costs of the neighbors of this node.
    3. Repeat until you've done this for every node in the graph.
    4. Calculate the final path

In Dijkstra's algorithm, you assign a number or weight to each segment. It then finds the path with the smallest total weight.

Each edge in the graph has a number associated with it. Those are called the _weights_

We are creating a weighted graph.

Dijkstra's algorithm only works with directed acyclic graphs, DAGs for short.

You _may not_ use negative-weight edges in Dijkstra's algorithm.

If you were to use negative-weight edges, you would need to look at Bellman-Ford algorithm.

When using Dijkstra's, you will want to have your finish set to "infinity" distance away, so you can overwrite with the fastest path there, even if in the loop that's not the fastest of them all, it's the fastest for right now.

## Greedy Algorithms

NP-complete problems have no known fast solution. If you have an NP-complete problem, your best bet is to use an approximation algorithm.

A greedy algorithm is simple, at each step, pick the optimal move.

Enter: approximation algorithms. They will be judged by:

    How fast they are
    How close they are to the optimal solution

### Sets

You have a few things you can do with sets in particular.

Set Union - Combine both sets.

Set Intersection - Find the items that show up in both sets

Set Difference - Subtract the items in one set from the items in another set.

Short explanation of NP-completeness: some problems are famously hard to solve. The traveling salesperson and the set-covering problems are two examples.

Some "giveaways" to a NP-Problem:

- Your algorithm runs quickly with a handful of items but really slows down with more items.

- "All combinations of X" usually point to an NP-complete problem.

- Do you have to calculate "every possible version" of x because you can't break it down into smaller sub-problems? Might be NP-complete

- If your problem involves a sequence and it's hard to solve, might be NP-complete

- If you problem involves a set and it's hard to solve, might be NP-complete

- Can you restate your problem as the set-covering problem or the traveling-salesperson? Definitely NP-complete.

## Dynamic Programming

Dynamic Programming starts by solving sub-problems and building up to solve the big problem.

Using the knapsack problem, you are start to break it down and realize the power and importance of Dynamic Programming.

If you have decimals and are drawing a grid to understand, you may have to take a more finer approach with 1.5 2 2.5 etc

With Dynamic Programming in relation to the knapsack problem, you can take the item or not, no decimals in this case.

Dynamic programming only works when each sub-problem is discrete- when it doesn't depend on other sub-problems.

Dynamic programming is useful when you're trying to optimize something given a constraint.

Dynamic programming involves:

    Solution always involves a grid.

    The values in the cells are usually what you're trying to optimize.

    Each sell is a sub-problem, so think about how you can divide your problem down.

Something neat to checkout is Levenshtein Distance. It measures the similarity of two strings.
