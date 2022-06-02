from MP_module import Miyaguchi_Preneel

K = '000102030405060708090a0b0c0d0e0f'
C = '010153484500800000000000000000b0'
i = int(K+C,16).to_bytes(32, 'big') 
print(Miyaguchi_Preneel(i))

