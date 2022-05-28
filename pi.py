#Leibniz forumula

from cmath import pi


def calculatePi(terms):
    denominator = 1
    operation = -1
    pi = 0
    for _ in range(0, terms):
        pi += operation * 4/denominator
        denominator += 2
        operation *= -1
    return pi

print(calculatePi(100000000000000000000))