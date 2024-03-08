def binary_array_to_number(arr):
    binary = ""
    for item in arr:
        binary += str(item)
    return bin(int(binary))


print(binary_array_to_number([0, 0, 0, 1]))
