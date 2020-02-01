"""
Author: Atharva Muley
Date: Jan 30 2020
"""
def bubble_sort(A):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if (A[i] > A[j]):
                A[i], A[j] = A[j], A[i]
    return A
if __name__ == "__main__":
    assert(bubble_sort([1,3,5,2,4]) == [1,2,3,4,5])
    assert(bubble_sort([5,3,1,2,4]) == [1,2,3,4,5])