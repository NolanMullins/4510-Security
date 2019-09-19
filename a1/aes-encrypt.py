#!/usr/bin/python3

import sys
from OpenSSL import SSL 

if __name__ == "__main__":
	if (len(sys.argv) <= 4):
		print("please provide key=<128-bit key>, mode=ecb|cbc, in=<input file>, and out=<output file>")
		exit(0)

	print("key: " + sys.argv[1])
	print("mode: " + sys.argv[2])


	