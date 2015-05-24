import random
import math


def merge(left, right):
    """ Merge two arrays """
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    if len(left) > 0:
        result.extend(left[left_index:])
    if len(right) > 0:
        result.extend(right[right_index:])
    return result


def mergesort(sort_me):
    """ Sort an array """
    if len(sort_me) <= 1:
        return sort_me

    left = sort_me[:len(sort_me) // 2]
    right = sort_me[len(sort_me) // 2:]

    left = mergesort(left)
    right = mergesort(right)

    if left[-1] <= right[0]:
        left += right
        return left
    result = merge(left, right)
    return result


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def partition1(array, left=0, right=0):
    if right == 0:
        right = len(array) - 1
    i = left
    j = right
    pivot = array[left + ((right - left) // 2)]
    # pivot_index = random.randint(left, right)
    #pivot = array[pivot_index]
    #print('Pivot index = ' + str(pivot_index))
    print('Picked pivot = ' + str(pivot))
    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            swap(array, i, j)
            i += 1
            j -= 1
    return i


def quicksort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)


def quick_sort_helper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        quick_sort_helper(alist, first, split_point - 1)
        quick_sort_helper(alist, split_point + 1, last)


def partition(alist, first, last, pivot_position=0):
    swap(alist, first, pivot_position)
    pivot = alist[first]

    i = first + 1
    j = last

    finished = False
    while not finished:
        while i <= j and alist[i] <= pivot:
            i += 1
        while alist[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            finished = True
        else:
            temp = alist[i]
            alist[i] = alist[j]
            alist[j] = temp
    swap(alist, first, j)
    return j


def partition2(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    swap(arr, pivot_index, right)
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, store_index, i)
            store_index += 1
    swap(arr, right, store_index)
    return store_index


def quickselect(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_index = left + math.floor(random.randint(0, right-left))
    pivot_index = partition2(arr, left, right, pivot_index)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, right, k)
#    if left == right:
#        return arr[left]
#    while True:
#        pivot_index = partition(arr, left, right)
#        if k == pivot_index:
#            return arr[k]
#        elif k < pivot_index:
#            right = pivot_index - 1
#        else:
#            left = pivot_index + 1


if __name__ == '__main__':
    test = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #print('posit: ' + str(partition(test, 0, len(test)-1)))
    #print(test)
    print('THE KTH ELEMENT IS' + str(quickselect(test, 0, len(test)-1, 0)))
    #print(quickselect(alist, 2))
    print('\n\nsorted: ' + str(mergesort(test)))