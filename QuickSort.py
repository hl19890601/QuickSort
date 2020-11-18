# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(array, low, high):
    i = (low - 1)         # index of smaller element
    pivot = array[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if array[j] <= pivot:

            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return (i + 1)

# The main function that implements QuickSort
# array[] --> array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort


def quickSort(array, low, high):
    if low < high:

        # pi is partitioning index, array[p] is now
        # at right place
        pi = partition(array, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


if __name__ == '__main__':

    nums = [3, 1, 6, 8, 0]
    quickSort(nums, 0, len(nums) - 1)
    print(nums)
