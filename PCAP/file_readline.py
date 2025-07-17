from os import strerror

try:
    c_count = l_count = 0
    contents = open('text.txt', 'rt')
    line = contents.readline()
    while line != '':
        l_count += 1
        for ch in line:
            c_count += 1
            print(ch, end='')
        line = contents.readline()
    contents.close()
    print("\n\nNumber of lines:", l_count)
    print("Number of characters:", c_count)
except IOError as e:
    print("Couldn't open file:", strerror(e.errno))
