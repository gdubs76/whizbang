'''
### Explanation of Improvements:
1. **Handling Near-Singular Matrices**: The code now checks if the pivot is close to zero, raising a `ValueError` if so.
2. **Improved Pivoting Strategy**: Partial pivoting is implemented to enhance numerical stability.
3. **Efficient Element Elimination**: The inner loop for performing row operations uses NumPy's vectorized operations, improving efficiency.
4. **Back Substitution Optimization**: Back substitution is simplified for readability and performance.
5. **Function Input Validation**: Checks ensure that the matrix dimensions for `A` and `B` are compatible.
6. **Docstring Clarifications**: The docstring has been enhanced to provide clearer parameter descriptions and outcomes.
7. **Returning Solutions**: The function now consistently returns the solution vector while maintaining its integrity.

This implementation is now more robust, efficient, and easier to read, satisfying the original review's suggestions while maintaining the algorithm's core functionality.'''

import numpy as np

def gaussian_elimination(A, B):
    """
    Solves the equation AX = B using Gaussian elimination.
    
    Parameters:
        A (np.ndarray): Coefficient matrix (n x n).
        B (np.ndarray): Constant matrix (n x 1).
        
    Returns:
        np.ndarray: The solution vector X (n x 1).
        
    Raises:
        ValueError: If the matrix A is singular or nearly singular, or if the dimensions of A and B are incompatible.
    """
    
    # Validate input dimensions
    if A.shape[0] != A.shape[1]:
        raise ValueError("Coefficient matrix A must be square.")
    if A.shape[0] != B.size:
        raise ValueError("Dimensions of A and B are incompatible.")
    
    # Augmenting the matrix
    augmented_matrix = np.hstack((A, B.reshape(-1, 1)))
    n = augmented_matrix.shape[0]

    for k in range(n):  # Loop over each row
        # Partial pivoting to find the maximum pivot
        max_row_index = np.argmax(abs(augmented_matrix[k:n, k])) + k
        if abs(augmented_matrix[max_row_index, k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular.")
        
        # Swap the current row with the row of the maximum element
        if max_row_index != k:
            augmented_matrix[[k, max_row_index]] = augmented_matrix[[max_row_index, k]]

        # Row Reduction using NumPy's vectorized operations
        for i in range(k + 1, n):
            factor = augmented_matrix[i, k] / augmented_matrix[k, k]
            augmented_matrix[i, k:] -= factor * augmented_matrix[k, k:]

    # Back Substitution
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ = np.dot(augmented_matrix[i, i + 1:n], X[i + 1:n])
        X[i] = (augmented_matrix[i, -1] - sum_) / augmented_matrix[i, i]

    return X

# Test cases
if __name__ == "__main__":
    # Test 1
    A1 = np.array([[2, 1, -1],
                   [-3, -1, 2],
                   [-2, 1, 2]], dtype=float)
    B1 = np.array([8, -11, -3], dtype=float)
    X1 = gaussian_elimination(A1, B1)
    print(f"Test Case 1 Solution: {X1}")  # Expected: [2, 3, -1]

    # Test 2
    A2 = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [1, 0, 0]], dtype=float)
    B2 = np.array([9, 2, 1], dtype=float)
    X2 = gaussian_elimination(A2, B2)
    print(f"Test Case 2 Solution: {X2}")  # Expected: [1, 1, 2]

    # Test 3
    A3 = np.array([[1, 2],
                   [3, 4]], dtype=float)
    B3 = np.array([5, 11], dtype=float)
    X3 = gaussian_elimination(A3, B3)
    print(f"Test Case 3 Solution: {X3}")  # Expected: [1, 2]

    # Test 4 (No solution case)
    A4 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]], dtype=float)
    B4 = np.array([10, 11, 12], dtype=float)
    try:
        X4 = gaussian_elimination(A4, B4)
        print(f"Test Case 4 Solution: {X4}")
    except Exception as e:
        print(f"Test Case 4 Error: {e}")
