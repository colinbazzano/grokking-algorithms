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
