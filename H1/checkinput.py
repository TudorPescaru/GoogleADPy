#!/usr/bin/env python


def hasNumbers(str):
    return any([char.isdigit() for char in str])


def hasLetters(str):
    return any([char.isalpha() for char in str])


def main():
    while True:
        name = input('Please enter a name: ')
        if hasNumbers(name):
            print('Name is invalid')
            continue
        else:
            break
    while True:
        inp = input('Input anything ("quit" exits the app): ')
        if inp == "quit":
            break;
        elif hasNumbers(inp) is False:
            print('Sirul de caractere a fost gasit de %s' %(name))
            continue
        elif hasLetters(inp) is False:
            print('Sirul de numere a fost gasit de %s' %(name))
            continue
        else:
            print('Sirul mixt a fost gasit de %s' %(name))
            continue


if __name__ == "__main__":
    main()

