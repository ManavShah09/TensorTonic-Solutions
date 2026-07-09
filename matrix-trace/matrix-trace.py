import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    matrix = np.asarray(A, dtype = float)
    return float(np.sum(np.diag(matrix)))
