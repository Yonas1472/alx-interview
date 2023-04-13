#!/usr/bin/python3
"""Performs log parsing from stdin"""

import re
import sys

counter = 0
file_size = 0
dict = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

def print_codes(dict, file_s):
    """Prints the status code and the number of times they appear"""
    print("File size: {}".format(file_s))
    for key in sorted(dict.keys()):
        if dict[key] != 0:
            print("{}: {}".format(key, dict[key]))

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            split_string = re.split('- |"|"| " " ', str(line))
            statusC_and_file_s = split_string[-1]
            if counter != 0 and counter % 10 == 0:
                print_codes(dict, file_size)
            counter = counter + 1
            try:
                statusC = int(statusC_and_file_s.split()[0])
                f_size = int(statusC_and_file_s.split()[1])
                if statusC in dict:
                    dict[statusC] += 1
                file_size = file_size + f_size
            except:
                pass
        print_codes(dict, file_size)
    except KeyboardInterrupt:
        print_codes(dict, file_size)
        raise
