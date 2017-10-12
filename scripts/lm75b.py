import smbus

i2c = smbus.SMBus(1)
lm75b_address = 0x48

block = i2c.read_i2c_block_data(lm75b_address, 0x00, 2)
val = block[0] << 8
val = val | block[1]
if(val >= 0x7fff):
    val = val - 0xffff
result = ((val >>5) * 0.125)

print("Temperature:%6.2f" % result)
