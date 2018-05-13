import sys
import random
import math

def main ():
 print "Welcome to a game of darts. This will approximate Pi."
 n = 1000000
 points = random_points(n)
 count = in_circle(points)
 approximate_Pi = Pi(count, n)
 percentage_error = error(approximate_Pi)
 print "Appoximate Pi is:", approximate_Pi, "and the real Pi is:", math.pi
 print "The percentage error is:", percentage_error

def random_points(n):
    """Returns n random points in square centered at origin (0, 0)"""
    points = []
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        points.append((x, y))
    return points

def in_circle(points):
    """Counts points inside circle"""
    n_count = 0
    for p in points:
        x = p[0]
        y = p[1]
        r = math.sqrt((x*x)+(y*y))
        if r <= 1:
            n_count += 1
        else:
            pass
    return n_count

def Pi(n_inside, n_total):
    """Calculates Pi from number of points inside circule divided by total number of points"""
    pi = (float(n_inside) / float(n_total)) * 4.0
    return pi

def error(approximate_Pi):
    percentage_error = ((approximate_Pi - math.pi) / math.pi) * 100
    return abs(percentage_error)

main()
