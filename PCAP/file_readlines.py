from os import strerror

try:
    c_count = l_count = 0
    contents = open('text.txt', 'rt')
    lines = contents.readlines(10)
    while lines:
        for line in lines:
            l_count += 1
            for ch in line:
                c_count += 1
                print(ch, end='')
        lines = contents.readlines(10)
    contents.close()
    print("\n\nNumber of lines:", l_count)
    print("umber of character", c_count)
except IOError as e:
    print("Couldn't open file:", strerror(e.errno))
