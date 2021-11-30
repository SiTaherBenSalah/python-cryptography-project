import base64
from Crypto.Cipher import AES
from Crypto import Random

def ae(k) :
   if k=="" :
     return "No Text detected "
   else :
    block=16
    Padding='*'
    p=lambda s:s+(block-len(s) %block)*Padding
    KEY=Random.new().read(16)
    IV=Random.new().read(16)
    E=AES.new(KEY,AES.MODE_CBC,IV)
    Encrypted_msg=base64.b64encode( E.encrypt(p(k).encode('utf-8')))
    return Encrypted_msg



