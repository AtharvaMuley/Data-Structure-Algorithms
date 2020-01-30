
def recursive_bubble_sort(A):
    if (len(A) == 1):
        return A
    else:
        for i in range(len(A)-1):
            if (A[i] > A[i+1]):
                A[i], A[i+1] = A[i+1], A[i]
        return recursive_bubble_sort(A[0:-1]) + A[-1:]

if __name__ == "__main__":
    assert(recursive_bubble_sort([1,3,5,2,4]) == [1,2,3,4,5])
    assert(recursive_bubble_sort([5,3,1,2,4]) == [1,2,3,4,5])