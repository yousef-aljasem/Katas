def find_needle(haystack):
    for position, value in enumerate(haystack):
        if value == "needle":
            return "found the needle at position " + str(position)
