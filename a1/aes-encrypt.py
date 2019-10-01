#!/usr/bin/python3

import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

if __name__ == "__main__":
	if (len(sys.argv) <= 4):
		print("please provide key=<128-bit key>, mode=ecb|cbc, in=<input file>, and out=<output file>")
		exit(0)

	args = {}
	for arg in sys.argv:
		if arg.find('=') > 0:
			pair = arg.split('=')
			args[pair[0]] = pair[1]

	inputData = open(args['in'], "r")
	contents = "".join(inputData.readlines())
	padded = pad(contents.encode("utf-8"), AES.block_size)
	cipher = None

	if args['mode'] == "ecb":
		cipher = AES.new(args['key'].encode("utf-8"), AES.MODE_ECB)
		enc = cipher.encrypt(padded)
	elif args['mode'] == 'cbc':
		cipher = AES.new(args['key'].encode("utf-8"), AES.MODE_CBC, b'\xb4\xb7\xf1\x9aT\xa4D\xcf1\xcaV\x0fo\xfa\x98\xc6')
		enc = cipher.encrypt(padded)
	else:
		cipher = AES.new(args['key'].encode("utf-8"), AES.MODE_GCM, nonce=b'\xb4\xb7\xf1\x9aT\xa4D\xcf1\xcaV\x0fo\xfa\x98\xc6')
		cipher.update(args['header'].encode("utf-8"))
		enc = cipher.encrypt(contents.encode("utf-8")) 

	print(enc)
	with open(args['out'], "wb") as outData:
		outData.write(enc)

	