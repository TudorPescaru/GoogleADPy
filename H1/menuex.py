#!/usr/bin/env python

import re


def main():
    menu = """0 - Quit
              1 - Afisare lista de cumparaturi
              2 - Adaugare element
              3 - Stergere element
              4 - Stergere lista de cumparaturi
              5 - Cautare in lista de cumparaturi"""
    menu = re.sub('^\s+', '', menu, flags=re.MULTILINE)
    menulist = menu.split('\n')
    while True:
        print('## Menu options:')
        print(menu)
        inp = input('## Please enter an option: ')
        try:
            inp = int(inp)
        except ValueError:
            print('Alegerea nu exista. Reincercati')
            continue
        if inp in range(1, 6):
            print(menulist[inp].split('-')[1][1:])
        elif inp == 0:
            break
        else:
            print('Alegerea nu exista. Reincercati')


if __name__ == "__main__":
    main()

