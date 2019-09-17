import matplotlib.pyplot as plt
import sys
from numpy import arange
from sympy import symbols, diff
from plasma import custom_exponential
from math import exp

def main():

    kab = float(sys.argv[1])
    kel = float(sys.argv[2])
    cdrag = float(sys.argv[3])
    kaberr = float(sys.argv[4])
    kelerr = float(sys.argv[5])
    cdragerr = float(sys.argv[6])
    eerr = float(sys.argv[7])

    graph(kab, kel, cdrag, kaberr, kelerr, cdragerr, eerr)
    # print(p_concentration)

def graph(kab, kel, cdrag, kaberr, kelerr, cdragerr, eerr):
    x = arange(1, 10, 0.1)
    plt.plot(x, [plasma_concentration(kab, kel, cdrag, t, eerr) for t in x])
    plt.plot(x, [plasma_concentration(kab+kaberr, kel+kelerr, cdrag+cdragerr, t, eerr) for t in x], 'r')
    plt.plot(x, [plasma_concentration(kab-kaberr, kel-kelerr, cdrag-cdragerr, t, eerr) for t in x], 'g')
    plt.show()

def plasma_concentration(kab, kel, cdrag, t, eerr):
    assert kab-kel != 0, 'División por cero'
    return cdrag*(kab/(kab-kel))*(exp(-kel*t)-exp(-kab*t))

if __name__ == '__main__':
    main()
