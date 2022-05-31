import cmac_module

key = 0x2b7e151628aed2a6abf7158809cf4f3c.to_bytes(16, "big")
cmac_module.SUBK(key)