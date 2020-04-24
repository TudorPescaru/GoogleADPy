#!/usr/bin/env python


def main():
    year = input('Please input a year: ')
    if year.isdigit() is False:
        print('That is not a valid input')
    elif (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        print('This is a leap year')
    else:
        print('This is not a leap year')


if __name__ == "__main__":
    main()

