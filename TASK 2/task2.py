import numpy as np
import time

start = time.time()
m, n = 1000,1000
mat = np.ones((m, n))
# for i in range(m):
#     for j in range(n):
#         mat[i, j] = int(input(f"Enter value mat[{i}][{j}] : "))

end = time.time()
elapsed=end-start
print("Time taken for creation : ", elapsed)

mat_bytes = mat.tobytes()
mat_int = np.frombuffer(mat_bytes, dtype=mat.dtype).reshape(m, n)

print("Matrix : \n", mat)
print("Matrix->Bytes : \n", mat_bytes)
print("Bytes->Matrix : \n", mat_int)
