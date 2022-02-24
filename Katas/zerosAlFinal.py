'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


def move_zeros(array: list):
    n = len(array)
    array = [a for a in array if a != 0]
    array.extend([0]*(n - len(array)))
    return array


if __name__ == '__main__':
    a = move_zeros([0, 1, 2, 0, 0, 3, 4, 0])
    print(a)
