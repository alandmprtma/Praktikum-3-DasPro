#Nama / NIM : Aland Mulia Pratama / 19622296
#Tanggal : 10 Maret 2023

#HargaMakanan
#Program menghitung harga makanan berdasarkan masukkan sebuah list berdasarkan ganjil atau genap suatu bilangan.

#KAMUS
# n, sumhargagenap, sumhargaganjil, hargagenap, hargaganjil, jumlah : int
# tabel : List of Integer

#ALGORITMA
n = int(input())
tabel = [0 for i in range(n)]
for i in range (n):
    tabel[i] = int(input())

sumhargagenap = 0
sumhargaganjil = 0
for i in range (n):
    if (tabel[i] == 0):
        harga = 0
    elif (tabel[i] % 2 == 0):
        hargagenap = tabel[i] * 100
        sumhargagenap += hargagenap
    elif (tabel[i] % 2 == 1):
        hargaganjil = tabel[i] * 200
        sumhargaganjil += hargaganjil

jumlah = sumhargaganjil + sumhargagenap
print(jumlah,"rupiah")