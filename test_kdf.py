from kdf_module import KDF

K = '000102030405060708090a0b0c0d0e0f'
C = '010153484500800000000000000000b0'
i = int(K+C,16).to_bytes(32, 'big')
print("i: ",i) 
print(KDF(int(K, 16).to_bytes(16, 'big'), int(C, 16).to_bytes(16, 'big')))

