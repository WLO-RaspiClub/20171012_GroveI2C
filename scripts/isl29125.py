import smbus
import time

i2c = smbus.SMBus(1)
address = 0x44

i2c.write_i2c_block_data(address,0x00,[0x46])

time.sleep(0.015)
#RO = i2c.read_byte_data(address,0x00)
#print(str(RO))
i2c.write_i2c_block_data(address,0x01,[0x15,0x00,0x00])
time.sleep(0.1)

block = i2c.read_i2c_block_data(address,0x08,7)

#print('Status:'+str(block[0]))

green = (block[2] << 8 | block[1])
red =   (block[4] << 8 | block[3])
blue =  (block[6] << 8 | block[5])

print('Red:' + str(red))
print('Green:' + str(green))
print('Blue:' + str(blue))
