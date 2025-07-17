from os import strerror
import sys

try:
    fo = open('text_w.txt', 'wt')  # A new file (text_w.txt) is created.
    for i in range(8):
        s = "line #" + str(i+1) + "\n"
        fo.write(s)
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

try:
    f = open('text_w.txt', 'rt')
    for line in f:
        print(line, end='')
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

sys.stderr.write('Error')  # Just a test message
