# NAMA / NIM : Aland Mulia Pratama / 19622296
# Tanggal : 10 Maret 2023

# Program TigaInteger
# Input: 3 integer: A, B, C
# Output: Sifat integer dari A, B, C (positif/negatif/nol dan ganjil/genap) 
#         Nilai maksimum, minimum, dan nilai tengah
 
# KAMUS
# variabel
#    A, B, C : int
#    nilaitengah : int
 
# PROCEDURE DAN FUNCTION
def CekInteger (x):
    if x == 0:
        print ("NOL")
    elif (x > 0) and (x%2 == 0):
        print("POSITIF-GENAP")
    elif (x > 0) and (x%2 == 1):
        print("POSITIF-GANJIL")
    elif (x < 0):
        print("NEGATIF")
# I.S.: x terdefinisi, bertype int
# F.S.: Jika x positif dan genap, maka tertulis di layar: POSITIF-GENAP
#       Jika x positif dan ganjil, maka tertulis di layar: POSITIF-GANJIL
#       Jika x negatif, maka tertulis di layar: NEGATIF
#       Jika x nol, maka tertulis di layar: NOL
# Tuliskan realisasi prosedur CekInteger di bawah ini
              
def Max (a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b>= c:
        return b
    elif c >= a and c >= b:
        return c
# menghasilkan nilai terbesar di antara a, b, c (integer)
# Tuliskan realisasi fungsi Max di bawah ini
     
def Min (a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return a
    elif c <= a and c <= b:
        return c

# menghasilkan nilai terkecil di antara a, b, c (integer)
# Tuliskan realisasi fungsi Min di bawah ini
            
# PROGRAM UTAMA
# Input
A = int(input())
B = int(input())
C = int(input())

# Menuliskan sifat integer
CekInteger(A)
CekInteger(B)
CekInteger(C)

# Penulisan maksimum, minimum, dan nilai tengah
print(Max(A,B,C))
print(Min(A,B,C))
nilaitengah = A + B + C - Max(A,B,C) - Min(A,B,C) 
print(nilaitengah)