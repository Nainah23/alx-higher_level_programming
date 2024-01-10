#!/usr/bin/python3
"""Define a fn that multiplies a matrix"""
def matrix_mul(m_a, m_b):
    """
    Multiplies m_a by m_b

    Args:
        m_a : first matrix
        m_b : second matrix
        
    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if m_a or m_b is not a list of lists
        TypeError: if one element of those list of lists is not an integer or a float
        TypeError: if m_a or m_b is not a rectangle 
        ValueError: if m_a or m_b is empty

    Return:
        resulting matrix from the multiplication
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    b_invert = []
    for x in range(len(m_b[0])):
        n_row = []
        for y in range(len(m_b)):
            n_row.append(m_b[y][x])
        b_invert.append(n_row)
    matrix_n = []
    for row in m_a:
        n_row = []
        for col in b_invert:
            product = 0
            for z in range(len(b_invert[0])):
                product += row[z] * col[z]
            n_row.append(product)
        matrix_n.append(n_row)
    return matrix_n
