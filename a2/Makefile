CC=gcc
CFLAGS= -z execstack -fno-stack-protector -g

all: file_exists is_log_file buf_exploit env_exploit

#sudo chmod u+s file_exsits
file_exists: file_exists.c
	$(CC) -o file_exists file_exists.c $(CFLAGS)

is_log_file: is_log_file.c
	$(CC) -o is_log_file is_log_file.c $(CFLAGS)

%: %.c
	$(CC) -o $* $*.c $(CFLAGS)

perm:
	sudo chmod u+s file_exists \
	&& sudo chmod u+s is_log_file

clean:
	rm file_exists is_log_file *.log buf_exploit env_exploit
