def find_multiples(integer, limit):
    multiple = integer
    arr = []
    while integer <= limit:
        arr.append(integer)
        integer = integer + multiple
    return arr
