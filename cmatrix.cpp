#include <iostream>
#include <vector>
#include <stdexcept>

/*
1. **`size_t` Usage**: `size_t` is used for loop indices to prevent possible negative values and improve clarity.
2. **Empty Matrix Check**: A dedicated function `IsEmpty` checks for empty matrices before performing operations.
3. **Detailed Error Messages**: Improved error messages provide context about the dimensions of matrices involved in operations.
4. **Const Correctness**: Functions that do not modify the input matrix are properly marked as `const`.
5. **User Input for Matrices**: Added a function `ReadMatrix` to allow users to input matrices from the console.
6. **Consistent Styling**: Enhanced readability through consistent formatting (e.g., spacing in loop increments).
*/

using Matrix = std::vector<std::vector<int>>;

// Function to create a zero matrix
Matrix ZeroMatrix(size_t rows, size_t cols) {
    return Matrix(rows, std::vector<int>(cols, 0));
}

// Function to check if a matrix is empty
bool IsEmpty(const Matrix& mat) {
    return mat.empty() || mat[0].empty();
}

// Function to add two matrices
Matrix AddMatrices(const Matrix& A, const Matrix& B) {
    if (IsEmpty(A) || IsEmpty(B)) {
        throw std::runtime_error("One of the matrices is empty.");
    }
    if (A.size() != B.size() || A[0].size() != B[0].size()) {
        throw std::runtime_error("Matrices have different dimensions: " 
                                   + std::to_string(A.size()) + "x" + 
                                   std::to_string(A[0].size()) + " and " + 
                                   std::to_string(B.size()) + "x" + 
                                   std::to_string(B[0].size()));
    }

    Matrix result = ZeroMatrix(A.size(), A[0].size());
    for (size_t i = 0; i < A.size(); ++i) {
        for (size_t j = 0; j < A[0].size(); ++j) {
            result[i][j] = A[i][j] + B[i][j]; 
        }
    }
    return result; 
}

// Function to multiply two matrices
Matrix MultiplyMatrices(const Matrix& A, const Matrix& B) {
    if (IsEmpty(A) || IsEmpty(B)) {
        throw std::runtime_error("One of the matrices is empty.");
    }
    if (A[0].size() != B.size()) {
        throw std::runtime_error("Matrix dimensions do not allow multiplication: "
                                   + std::to_string(A[0].size()) + " (A columns) vs " + 
                                   std::to_string(B.size()) + " (B rows)");
    }

    Matrix result = ZeroMatrix(A.size(), B[0].size());
    for (size_t i = 0; i < A.size(); ++i) {
        for (size_t j = 0; j < B[0].size(); ++j) {
            for (size_t k = 0; k < B.size(); ++k) {
                result[i][j] += A[i][k] * B[k][j]; 
            }
        }
    }
    return result; 
}

// Function to transpose a matrix
Matrix TransposeMatrix(const Matrix& A) {
    if (IsEmpty(A)) {
        throw std::runtime_error("Matrix is empty.");
    }

    Matrix result = ZeroMatrix(A[0].size(), A.size());  
    for (size_t i = 0; i < A.size(); ++i) {
        for (size_t j = 0; j < A[0].size(); ++j) {
            result[j][i] = A[i][j]; 
        }
    }
    return result;  
}

// Function to print a matrix
void PrintMatrix(const Matrix& mat) {
    for (const auto& row : mat) {
        for (const auto& elem : row) {
            std::cout << elem << " ";
        }
        std::cout << std::endl;
    }
}

// Function to read a matrix from user input
Matrix ReadMatrix() {
    size_t rows, cols;
    std::cout << "Enter number of rows and columns (space-separated): ";
    std::cin >> rows >> cols;
    
    Matrix mat = ZeroMatrix(rows, cols);
    std::cout << "Enter elements row by row:" << std::endl;
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            std::cin >> mat[i][j];
        }
    }
    return mat;
}

// Main function
int main() {
    std::cout << "Enter Matrix A: " << std::endl;
    Matrix A = ReadMatrix();

    std::cout << "Enter Matrix B: " << std::endl;
    Matrix B = ReadMatrix();

    // Perform matrix addition
    try {
        Matrix SUM = AddMatrices(A, B);
        std::cout << "Sum of matrices:" << std::endl;
        PrintMatrix(SUM);
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }

    // Perform matrix multiplication
    try {
        Matrix PRODUCT = MultiplyMatrices(A, TransposeMatrix(B)); // Ensure B is transposed for multiplication
        std::cout << "Product of matrices:" << std::endl;
        PrintMatrix(PRODUCT);
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }

    // Transpose matrix A
    try {
        Matrix TRANSPOSED_A = TransposeMatrix(A);
        std::cout << "Transposed matrix A:" << std::endl;
        PrintMatrix(TRANSPOSED_A);
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl;
    }

    return 0;
}
