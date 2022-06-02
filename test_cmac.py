import cmac_module

key = 0x2b7e151628aed2a6abf7158809cf4f3c.to_bytes(16, "big")
# m = 0x6bc1bee22e409f96e93d7e117393172a.to_bytes(16, 'big')
m = 0x6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e5130c81c46a35ce411.to_bytes(40, 'big')
print(hex(int(cmac_module.CMAC(key, m, 128),2))[2:])