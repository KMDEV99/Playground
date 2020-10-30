import re

"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
"""


def top_3_words(sentence):
    res = {}
    sentence_fixed = re.findall(r"'?[a-z]+(?:'*[a-z]+)?'?", sentence.lower())

    for word in sentence_fixed:
        try:
            res[word] += 1
        except KeyError:
            res[word] = 0
    return sorted(res, key=res.get, reverse=True)[:3]
