all: 
	chmod +x aes-encrypt.py
	chmod +x aes-decrypt.py

encrypt: 
	./aes-encrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=data/plain out=data/enc

decrypt: 
	./aes-decrypt.py key=FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF mode=ecb in=data/enc out=data/dec