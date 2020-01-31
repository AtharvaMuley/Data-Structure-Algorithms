def insertion_sort(A):
    for i in range(1, len(A)):
        j = i - 1
        key = A[i]
        while (j >= 0 and key < A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A
            
if __name__ == "__main__":
    assert(insertion_sort([1,3,5,2,4]) == [1,2,3,4,5])
    assert(insertion_sort([5,3,1,2,4]) == [1,2,3,4,5])