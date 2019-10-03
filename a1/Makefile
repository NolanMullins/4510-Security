all: 
	chmod +x aes-encrypt.py
	chmod +x aes-decrypt.py

run-encrypt: 
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=gcm in=data/plain out=data/enc header=TestHeader

run-decrypt: 
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=gcm in=data/enc out=data/dec header=TestHeader

run-encrypt-cbc:
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=cbc in=in_file out=cipher_out_file

run-decrypt-cbc:	
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=cbc in=cipher_out_file out=plain_out_file 

run-encrypt-ecb:
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=in_file out=cipher_out_file

run-decrypt-ebc:	
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=cipher_out_file out=plain_out_file 

run-encrypt-ecb:
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=in_file out=cipher_out_file

run-decrypt-ebc:	
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=cipher_out_file out=plain_out_file 
