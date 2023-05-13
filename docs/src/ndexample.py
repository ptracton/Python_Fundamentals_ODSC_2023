#! /usr/bin/env python3

import numpy as np

vector = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(f"Vector 1D = {vector} {vector.shape}")

vector2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex128)
print(f"Vector 2D = {vector2d}")

vector3d = np.ones((2, 3, 2))  # or np.zeros
print(f"Vector 3D = {vector3d}")

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(f"Add \n{A + B}\n")
print(f"Element Mult \n{A * B}\n")  # elementwise product
print(f"Dot Product \n{A @ B}\n")  # matrix product
print(f"Dot Product Method \n{A.dot(B)}\n")
