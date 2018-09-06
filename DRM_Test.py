from Cryptodome.Cipher import Salsa20
import os
import winreg
import time

if os.path.exists('data.bin'):
    print("Checking legitimacy...\n")

    #Windows Product ID Fetching Function
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        value = winreg.QueryValueEx(key, "DigitalProductId")
    except OSError:
        print(r"""Cannot find value "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId". Try updating Windows.""")
        quit()
     
    assert type(value) is tuple
    assert len(value) == 2
    if value[1] != 3:
        print(r"""Type mismatch in "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\DigitalProductId". Try updating Windows.""")
        quit()
    assert type(value[0]) is bytes
 
    rawdata = list(value[0])
    productid = ""
    for i in range(25):
        cur = 0
        for x in range(14, -1, -1):
            cur = rawdata[x + 52] + cur * 256
            rawdata[x + 52] = (cur // 24) & 255
            cur = cur % 24
        productid = "BCDFGHJKMPQRTVWXY2346789"[cur] + productid
        if ((i + 1) % 5 == 0) and (i != 24):
            productid = '-' + productid
 
    print(productid)

    #Windows Product ID Decrypting Function
    os.rename('data.bin', 'data.json')
    f = open('data.json', 'rb')
    msg = f.read()
    f.close()
    os.rename('data.json', 'data.bin')
    secret = b'420TrumpSucks420'
    msg_nonce = msg[:8]
    ciphertext = msg[8:]
    cipher = Salsa20.new(key=secret, nonce=msg_nonce)
    plaintext = cipher.decrypt(ciphertext)
    #plaintext = plaintext.decode()
    plaintext = str(plaintext)
    plaintext = plaintext[2:]
    plaintext = plaintext[:-1]
    print(plaintext)

    #Legitimacy Test Function
    if productid == plaintext:
        print("\nValid!")
        '''Insert your
            code here'''
    else:
        print("You are pirate :(")

else:
    print("'data.bin' does not exist. Make sure to run DRM Setup before trying again.")

time.sleep(5)
