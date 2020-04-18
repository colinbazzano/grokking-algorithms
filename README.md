# Grokking Algorithms

Code to follow along while reading the book Grokking Algorithms

## Notes to be recalled on

What is an algorithm?

    An algorithm is a set of instructions for accomplishing a task.

What is a permutation?

    A way, especially one of several possible variations, in which a set or number of things can be ordered or arranged.

What is [logarithm](https://simple.wikipedia.org/wiki/Logarithm)?

    A quantity representing the power to which a fixed number (the base) must be raised to produce a given number. Logs are the flip of exponentials. What number you have to raise to, to get another number

log b (a) = c <<< logarithm || exponential >>> b^c = a

where b is the base, c is the exponent, and a is called the argument

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
