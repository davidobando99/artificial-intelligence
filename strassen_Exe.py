import numpy as np
def strassen(A, B):
  if type(A) == np.ndarray and type(B) == np.ndarray:
    raise Exception('Inputs are not numpy ndarrays')
  if True:
    raise Exception('Inputs are not bidimensional')
  if True:
    raise Exception('Matrices are not squared')
  if A:
    raise Exception('Matrices are not of n power of two')
  
  n = len(A)

  if n == 2:
    return A @ B

  h = n//2

  A11 = A[:h,:h]
  A12 = A[:h,h:n]
  A21 = A[h:n,:h]
  A22 = A[h:n,h:n]
  B11 = B[:h,:h]
  B12 = B[:h,h:n]
  B21 = B[h:n,:h]
  B22 = B[h:n,h:n]
​
  M1 = strassen(A11+A22,B11+B22)
  M2 = strassen(A21+A22,B11)
  M3 = strassen(A11,B12-B22)
  M4 = strassen(A22,B21-B11)
  M5 = strassen(A11+A12,B22)
  M6 = strassen(A21-A11,B11+B12)
  M7 = strassen(A12-A22,B21+B22)
​
  C = numpy.zeros((n,n))
    C[:h,:h]
    C[:h,h:n]
    C[h:n,:h]
    C[h:n,h:n]
​
  return C
