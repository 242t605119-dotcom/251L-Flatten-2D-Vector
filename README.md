# Flatten 2D Vector

This repository contains my Python solution for LeetCode 251 - Flatten 2D Vector.

## Problem

Design an iterator to flatten a 2D vector and return its elements one by one.

For example:

Input:
[[1, 2], [3], [4, 5, 6]]

Output:
1, 2, 3, 4, 5, 6

## Approach

I used two variables to keep track of the current row and column.

The `move()` function skips empty rows and moves to the next available element.

The `next()` function returns the current element and moves forward.

The `hasNext()` function checks whether another element is available.

## Complexity

- Time: O(1) amortized per operation
- Space: O(1)

## Language

Python

## Key Learning

This problem helped me understand how to maintain iterator state while working with a 2D list.

It also improved my understanding of:

- Iterators
- Two pointers
- Nested lists
- Handling empty rows
- Maintaining state between function calls

## Conclusion

A simple iterator-based approach can flatten the 2D vector without creating a separate flattened array.

## Author

T.Nandhini
