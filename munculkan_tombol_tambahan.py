import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Tombol Tambahan Termux cok ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By: DonnyC ')
print('\t no: 085156576976 ')
print('\t ig: @donnydcx')
print('\t Github : https://github.com/donnycah')
print(a+'+'*40)
print('\nProses...sabar...cokkk....')
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success cok.. !')
sleep(1)
print(b+'\n[!] menambahkan File Tambahan..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Memproses  !')
sleep(1)
print(b+'\n[!] Tunggu Sebentar')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^'+c+'\n\nhubungi : saya lewat Web atau Fanspage Facebook*\n\n')
