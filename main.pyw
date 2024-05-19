from calculator_fraccion.libFraccion import Fraccion
from calculator_fraccion.libFracMix import FracMix


def main():
    a = FracMix(2, 3, 4)
    b = FracMix(3, 1, 2)
    c = FracMix(3, 1, 2)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a == b)
    print(c == b)


if __name__ == '__main__':
    main()
