#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    return True
