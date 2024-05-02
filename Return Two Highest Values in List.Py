def two_highest(arg1):
    if len(arg1) <= 0:
        return []
    arg1.sort(reverse=True)
    x = arg1[0]
    for i in arg1:
        if x != i:
            return [x, i]
    return [x]
