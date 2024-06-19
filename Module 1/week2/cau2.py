def char_count(string):
    counter = {}
    for char in string:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1

    return counter

if __name__ == "__main__":
    assert char_count("Baby") == {"B": 1, "a": 1, "b": 1, "y": 1}
    print(char_count("smiles"))  # {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}