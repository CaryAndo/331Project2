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

    left = sort_me[:len(sort_me)//2]
    right = sort_me[len(sort_me)//2:]

    left = mergesort(left)
    right = mergesort(right)

    if left[-1] <= right[0]:
        left += right
        return left
    print("merging" + str(left))
    print("and" + str(right))
    result = merge(left, right)
    print("result: " + str(result))
    return result


if __name__ == '__main__':
    test = [1, 9, 5, 3, 7, 3, 2, 4, 4]
    toby = mergesort(test)
    print(toby)