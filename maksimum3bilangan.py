#Maksimum3Bilangan
#Program menerima 3 buah bilangan integer lalu mengembalikan nilai yang paling maksimum 

#KAMUS
#angka1, angka2, angka3 : Int

#ALGORITMA
#Input
angka1 = int(input()) 
angka2 = int(input())
angka3 = int(input())

if angka1 >= angka2 and angka1 >= angka3 :
    print (angka1) 
elif angka2 >= angka1 and angka2 >= angka3:
    print (angka2) 
elif angka3 >= angka1 and angka3>= angka2:
    print (angka3)  