# Praktikum-3-DasPro
Praktikum 3 Dasar Pemrograman Institut Teknologi Bandung yang menggunakan bahasa Python
## Soal 1
Nama file: maksimum3bilangan.py
Tuliskanlah sebuah program yang membaca 3 buah bilangan integer dan menuliskan nilai terbesar di antara ketiganya.
## Soal 2
Nama file: lingkaran.py

Buatlah program yang digunakan untuk menghitung luas lingkaran. Program menerima input jari-jari (integer). Input jari-jari harus divalidasi sehingga selalu > 0. Apabila jari-jari yang dimasukkan <= 0, program akan mengeluarkan pesan error. Jika jari-jari yang dimasukkan valid, program menghasilkan luas lingkaran dengan rumus: 3.1415 * jari-jari * jari-jari.

Keterangan:
Luas lingkaran harus ditulis dengan 2 angka di belakang koma.
## Soal 3
Nama file: tigainteger.py

Sebuah program digunakan untuk membaca 3 buah integer, yaitu A, B, C, menuliskan sifat integer ketiga integer dengan ketentuan sebagai berikut:

Jika suatu integer x adalah positif dan genap menuliskan: “POSITIF-GENAP”.
Jika suatu integer x adalah positif dan ganjil, menuliskan: “POSITIF-GANJIL”.
Jika suatu integer x adalah negatif, menuliskan “NEGATIF”.
Jika suatu integer x adalah nol, menuliskan “NOL”.
Selanjutnya program menuliskan nilai maksimum, minimum, dan nilai tengah dari ketiganya.

Persoalan ini harus diselesaikan dengan memanfaatkan fungsi dan prosedur.

Salinlah program di bawah ini dan lanjutkan realisasi fungsi Max dan Min serta prosedur CekInteger sesuai dengan spesifikasi yang diberikan.

Tidak boleh mengutak-atik bagian program yang lain. Jangan lupa menambahkan identitas.
## Soal 4
Nama file: hargaMakanan.py
Restoran Se’i Sapi menginginkan sebuah program yang digunakan untuk menghitung total harga makanan. Program pertama - tama menerima input N sebagai  jumlah makanan yang dibeli, kemudian menerima N buah kode makanan bertipe integer positif atau 0. Bila kode makanan yang dimasukkan berada pada urutan ganjil, maka harga makanan didapat dengan mengalikan kode dengan 100 rupiah. Bila kode makanan pada urutan genap, harga makanan didapat dengan mengalikan kode dengan 200 rupiah. Setelahnya, program akan menampilkan total penjumlahan harga makanan.
Asumsi: N > 0; kode makanan >= 0.
Contoh input/output:
Input
3
2
3
0
Output
800 rupiah
Keterangan:
800 = 2 * 100 + 3 * 200 + 0 * 100 
## Soal 5
Nama file: segitiga.py
Buatlah sebuah program yang menerima masukan sebuah bilangan bulat, misal N dan kemudian menampilkan gambar huruf segitiga dari karakter bintang seperti contoh di bawah, jika N adalah bilangan bulat ganjil (N > 0). Jika N bukan positif dan/atau bukan ganjil, maka diberikan pesan kesalahan.
Untuk mengimplementasikan program tersebut, harus dibuat minimum fungsi dan prosedur sebagai berikut:
1.      Prosedur GambarSegitiga
Prosedur ini digunakan untuk menggambar segitiga sebagaimana spesifikasi di atas. Prosedur ini mempunyai parameter input sebuah integer, misalnya N, yang diasumsikan benar (integer positif dan ganjil) dan kemudian menampilkan ke layar sebuah segitiga dari bintang sesuai spesifikasi di atas.
Untuk menyederhanakan persoalan, prosedur GambarSegitiga ini dapat ditolong dengan membuat satu atau lebih prosedur untuk menggambar bintang dan/atau spasi per baris. Buatlah definisi, spesifikasi, dan implementasi dari prosedur(-prosedur) tambahan ini.
2.      Fungsi IsValid
Fungsi ini menerima input sebuah integer, misalnya N, dan menghasilkan boolean, yaitu true jika N adalah integer yang dapat digunakan untuk menggambarkan segiempat di atas (integer positif dan ganjil) dan false jika tidak.
Salin dan lengkapilah template program sbb.
