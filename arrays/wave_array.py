
def wave_array(A):
    A = sorted(A)
    for i in range(0, len(A), 2):
        A[i], A[i + 1] = A[i + 1], A[i]
    return A
