def compare_number(num_list, num=1):
    return any(
        num_list[i] == num for i in range(len(num_list))
    )


if __name__ == '__main__':
    assert compare_number([1, 3, 9, 4], -1) == False
    print(compare_number([1, 2, 3, 4], 2))