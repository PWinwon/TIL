def only_square_area(sqare1, sqare2):
    result = []
    for w in sqare1:
        for h in sqare2:
            if w == h:
                result.append(w*h)
    return result



print(only_square_area([32, 55, 63], [13, 32, 40, 55]))