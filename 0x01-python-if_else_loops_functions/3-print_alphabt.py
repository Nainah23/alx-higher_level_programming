#!/usr/bin/python3
for i in range(97, 123):
    if i in (101, 123):
        continue
    print("{}".format(chr(i)), end='')
