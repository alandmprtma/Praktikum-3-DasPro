#Nama / NIM : Aland Mulia Pratama / 19622296
#Tanggal : 10 Maret 2023

# Program GambarSegitiga
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar segitiga sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarSegitiga(N):
    for i in range(N, 1, -2):
        print(' '*(i-1) + '*'*(N-i+1))
    print(N*'*')
    for i in range(3, N+1, 2):
        print(' '*(i-1) + '*'*(N-i+1))
# I.S. N > 0 dan N ganjil
# F.S. Gambar segitiga dengan tinggi sebesar N sesuai spesifikasi soal
# KAMUS LOKAL


def IsValid(N):
    return N > 0 and N % 2 == 1
# menghasilkan true jika N positif dan ganjil, false jika tidak

# ALGORITMA PROGRAM UTAMA
N = int(input())
if (IsValid(N)):  
    GambarSegitiga(N)    
else: 
    print("Masukan tidak valid")