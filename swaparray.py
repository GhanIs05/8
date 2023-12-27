import numpy as np
# Define a sample 2D array (replace this with your own array)
original_array = np.array([[1, 2, 3],
[4, 5, 6],
[7, 8, 9]])
# Swap rows and columns in reverse order
swapped_array = original_array[::-1, ::-1]
# Print the original and swapped arrays
print("Original Array:")
print(original_array)
print("\nSwapped Array:")
print(swapped_array)
