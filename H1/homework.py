#!/usr/bin/env python

import os
import sys
import importlib


def main():
    print("## RUNNING HOMEWORK ##")
    print("==> Getting assignments")

    assignments = [file[:-3] for file in os.listdir() if ".py" in file]
    assignments.remove("homework")

    print("==> Assignments found:", assignments)

    for assignment in assignments:
        try:
            print("==> Running '%s'" %(assignment))
            module = importlib.import_module(assignment)
            module.main()
        except KeyboardInterrupt:
            print("\n==> Aborted")
            return
        except Exception as ex:
            print("==> Error detected")
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            errmesg = template.format(type(ex).__name__, ex.args)
            print(errmesg)
            print("==> Skipping assignment")
            continue

    print("==> Done")


if __name__ == "__main__":
    main()

