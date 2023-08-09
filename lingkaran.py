#Nama / NIM : Aland Mulia Pratama / 19622296
#Tanggal : 10 Maret 2023

#LuasLingkaran
#Menerima masukkan jari-jari serta menghitung luas lingkaran dengan pembulatan 2 desimal

#KAMUS
#jari_jari : Int
#luas = float

#ALGORITMA
jari_jari = int(input())

if (jari_jari <= 0):
    print("Jari-jari harus > 0")
else:
    luas = (jari_jari**2) * 3.1415
    print('{:.2f}'.format(luas))