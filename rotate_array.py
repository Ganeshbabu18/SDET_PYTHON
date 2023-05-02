def rotate_array(arr, rotations_array):

    length_array = len(arr)
    rotations_array = rotations_array % length_array
    arr[:length_array- rotations_array] = arr[:length_array - rotations_array][::-1]
    arr[length_array - rotations_array:] = arr[length_array - rotations_array:][::-1]
    arr[:] = arr[::-1]

    return arr

arr = [1, 2, 3, 4, 5]
rotations_array = 2

rotated_arr = rotate_array(arr, rotations_array)

print(rotated_arr)

# Output: [4, 5, 1, 2, 3]
