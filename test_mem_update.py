from aes_module import AES_CBC, AES_ECB
from kdf_module import KDF
from cmac_module import CMAC


K_auth = int('000102030405060708090a0b0c0d0e0f', 16).to_bytes(16, 'big')
KEY_UPDATE_ENC_C = int('010153484500800000000000000000b0', 16).to_bytes(16, 'big')
KEY_UPDATE_MAC_C = int('010253484500800000000000000000b0', 16).to_bytes(16, 'big')
K_new = int('0f0e0d0c0b0a09080706050403020100', 16).to_bytes(16, 'big')
UID = '000000000000000000000000000001'
ID = '4' 
AuthID = '1' 
CID = '0000001'
FID = '0'
m1 = UID+ID+AuthID

K1 = KDF(K_auth, KEY_UPDATE_ENC_C)
print("K1:", K1)
K2 = KDF(K_auth, KEY_UPDATE_MAC_C)
print("K2:", K2)


m2_in = int(CID + "0"*25 + K_new.hex(), 16).to_bytes(32, 'big')

o = AES_CBC(int(K1, 16).to_bytes(16, 'big'), int(0).to_bytes(16, 'big'))
m2 = o.encrypt(m2_in)
print("m2:",m2.hex())

m_add = bytearray(int(m1,16).to_bytes(16, 'big')) + bytearray(m2)
m3 = CMAC(int(K2, 16).to_bytes(16, 'big'), m_add, 128)
print("m3:",hex(int(m3,2))[2:])

K3 = KDF(K_new, KEY_UPDATE_ENC_C)
print("K3:", K3)
K4 = KDF(K_new, KEY_UPDATE_MAC_C)
print("K4:", K4)

ecb_obj = AES_ECB(int(K3, 16).to_bytes(16, 'big'))
print('K3:',int(K3, 16).to_bytes(16, 'big'))
m4_tail_before_enc = CID+'8'+'0'*(31-len(CID))
print('m4_tail_bef:',m4_tail_before_enc)
m4_tail = ecb_obj.encrypt(int(m4_tail_before_enc, 16).to_bytes(16, 'big')).hex()
print('m4_tail:',m4_tail)
m4 = UID+ID+AuthID+m4_tail
print("m4:", m4)
m5 = CMAC(int(K4,16).to_bytes(16, 'big'), int(m4,16).to_bytes(32, 'big'), 128)

print("m5:", hex(int(m5,2))[2:])