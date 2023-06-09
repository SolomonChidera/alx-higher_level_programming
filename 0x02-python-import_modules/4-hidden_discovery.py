#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    all_names = dir(hidden_4)
    for names in all_names:
        if (names[0:2] != "__"):
            print(names)
