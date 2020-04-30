#!/usr/bin/env python

import os
import sys
import importlib


def main():
    assignments = [file[:-3] for file in os.listdir() if ".py" in file]
    assignments.remove("homework")

    for assignment in assignments:
        print(">> Running %s" %(assignment))
        module = importlib.import_module(assignment)
        module.main()

    print(">> Done")


if __name__ == "__main__":
    main()

