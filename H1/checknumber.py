#!/usr/bin/env python


def isNumber(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def main():
    x = input('Please input a number: ')
    if isNumber(x) is False:
        print('That is not a valid input')
    elif float(x) == 0:
        print('The number is 0')
    elif float(x) < 0:
        print('Number is negative, absolute value is %f' %(-1 * float(x)))
    elif float(x) < 10:
        print('Number is lower than 10')
    else:
        print('Number is greater than 10')


if __name__ == "__main__":
    main()

