def permute1(start, rest):
    res = []
    if len(rest) <= 1:
        res += [start + rest, rest + start]
    else:
        for i, c in enumerate(rest):
            s = rest[:i] + rest[i+1:]
            for perm in permute1(c, s):
                res += [start + perm]
    return res



print(permute1('', 'google'))