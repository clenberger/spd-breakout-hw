def find_duplicates(num_arr):
    dict = {}
    for num in num_arr:
        if num in dict:
            return True
        else:
            dict[num] = 1
    return False


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 8]
    print(find_duplicates(test_arr))