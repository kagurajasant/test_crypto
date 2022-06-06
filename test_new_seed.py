from aes_module import AES_ECB

PRNG_STATE = '41f21213bca0434b3eb3bafcb0a19d74'
PRNG_KEY = 'a1be019264992b2b725a4dd4c7767002'

o = AES_ECB(int(PRNG_KEY, 16).to_bytes(16, 'big'))

PRNG_STATE_new = o.encrypt(int(PRNG_STATE, 16).to_bytes(16, 'big'))

print(PRNG_STATE_new.hex())
