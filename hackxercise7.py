from collections import Counter


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def is_english(s):
    new_s = s
    if not is_ascii(s):
        new_s = ''.join([i for i in s if i.isalpha()])

    three_most_common_letters = Counter(new_s).most_common(3)
    mapped_letters = dict(three_most_common_letters)

    six_most_frequent_letters_in_english = ['e', 't', 'a', 'o', 'i', 'n']
    three_most_common_letters_as_set = set(mapped_letters.keys())
    intersection = three_most_common_letters_as_set.intersection(six_most_frequent_letters_in_english)

    return len(list(intersection)) > 0
