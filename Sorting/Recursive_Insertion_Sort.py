"""
Author: Atharva Muley
Date: Jan 30 2020
"""
def recursive_insertion_sort(A, n):
    if (n == 1):
        return A
    else:
        recursive_insertion_sort(A, n-1)
        j = n - 2
        key =  A[n-1]
        while (j>=0 and key < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
    
if __name__ == "__main__":
    assert(recursive_insertion_sort([1,3,5,2,4], 5) == [1,2,3,4,5])
    assert(recursive_insertion_sort([5,3,1,2,4], 5) == [1,2,3,4,5])