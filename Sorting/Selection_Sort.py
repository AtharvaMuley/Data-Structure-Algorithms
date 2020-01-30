def selection_sort(A):
    for i in range(len(A)-1):
        min_index = i
        for j in range(i+1, len(A)):
            if (A[min_index] > A[j]):
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

if __name__ == "__main__":
    assert(selection_sort([1,3,5,2,4]) == [1,2,3,4,5])
    assert(selection_sort([5,3,1,2,4]) == [1,2,3,4,5])