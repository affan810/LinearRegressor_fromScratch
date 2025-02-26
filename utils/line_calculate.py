'''
given 2 points calculates the slop and intercept conneting the two lines
'''


def line_calculate(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if x1 == x2:
        return None, None  # Undefined slope for a vertical line

    # Calculate slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept (c)
    c = y1 - m * x1

    return m, c