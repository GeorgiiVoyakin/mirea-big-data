import math


def area_of_shapes() -> None:
    a, h = map(int, input('Введите сторону и высоту треугольника: ').split())
    areas = dict()
    areas['треугольник'] = 1/2 * a * h

    w, h = map(int, input('Введите ширину и высоту прямоугольника: ').split())
    areas['прямоугольник'] = w * h

    r = int(input('Введите радиус круга: '))
    areas['круг'] = math.pi * r ** 2

    print(areas)


def not_calculator() -> None:
    first, second = map(int, input('Введите два числа: ').split())
    operation = input(
        'Введите операцию (+, -, /, //, **), которую необходимо произвести: ')
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        try:
            print(first / second)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    elif operation == '//':
        try:
            print(first // second)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')
    elif operation == '**':
        print(first ** second)


def heron_formula() -> None:
    a, b, c = map(int, input('Введите стороны треугольника: ').split())
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))


def main() -> None:
    area_of_shapes()
    not_calculator()
    heron_formula()


if __name__ == '__main__':
    main()
