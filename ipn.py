#!/usr/bin/env python

import sys
from functools import reduce

def ip_to_int(s):
    "Convert dotted IPv4 address to integer."
    return reduce(lambda a,b: a<<8 | b, map(int, s.split(".")))

def ipn(fip, sip, mask):
    "Check if fip and sip are in the same network"
    bit = 1 << 31
    for count in range(0, mask):
        if (fip & bit) != (sip & bit):
            return False
        bit = bit >> 1
    return True

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print ("Usage: ipn first_ip second_ip bigger_hamming_weight_mask")
        print ("If these ip are in the same network print \"Ok !\".")
        print ("")
        print ("Example usage:")
        print ("$ ./ipn 10.42.4.2 10.42.4.6 24")
        print ("Ok !")
        sys.exit(0)
    else:
        first_ip = ip_to_int(sys.argv[1])
        second_ip = ip_to_int(sys.argv[2])
        mask = int(sys.argv[3])
        if ipn(first_ip, second_ip, mask):
            print("OK !")
        else:
            print("KO !")
