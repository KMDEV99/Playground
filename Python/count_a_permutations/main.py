from timeit import timeit
from sys import getrecursionlimit

# test_input = "abb" + "b" * 1000 + "bbab" + "b" * 100 + "ab"
test_input = "ababab"


def split_string(text, a_amount):
    if len(text) < 3:
        return 0
    for i in range(1, len(text)):
        start = text[0:i]
        end = text[i:]
        yield start, end
        if start.count('a') == a_amount:
            for split in split_string(end, a_amount):
                result = [start]
                result.extend(split)
                yield result


def permute(s, a_amount):
    result = [[s]]
    for i in range(1, len(s)):
        first = [s[:i]]
        rest = s[i:]
        if first[0].count('a') == a_amount:
            for p in permute(rest, a_amount):
                result.append(first + p)
    return result


def permute_return():
    res = 0
    a_amount = test_input.count('a') / 3
    res_table = permute(test_input, a_amount)
    for string in res_table:
        if len(string) == 3:
            res += 1
    print("Permutations: %s" % res)


def permute_yield():
    res = 0
    a_amount = test_input.count('a') / 3
    for string in split_string(test_input, a_amount):
        if len(string) == 3 and not [i for i in string if i.count('a') != a_amount]:
            res += 1
    print("Permutations: %s" % res)


if __name__ == "__main__":
    print("Current recursion limit: %s" % getrecursionlimit())  # LIFO
    print("\n\t\tYield:")
    print("Time:", timeit("permute_yield()", setup="from __main__ import permute_yield", number=1))
    print("\n\t\tReturn:")
    print("Time:", timeit("permute_return()", setup="from __main__ import permute_return", number=1))
