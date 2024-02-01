import math

def count_intersections(radians_input):
    # Extract start and end lists from the input tuple
    start = radians_input[0]
    end = radians_input[1]

    # Get the number of chords
    n = len(start)
    count = 0

    # Output the input for verification
    print("Start points:", start)
    print("End points:", end)

    # Iterate through each chord
    for i in range(n):
        # Extract starting point and convert to float
        start_float_i = start[i]
        # Extract ending point, remove the first character ('s' or 'e'), and convert to float
        end_float_i = float(end[i][1:])

        # Compare with other chords
        for j in range(i + 1, n):
            # Extract starting point and convert to float
            start_float_j = start[j]
            # Extract ending point, remove the first character ('s' or 'e'), and convert to float
            end_float_j = float(end[j][1:])

            # Check for intersection inside the circle
            if (start_float_i < start_float_j < end_float_i or start_float_i < end_float_j < end_float_i) \
                    and (end_float_i > start_float_j > start_float_i or end_float_i > end_float_j > start_float_i):
                # Increment the intersection count and print details
                count += 1
                print("Intersection between", i, "and", j)

    # Output the total number of intersections
    print("Total intersections:", count)

    return count

# Example usage:
user_input = input("Enter the radians input in two parallel lists : ")
radians_input = eval(user_input)  # Use eval to convert the input string to a tuple

# Call the function with user inputs
count_intersections(radians_input)
