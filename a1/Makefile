all: 
	chmod +x aes-encrypt.py
	chmod +x aes-decrypt.py

encrypt: 
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=gcm in=data/plain out=data/enc header=TestHeader

decrypt: 
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=gcm in=data/enc out=data/dec header=TestHeader