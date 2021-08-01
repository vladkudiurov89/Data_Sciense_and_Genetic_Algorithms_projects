# Given an array integers 'nums', sort in ascending order


class Solution:
    # Function to sort a list using quick sort algorithm
    def quick_Sort(self, arr, start, end):
        if start < end:
            pi = self.partition(arr, start, end)
            self.quick_Sort(arr, start, pi - 1)
            self.quick_Sort(arr, pi + 1, end)

    @staticmethod
    def partition(arr, start, end):
        i = start - 1
        pivot = arr[end]
        for j in range(start, end):
            if arr[j] < pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[end] = arr[end], arr[i + 1]
        return i + 1

    # @quickSort
    @staticmethod
    def quickSort(arr):
        def helpner(head, tail):
            if head >= tail:
                return
            l, r = head, tail
            m = (r - l) // 2 + l
            pivot = arr[m]
            while r >= l:
                while r >= l and arr[l] < pivot:
                    l += 1
                while r >= l and arr[r] > pivot:
                    r -= 1
                if r >= l:
                    arr[l], arr[r] = arr[r], arr[l]
                    l += 1
                    r += 1
            helpner(head, r)
            helpner(l, tail)

        helpner(0, len(arr) - 1)
        return arr


# Solution 2
class Solution2(object):

    def result_sor(self, arr):
        self.quick_test_sort(arr, 0, len(arr) - 1)
        return arr

    def quick_test_sort(self, arr, start, end):
        if end <= start:
            return
        i = start + 1
        j = end
        while i <= j:
            while i <= j and arr[i] <= arr[start]:
                i += 1
            while i <= j and arr[j] >= arr[start]:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[start], arr[j] = arr[j], arr[start]
        self.quick_test_sort(arr, start, j - 1)
        self.quick_test_sort(arr, j + 1, end)


# bubble sort O(n**2)
def bubble_sort(arr):
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# selection sort O(n**2)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# insertion sort O(n**2)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        current_el = arr[i]
        while j >= 0 and current_el < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = current_el


# quick sort out place
def quick_sort_op(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[-1]
    less = [el for el in arr[:-1] if el < pivot]
    greater = [el for el in arr[:-1] if el >= pivot]
    return quick_sort_op(less) + [pivot] + quick_sort_op(greater)


# quick sort in place with function partition
def partition(arr, start, end):
    i = start - 1
    pivot = arr[end]
    for j in range(start, end):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort_ip(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort_ip(arr, start, pi - 1)
        quick_sort_ip(arr, pi + 1, end)


# Merge sort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    result, mid = [], int(len(arr) / 2)

    y = merge_sort(arr[:mid])
    z = merge_sort(arr[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z.pop(0))
        else:
            result.append(y.pop(0))

    result.extend(y + z)
    return result


if __name__ == '__main__':
    nums_b = [4, 8, 3, 1, 2]
    nums_s = [4, 8, 3, 1, 2]
    nums_i = [4, 8, 3, 1, 2]
    nums_q = [4, 8, 3, 1, 2]
    nums_p = [4, 8, 2, 1, 3]
    nums_m = [4, 8, 2, 1, 3]

    print(f'Before bubble sort: {nums_b}')
    bubble_sort(nums_b)
    print(f'After bubble sort: {nums_b}\n')

    print(f'Before selection sort: {nums_s}')
    selection_sort(nums_s)
    print(f'After selection sort: {nums_s}\n')

    print(f'Before insertion sort: {nums_i}')
    insertion_sort(nums_i)
    print(f'After insertion sort: {nums_i}\n')

    print(f'Before quick sort out place sort: {nums_q}')
    print(f'After quick sort out place sort: {quick_sort_op(nums_q)}\n')

    print(f'Before quick sort in place: {nums_p}')
    quick_sort_ip(nums_p, 0, len(nums_p) - 1)
    print(f'After quick sort in place sort: {nums_p}\n')

    print(f'Before merge sort: {nums_m}')
    merge_sort(nums_m)
    print(f'After merge sort: {nums_m}\n')
