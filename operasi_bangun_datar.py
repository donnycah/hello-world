def hitung_L_persegi():
    print("hitung luas persegi")
    sisi_1 = float(input("masukan sisi pertama: "))
    sisi_2 = float(input("masukan sisi kedua: "))
    luas_persegi = sisi_1 * sisi_2
    print('='*30)
    print('luas persegi: ', sisi_1,'x',sisi_2,'=',luas_persegi, "\n")

def hitung_L_persegi_panjang():
    print('hitung luas persegi panjang')
    panjang_1 = float(input('masukan panjang: '))
    lebar_1 = float(input('masukan lebar: '))
    luas_persegi_panjang = panjang_1 * lebar_1
    print('='*30)
    print('luas persegi panjang: ',panjang_1,'x',lebar_1,'=', luas_persegi_panjang, "\n")

def hitung_L_trapesium():
    print('hitung luas trapesium')
    panjang_a = float(input('masukan panjang a: '))
    lebar_b = float(input('masukan lebar a: '))
    tinggi_trapesium = float(input('masukan tinggi: '))
    luas_trapesium = 0.5 * (panjang_a + lebar_b) * tinggi_trapesium
    print('='*30)
    print('luas trapesium: 0.5 x (',panjang_a,'+',lebar_b,') x',tinggi_trapesium,'= ',luas_trapesium, "\n")

def hitung_L_lingkaran():
    print("hitung luas lingkaran")
    jari_jari = float(input("masukan jari jari: "))
    luas_lingkaran = 22/7 * (jari_jari * jari_jari)
    print('='*30)
    print('luas lingkaran: 22/7 x (',jari_jari,'x',jari_jari,') = ', luas_lingkaran, "\n")

def hitung_L_jajargenjang():
    print("hitung luas jajargenjang")
    alas_jajargenjang = float(input("masukan alas: "))
    tinggi_jajargenjang = float(input("masukan tinggi: "))
    luas_jajargenjang = alas_jajargenjang * tinggi_jajargenjang
    print('='*30)
    print('luas jajargenjang: ',alas_jajargenjang,'x',tinggi_jajargenjang,'= ', luas_jajargenjang, "\n")

def hitung_L_layang_layang():
    print('hitung luas layang layang')
    diagonal_a = float(input('masukan diagonal a: '))
    diagonal_b = float(input('masukan diagonal b: '))
    luas_layang_layang = 1/2 * (diagonal_b * diagonal_a)
    print('='*30)
    print('luas layang layang: 0.5 x (',diagonal_a,'x',diagonal_b,') = ', luas_layang_layang, "\n")

def hitung_L_belah_ketupat():
    print('hitung luas belah ketupat')
    diagonal_belah_ketupat_a = float(input('masukan diagonal a: '))
    diagonal_belah_ketupat_b = float(input('masukan diagonal b: '))
    luas_belah_ketupat = 1/2 * (diagonal_belah_ketupat_a * diagonal_belah_ketupat_b)
    print('='*30)
    print('luas belah ketupat: 0.5 x (',diagonal_belah_ketupat_a,'x',diagonal_belah_ketupat_b,') = ', luas_belah_ketupat, "\n")

def hitung_L_segitiga():
    print('hitung luas segitiga')
    alas_segitiga = float(input('masukan alas: '))
    tinggi_segitiga = float(input('masukan tinggi: '))
    luas_segitiga = 1/2 * alas_segitiga * tinggi_segitiga
    print('='*30)
    print('luas segitiga: 0.5 x',alas_segitiga,'x',tinggi_segitiga,'= ', luas_segitiga, "\n")


#while True:
   # userInput = str(input('pilih rumus: \n\nA.Rumus Luas Bangun Datar\nB.Rumus volume Bangun Ruang\nC.Rumus Keliling Bangun Ruang\n\nPilih No Berapa: '))
   # if (userInput == A)
while True:
    userInput = int(input('pilih rumus: \n\n1.hitung luas persegi\n2.hitung luas persegi panjang\n3.hitung luas trapesium\n4.hitung luas lingkaran\n5.hitung luas jajargenjang\n6.hitung luas belah ketupat\n7.hitung luas layang layang\n8.hitung luas segitiga\n\n0.keluar dari program\n\npilih nomor berapa: '))
    if (userInput == 1):
        hitung_L_persegi()
    elif (userInput == 2):
        hitung_L_persegi_panjang()
    elif (userInput == 3):
        hitung_L_trapesium()
    elif (userInput == 4):
        hitung_L_lingkaran()
    elif (userInput == 5):
        hitung_L_jajargenjang()
    elif (userInput == 6):
        hitung_L_belah_ketupat()
    elif (userInput == 7):
        hitung_L_layang_layang()
    elif (userInput == 8):
        hitung_L_segitiga()
    else:
        break

