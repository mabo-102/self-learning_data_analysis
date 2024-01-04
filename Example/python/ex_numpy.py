import numpy as np

# 配列の作成
arr = np.array([1, 2, 3, 4, 5])
print("arr:", arr)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("matrix:")
print(matrix)

# 配列の基本的な操作
print("arr shape:", arr.shape)
print("arr ndim:", arr.ndim)
print("arr dtype:", arr.dtype)

# 基本的な演算
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result_sum = a + b
print("Sum of a and b:", result_sum)

result_multiply = a * b
print("Product of a and b:", result_multiply)

# 行列の掛け算
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result_matrix = np.dot(matrix_a, matrix_b)
print("Matrix multiplication result:")
print(result_matrix)

# インデクシングとスライシング
print("Element at index 2 in arr:", arr[2])
print("Slice of arr from index 1 to 4:", arr[1:4])

# 統計関数
data = np.array([1, 2, 3, 4, 5])

mean_value = np.mean(data)
print("Mean value of data:", mean_value)

std_dev = np.std(data)
print("Standard deviation of data:", std_dev)

max_value = np.max(data)
print("Maximum value in data:", max_value)

min_value = np.min(data)
print("Minimum value in data:", min_value)
