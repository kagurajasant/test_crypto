from MP_module import Miyaguchi_Preneel
from aes_module import AES_ECB

K = '000102030405060708090a0b0c0d0e0f'
C = '010153484500800000000000000000b0'
i = K+C
print("i:",i)
key = 0 
o = AES_ECB(key.to_bytes(16, 'big'))
out = o.encrypt(int(K,16).to_bytes(16, 'big'))
out_xor = int(out.hex(), 16) ^ int(K,16)
o = AES_ECB(out_xor.to_bytes(16,'big'))

out = o.encrypt(int(C,16).to_bytes(16, 'big'))
print(out.hex())

