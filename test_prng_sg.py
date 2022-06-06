from kdf_module import KDF
from aes_module import AES_ECB
SECRET_KEY = '2b7e151628aed2a6abf7158809cf4f3c'
PRNG_SEED_KEY_C = '010553484500800000000000000000B0'
PRNG_SEED_KEY = KDF(int(SECRET_KEY,16).to_bytes(16, 'big'), int(PRNG_SEED_KEY_C,16).to_bytes(16, 'big'))
PRNG_SEED = '6bc1bee22e409f96e93d7e117393172a'

o = AES_ECB(int(PRNG_SEED_KEY,16).to_bytes(16, 'big'))

PRNG_SEED_new = o.encrypt(int(PRNG_SEED, 16).to_bytes(16, 'big'))

print(PRNG_SEED_new.hex())


# PRNG_SEEDi = ENCECB,PRNG_SEED_KEY(PRNG_SEEDi-1)