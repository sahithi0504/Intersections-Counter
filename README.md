# Intersection Counter

This program counts the number of intersections between chords in a circle. 

## Algorithm

Explanation of how the intersection counting algorithm works:
- The input consists of two parallel lists - one with radian values, one with start/end identifiers

- The algorithm loops through each possible pair of chords

- For each chord pair:

  - It extracts the start and end radian values
  - It checks if the start of chord 1 is between the start and end of chord 2
  - And vice versa - if the start of chord 2 is between the start and end of chord 1
  - If both of these overlap conditions are true, it increments an intersection counter

- After checking all chord pairs, the total intersection count is returned

The key points:

- Nested loops to check every chord pair
- Extracting start and end radians for each pair  
- Checking for overlap between start/end points of the chords
- Counting intersections when overlap conditions are met

## Usage

To use the program:

1. Run the Python file
2. When prompted, enter the input in the format:

```
[(0.9, 1.2, 1.5, 1.7), ('s1', 's2', 'e1', 'e2')] 
```

- List 1 contains the radian measures in ascending order
- List 2 identifies whether each radian is a start or end point

3. The program will print out intersections found and total count.

## Runtime Analysis

The algorithm has a runtime complexity of O(N^2) due to the nested loops iterating through each pair of chords to check for intersections. 

Specifically:

- There are N chords 
- We loop through the chords with index i from 0 to N
- For each i, we loop through the chords again with index j from i+1 to N
- This results in N * (N-1) / 2 iterations of the inner loop 
- Therefore, the overall runtime is O(N^2)

