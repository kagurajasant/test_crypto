from MP_module import Miyaguchi_Preneel

ENTROPY = 'ae2d8a571e03ac9c9eb76fac45af8e51'
PRNG_STATE = '614aae8a7bb8fff31ac3230e6240506b'
PRNG_EXTENSION_C = '80000000000000000000000000000100'
PRNG_SEED = '41f21213bca0434b3eb3bafcb0a19d74'

i = int(PRNG_STATE+ENTROPY+PRNG_EXTENSION_C, 16).to_bytes(48, 'big')
PRNG_STATE_EXT = Miyaguchi_Preneel(i, 0)
i = int(PRNG_SEED+ENTROPY+PRNG_EXTENSION_C, 16).to_bytes(48, 'big')
PRNG_SEED_EXT = Miyaguchi_Preneel(i, 0)

print("PRNG_SEED_EXT: {0},\nPRNG_STATE_EXT: {1}".format(PRNG_SEED_EXT, PRNG_STATE_EXT))
