# The Snake — Area Filling
# This challenge is based on the classic videogame "Snake".

# Assume the game screen is an n * n square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

# For example, if n = 7 the game looks something like this:



# In this version of the game, the length of the snake doubles each 
# time it eats food (e.g. if the length is 4, after eating it becomes 8).

# Create a function that takes the side n of the 
# game screen and returns the number of times the snake 
# can eat before it runs out of space in the game screen.

# Examples
# snakefill(3) ➞ 3

# snakefill(6) ➞ 5

# snakefill(24) ➞ 9
# Notes
# The given number will always be a positive integer (there are no exceptions to handle).




# The challenge involves determining how many times a snake can eat food before it runs out of space in a grid of size 
# 𝑛
# ×
# 𝑛
# n×n. The snake starts with a length of 1, and each time it eats, its length doubles.

# Let's break down the problem:

# The total area of the grid is 
# 𝑛
# ×
# 𝑛
# n×n.
# The snake starts with a length of 1.
# Each time the snake eats, its length doubles.
# The snake can eat until its length exceeds the area of the grid.
# Steps to Solve:
# Start with an initial length of 1.
# Double the length after each "eat" action.
# Keep track of the number of times the snake has eaten.
# Stop when the snake's length would exceed the total area of the grid.




def snakefill(n):
    area = n * n
    length = 1
    eats = 0
    
    while length <= area:
        length *= 2
        eats += 1
    
    return eats - 1

# Test cases
print(snakefill(3))  # Output: 3
print(snakefill(6))  # Output: 5
print(snakefill(24))  # Output: 9
