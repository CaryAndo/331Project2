import random
import math
import time


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


def partition(arr, left, right, pivot_index):
    """ Partition the array relative to the given pivot. This function is in-place and uses O(1) space """
    pivot_value = arr[pivot_index]
    swap(arr, pivot_index, right)  # We use the last element as the pivot placeholder
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, store_index, i)
            store_index += 1
    swap(arr, right, store_index)
    return store_index


def quickselect_recursive(arr, left, right, k):
    """ Algorithm #2: Select the kth element by recursively partitioning the array """
    if left == right:
        return arr[left]
    pivot_index = left + math.floor(random.randint(0, right-left))
    pivot_index = partition(arr, left, right, pivot_index)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect_recursive(arr, left, pivot_index - 1, k)
    else:
        return quickselect_recursive(arr, pivot_index + 1, right, k)


def quickselect_iterative(arr, left, right, k):
    """ Algorithm #2: Select the kth element by iteratively partitioning the array """
    if left == right:
        return arr[left]
    while True:
        pivot_index = left + math.floor(random.randint(0, right-left))
        pivot_index = partition(arr, left, right, pivot_index)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left = pivot_index + 1


def linear_select(arr, k):
    """ Algorithm #3: Use the median-of-medians to select a better pivot to select the kth element """
    if len(arr) <= 5:
        return mergesort(arr)[k]
    else:
        medians = []
        divided = [arr[i:i+5] for i in range(0, len(arr), 5)]  # Divide arr into groups of 5
        for i in divided:
            sorteded = mergesort(i)
            medians.append(sorteded[len(sorteded)//2])
        median_of_medians = linear_select(medians, math.floor(len(medians) / 2))
        val = arr.index(median_of_medians)  # The index of the median of medians
        t = partition(arr, 0, len(arr) - 1, val)
        if k == t:
            return arr[k]
        elif k < t:
            return linear_select(arr[:t], k)
        else:
            return linear_select(arr[t+1:], k - t - 1)


def random_list(n):
    return [random.randint(0, 2000) for i in range(n)]


if __name__ == '__main__':
    test = [54, 26, 93, 17, 77, 31, 44, 55, 20, 3]
    t = [4, 3, 2, 1]
    print(linear_select(t, 3))
    print(quickselect_recursive(t, 0, len(t)-1, 3))
    print(mergesort(t)[3])

    for i in range(1, 10):
        length = 10 ** i
        temp_array = random_list(length)
        print("Array size: " + str(length))
        print("Selecting 1st element")
        a = time.time()
        y = quickselect_recursive(temp_array, 0, len(temp_array)-1, 0)
        b = time.time()
        print("quickselect recursive took: " + str(b - a) + " seconds")
        a = time.time()
        y = quickselect_iterative(temp_array, 0, len(temp_array)-1, 0)
        b = time.time()
        print("quickselect iterative took: " + str(b - a) + " seconds")
        a = time.time()
        z = linear_select(temp_array, 0)
        b = time.time()
        print("MM approach took: " + str(b - a) + " seconds")
        a = time.time()
        x = mergesort(temp_array)[0]
        b = time.time()
        print("Mergesort approach took: " + str(b - a) + " seconds")
        print("")

        if x != y or y != z:
            print("ERROR INCONSISTENT DATA")
            break

        print("Selecting 1/4th element")
        a = time.time()
        y = quickselect_recursive(temp_array, 0, len(temp_array)-1, len(temp_array)//4)
        b = time.time()
        print("quickselect_recursive took: " + str(b - a) + " seconds")
        a = time.time()
        y = quickselect_iterative(temp_array, 0, len(temp_array)-1, len(temp_array)//4)
        b = time.time()
        print("quickselect iterative took: " + str(b - a) + " seconds")
        a = time.time()
        z = linear_select(temp_array, len(temp_array)//4)
        b = time.time()
        print("MM approach took: " + str(b - a) + " seconds")
        a = time.time()
        x = mergesort(temp_array)[len(temp_array)//4]
        b = time.time()
        print("Mergesort approach took: " + str(b - a) + " seconds")
        print("")

        if x != y or y != z:
            print("ERROR INCONSISTENT DATA")
            break

        print("Selecting 1/2 element")
        a = time.time()
        y = quickselect_recursive(temp_array, 0, len(temp_array)-1, len(temp_array)//2)
        b = time.time()
        print("quickselect_recursive took: " + str(b - a) + " seconds")
        a = time.time()
        y = quickselect_iterative(temp_array, 0, len(temp_array)-1, len(temp_array)//2)
        b = time.time()
        print("quickselect iterative took: " + str(b - a) + " seconds")
        a = time.time()
        z = linear_select(temp_array, len(temp_array)//2)
        b = time.time()
        print("MM approach took: " + str(b - a) + " seconds")
        a = time.time()
        x = mergesort(temp_array)[len(temp_array)//2]
        b = time.time()
        print("Mergesort approach took: " + str(b - a) + " seconds")
        print("")

        if x != y or y != z:
            print("ERROR INCONSISTENT DATA")
            break

        print("Selecting 3/4th element")
        a = time.time()
        y = quickselect_recursive(temp_array, 0, len(temp_array)-1, (3*len(temp_array))//4)
        b = time.time()
        print("quickselect_recursive took: " + str(b - a) + " seconds")
        a = time.time()
        y = quickselect_iterative(temp_array, 0, len(temp_array)-1, (3*len(temp_array)//4))
        b = time.time()
        print("quickselect iterative took: " + str(b - a) + " seconds")
        a = time.time()
        z = linear_select(temp_array, (3*len(temp_array))//4)
        b = time.time()
        print("MM approach took: " + str(b - a) + " seconds")
        a = time.time()
        x = mergesort(temp_array)[(3*len(temp_array))//4]
        b = time.time()
        print("Mergesort approach took: " + str(b - a) + " seconds")
        print("")

        if x != y or y != z:
            print("ERROR INCONSISTENT DATA")
            break

        print("Selecting last element")
        a = time.time()
        y = quickselect_recursive(temp_array, 0, len(temp_array)-1, len(temp_array) - 1)
        b = time.time()
        print("quickselect_recursive took: " + str(b - a) + " seconds")
        a = time.time()
        y = quickselect_iterative(temp_array, 0, len(temp_array)-1, len(temp_array) - 1)
        b = time.time()
        print("quickselect iterative took: " + str(b - a) + " seconds")
        a = time.time()
        z = linear_select(temp_array, len(temp_array) - 1)
        b = time.time()
        print("MM approach took: " + str(b - a) + " seconds")
        a = time.time()
        x = mergesort(temp_array)[len(temp_array) - 1]
        b = time.time()
        print("Mergesort approach took: " + str(b - a) + " seconds")
        print("")
