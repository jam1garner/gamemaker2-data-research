import struct

def readMagic(f):
    return f.read(4).decode("ascii")

with open('RivalsofAether.exe', 'r+b') as f:
    s = f.read()

    last = -1
    current = s.find(b'GEN8')
    while current != -1:
        last = current
        current = s.find(b'GEN8', current + 1)

    f.seek(last - 8, 0)
    with open('data_extracted.win', 'rb') as newData:
        f.write(newData.read())

#    48B17304