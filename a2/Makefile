CC=gcc
CFLAGS= -z execstack -fno-stack-protector

all: file_exists is_log_file buf_exploit env_exploit

file_exists: file_exists.c
	$(CC) -o file_exists file_exists.c $(CFLAGS)

is_log_file: is_log_file.c
	$(CC) -o is_log_file is_log_file.c $(CFLAGS)

%: %.c
	$(CC) -o $* $*.c $(CFLAGS)

clean:
	rm file_exists is_log_file *.log buf_exploit
