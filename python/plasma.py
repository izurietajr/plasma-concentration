import sys
from math import factorial, exp
import matplotlib.pyplot as plt

def main():


    kab = float(sys.argv[1])
    kel = float(sys.argv[2])
    cdrag = float(sys.argv[3])
    kaberr = float(sys.argv[4])
    kelerr = float(sys.argv[5])
    cdragerr = float(sys.argv[6])
    eerr = float(sys.argv[7])


    # cudstom_e = custom_exponential(kab, eerr)
    p_concentration = plasma_concentration(kab, kel, cdrag, kaberr, kelerr, cdragerr, eerr)
    # x = range(10)
    # plt.plot(x, [custom_exponential(q, 0.001) for q in x])
    # plt.plot(x, [exp(q) for q in x], 'r')
    # plt.show()
    print(p_concentration)

def plasma_concentration(kab, kel, cdrag, kaberr, kelerr, cdragerr, eerr):
    return 1.224

def custom_exponential(num, error):
    flag = True
    count = 0
    e_calculado = (num**count)/factorial(count)
    count = count + 1
    while flag:
        e_parcial =  e_calculado + (num**count)/factorial(count)
        err = relative_error(e_calculado, e_parcial)
        e_calculado = e_parcial
        count = count + 1
        if err < error:
            flag = False
    return e_calculado  #, err

def relative_error(num1, num2):
    return abs(num1-num2)/num1

if __name__ == '__main__':
    main()
