'''Solution to Q6'''

def round_up(value, pass_mark):
    if value <= pass_mark:
        return value
    nearest_multiple = 5 * round(value/5)
    if (nearest_multiple < value):
        return value
    if (nearest_multiple - value >= 3):
        return value
    return nearest_multiple

def main():
    marks = [27,39,71,52,63,73,83,65, 56, 67]
    sorted_marks = sorted(marks)
    # print('Sorted marks ==> ', sorted_marks)
    rounded_marks = []
    for mark in sorted_marks:
        rounded_marks.append(round_up(mark, pass_mark=38))
    # print('Rounded marks ==> ', rounded_marks)

if __name__ == "__main__":
    main()
