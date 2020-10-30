"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
"""


def solution(seq, breakers):
    res = []
    for line in seq.splitlines(False):
        for breaker in breakers:
            line = line.split(breaker, 1)[0]
        res.append(line.strip())
    return "\n".join(res)
