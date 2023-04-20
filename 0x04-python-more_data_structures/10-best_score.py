#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        b = max(list(a_dictionary.values()))
        for k, v in a_dictionary.items():
            if v == b:
                return k
    else:
        return None
