#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc"""

    file_names = dir(hidden_4)

    ord_name = sorted(name for name in file_names if not name.startswith("__"))

    for name in ord_name:
        print(name)
