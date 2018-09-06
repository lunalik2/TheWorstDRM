import time
import urllib.request
import urllib.parse
import re
import os
import winreg
from Cryptodome.Cipher import Salsa20

#HTML Parsing Function
try:
    url = "https://docs.google.com/document/d/1vY3dPMv4OQbnNMm3MjGBUoJKtg1y9O6Z5mn89kq6QmY/view"
    values = {}
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8') # data should be bytes
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    
    saveFile = open('data.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except:
    print("No internet :(")
    time.sleep(2)
    exit()

f = open('data.txt','r')
message = f.read()
key = (message) 
result = re.search('" content="Key:(.*):Key"><meta name="google"', key)
key = str(result.group(1))
f.close()
os.remove("data.txt")

answer = input("What is your activation key?\n\n")

if answer == key:
    print("\nValid!")

else:
    print("\nKill yourself ;)")
    time.sleep(2)
    exit()

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
 
print('\nProduct ID = ' + productid)

#Windows Product ID Encrypting Function
plaintext = productid.encode()

secret = b'420TrumpSucks420'
cipher = Salsa20.new(key=secret)
msg = cipher.nonce + cipher.encrypt(plaintext)
f = open('data.json', 'wb')
f.write(msg)
f.close()
if os.path.exists('data.bin'):
    os.remove('data.bin')
os.rename('data.json', 'data.bin')

time.sleep(5)
