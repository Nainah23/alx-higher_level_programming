#!/usr/bin/python3
""" multiplies 2 matrices by using the module NumPy"""
def lazy_matrix_mul(m_a, m_b):
    """
    Returns the prod of multiplying 2 matrices
    Args:
        m_a : first matrix
        m_b : second matrix
    """
    return (np.matmul(m_a, m_b))
