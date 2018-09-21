import struct

def readMagic(f):
    return f.read(4).decode("ascii")

def readUint32(f):
    return struct.unpack('<L', f.read(4))[0]

with open('RivalsofAether.exe', 'rb') as f:
    s = f.read()

    last = -1
    current = s.find(b'GEN8')
    while current != -1:
        last = current
        current = s.find(b'GEN8', current + 1)

    if last != -1:
        f.seek(last - 4, 0)
        size = readUint32(f)
        f.seek(last - 8, 0)
        fileBytes = f.read(size + 8)

with open('data_extracted.win', 'wb') as f:
    f.write(fileBytes)
    