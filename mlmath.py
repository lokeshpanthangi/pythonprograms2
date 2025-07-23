def dot_product(a, b):
    """
    Calculates the dot product of two vectors a and b.

    Args:
        a (list): A list of numbers representing the first vector.
        b (list): A list of numbers representing the second vector.

    Returns: number: The dot product of the two vectors
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")

    result = 0
    for i in range(len(a)):
        result = result + (a[i] * b[i])
    return result


def matrix_multiply(a, b):
    """
    Multiplies two matrices a and b using standard matrix multiplication rules.

    Args:
        a (list of list): First matrix (2D list).
        b (list of list): Second matrix (2D list).

    Returns: list of list: Result of multiplying a and b.
    """
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    if cols_a != rows_b:
        raise ValueError("Number of columns in first matrix must equal number of rows in second matrix.")

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            value = 0
            for k in range(cols_a):
                value = value + (a[i][k] * b[k][j])
            row.append(value)
        result.append(row)
    return result


def conditional_probability(pairs):
    """
    Calculates the conditional probability P(A=1 | B=1) from (A, B) event pairs.

    Args: pairs (list of tuple): A list of tuples where each tuple has two elements:
                               A (0 or 1), and B (0 or 1)

    Returns: The conditional probability of A=1 given B=1.

    """
    count_b = 0
    count_a_and_b = 0

    for pair in pairs:
        a = pair[0]
        b = pair[1]

        if b == 1:
            count_b = count_b + 1
            if a == 1:
                count_a_and_b = count_a_and_b + 1

    if count_b == 0:
        return 0.0
    else:
        return count_a_and_b / count_b
