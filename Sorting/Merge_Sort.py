"""
Author: Atharva Muley
Date: Jan 30 2020
"""
def merge_sort(A):
    if len(A) > 1: 
        m = (len(A))//2
        LH = A[:m]
        RH = A[m:]

        merge_sort(LH)
        merge_sort(RH)

        i = j = k = 0
        while(i < len(LH) and j < len(RH)):
            if (LH[i] < RH[j]):
                A[k] = LH[i]
                i += 1
            else:
                A[k] = RH[j]
                j += 1
            k += 1
        
        while (i < len(LH)):
            A[k] = LH[i]
            i += 1
            k += 1

        while (j < len(RH)):
            A[k] = RH[j]
            j += 1
            k += 1
    
if __name__ == "__main__":
    arr1 = [1,3,5,2,4]
    merge_sort(arr1)
    assert(arr1 == [1,2,3,4,5])
    arr2 = [5,3,1,2,4]
    merge_sort(arr2)
    assert(arr2 == [1,2,3,4,5])