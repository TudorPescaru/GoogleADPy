#!/usr/bin/env python


def main():
    x = input('Please input an integer: ')
    if x.isdigit() is False:
        print('That is not a valid input')
    else:
        print('This number is %s' %('even' if int(x) % 2 == 0 else 'odd'))


if __name__ == "__main__":
    main()

