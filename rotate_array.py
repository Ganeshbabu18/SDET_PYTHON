def rotate_array(arr, k):

    n = len(arr)
    k = k % n
    arr[:n - k] = arr[:n - k][::-1]
    arr[n - k:] = arr[n - k:][::-1]
    arr[:] = arr[::-1]

    return arr

arr = [1, 2, 3, 4, 5]
k = 2

rotated_arr = rotate_array(arr, k)

print(rotated_arr)

# Output: [4, 5, 1, 2, 3]
