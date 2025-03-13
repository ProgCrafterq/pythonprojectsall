#!/usr/bin/python
#############################################################
# Bubblesort for Python                                     #
# by: Dennis Linuz <dennismald@gmail.com>                   #
# Demonstration of a bubble 		                    #
#############################################################

import sys
import time

# Initialize input_array
input_array = []

# Check if arguments are provided
if len(sys.argv) < 2:
    print("\nPlease input list items as arguments")
    print("\nExample: python bubblesort.py <item1> [item2] [item3] [item4] ...")
    sys.exit()

i = 1
while i < len(sys.argv):
    try:
        input_array.append(int(sys.argv[i]))
    except ValueError:
        print(f"Error: {sys.argv[i]} is not a valid number.")
        sys.exit()
    i += 1

# Bubble Sort function
def bubbleSort(array):
    length = len(array)
    result = True
    global count
    while result:
        result = False
        i = 0
        while i < length - 1:
            if array[i] > array[i + 1]:
                # Swap values
                tempVar = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tempVar
                result = True
            i += 1
            count += 1
            print(f"Sorting: {array}")
    return array

count = 0

# Start timing the sort
start_time = time.time()

sorted_array = bubbleSort(input_array)

print("\nSorted after", count, "tries.")
print("Sorted:", sorted_array)
print("---")
print(f"Overall Time: {time.time() - start_time} seconds")
  