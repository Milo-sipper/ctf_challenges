from binascii import crc32

correct_crc = int.from_bytes(b'\x9C\x1A\x1A\x01',byteorder='big')

for h in range(4000):
    for w in range(4000):
        crc=b"\x49\x48\x44\x52"+w.to_bytes(4,byteorder='big')+h.to_bytes(4,byteorder='big')+b"\x08\x06\x00\x00\x00"
        if crc32(crc) % (1<<32) == correct_crc:
            print ('FOUND!')
            print ('Width: ',end="")
            print (hex(w))
            print ('Height :',end="")
            print (hex(h))
            exit()