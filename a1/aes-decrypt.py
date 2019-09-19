#!/usr/bin/python3

import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


if __name__ == "__main__":
	if (len(sys.argv) <= 4):
		print("please provide key=<128-bit key>, mode=ecb|cbc, in=<input file>, and out=<output file>")
		exit(0)

	args = {}
	for arg in sys.argv:
		if arg.find('=') > 0:
			pair = arg.split('=')
			args[pair[0]] = pair[1]

	inputData = open(args['in'], "rb")
	contents = b"".join(inputData.readlines())

	if args['mode'] == "ecb":
		cipher = AES.new(args['key'].encode("utf-8"), AES.MODE_ECB)
	else:
		cipher = AES.new(args['key'].encode("utf-8"), AES.MODE_CBC, b'\xb4\xb7\xf1\x9aT\xa4D\xcf1\xcaV\x0fo\xfa\x98\xc6')

	dec = cipher.decrypt(contents)
	plainText = unpad(dec, AES.block_size).decode("utf-8")
	with open(args['out'], "w") as outData:
		outData.write(plainText)

	