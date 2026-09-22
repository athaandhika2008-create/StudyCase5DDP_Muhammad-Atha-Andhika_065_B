**-PRAKTIKUM DDP STUDY CASE 5-**

**Nama : Muhammad Atha Andhika**

**Nim  : 2609116065**

**Kelas : B**

**Tipe Soal : Ganjil (Sistem Pemesanan Hotel)**

-----------------------------------------------

**1. Penjelasan Pertama**

<img width="1060" height="556" alt="Screenshot 2026-09-23 014649" src="https://github.com/user-attachments/assets/a0d8705a-8de2-42b0-a5e1-2b80364d8e39" />

Berikut merupakan Function `hitung_biaya()` yang digunakan untuk menghitung total biaya pemesanan hotel berdasarkan tipe kamar dan lama menginap. Function ini menerima 2 parameter yaitu `tipe_kamar` dan `lama_nginap`, kemudian menggunakan percabangan `if,elif` dan `else` untuk menentukan tarif kamar Standard atau Deluxe. Setelah tarif ditentukan, program kemudian menghitung total biaya sesuai jumlah malam menginap, lalu mengembalikan hasil perhitungannya menggunakan `return totalbiaya`.

-----------------------------------------------

**2. Penjelasan Kedua**

<img width="1669" height="1401" alt="Screenshot 2026-09-23 014751" src="https://github.com/user-attachments/assets/82bd222f-c4a8-4b7a-ba55-81471cf9bbb7" />

Berikut merupakan Function `validasitgl()` yang digunakan untuk memvalidasi tanggal check-in dan check-out dengan format `DD-MM-YYYY`. Function ini mengecek apakah format tanggal sudah sesuai, memastikan hari, bulan, dan tahun harus berupa angka, serta memeriksa apakah nilai hari, bulan, dan tahun berada pada rentang yang valid sesuai jumlah hari di setiap bulan. Hasil validasi akan dikembalikan menggunakan `return`, yaitu `True` jika valid dan `False` jika invalid.

-----------------------------------------------

**3. Penjelasan Ketiga**

<img width="1538" height="845" alt="Screenshot 2026-09-23 014827" src="https://github.com/user-attachments/assets/2c7b71f9-a8ef-4435-88b5-7913fd5d553c" />

Berikut merupakan bagian program yang digunakan untuk menerima input **nama penyewa** dan **tipe kamar**. Program menggunakan `while True` agar pengguna diminta mengisi data kembali jika input masih kosong atau tidak sesuai. Pada input tipe kamar, program hanya menerima pilihan **Standard** atau **Deluxe** dan mengubah semua variasi huruf menjadi format yang sama menggunakan `.lower()`, hingga input seperti `deLUXE`, `STANDARD`, `standard` tetap bisa dikenali dan valid.

-----------------------------------------------

**4. Penjelasan Keempat**

<img width="1597" height="1321" alt="Screenshot 2026-09-23 014952" src="https://github.com/user-attachments/assets/43495d54-2476-4c26-bcf2-0dd6dbc72fb6" />

Berikut merupakan bagian program yang digunakan untuk menerima input **tanggal check-in dan check-out** sekaligus menghitung **lama menginap**. Program menggunakan `while True` agar bisa mengisi ulang jika tanggal kosong atau format yang dimasukkan tidak sesuai `DD-MM-YYYY`. Setelah keduanya dinyatakan valid melalui function `validasitgl()`, program mengambil nilai hari, bulan, dan tahun untuk menghitung lama menginap serta memastikan minimal menginap 1 malam dan maksimal 30 malam. Jika semua data valid, proses akan keluar dari perulangan dan melanjutkan ke perhitungan biaya pemesanan hotel.

-----------------------------------------------

**5. Penjelasan Kelima**

<img width="822" height="262" alt="Screenshot 2026-09-23 015055" src="https://github.com/user-attachments/assets/b6c1496b-5a88-4a1e-a6e3-f8bbceac86f2" />

Berikut merupakan bagian program yang digunakan untuk mengambil Function `hitung_biaya()` dengan parameter `tipe_kamar` dan `lama_menginap` yang sudah diperoleh dari input pengguna dan hasil perhitungan tanggal. Nilai yang dikembalikan oleh function disimpan ke dalam variabel `totalbiaya` dan program akan kembali menentukan tarif kamar sesuai tipe kamar yang dipilih agar tarif per malam dapat ditampilkan pada hasil akhir bersama total biaya pemesanan hotel.

-----------------------------------------------

**6. Penjelasan Terakhir**

<img width="952" height="325" alt="Screenshot 2026-09-23 015107" src="https://github.com/user-attachments/assets/b84aa9c4-0a3f-4387-b3c1-a32363dd87f5" />

Berikut adalah program yang menampilkan hasil akhir pemesanan hotel setelah seluruh data berhasil diproses. Program menampilkan informasi berupa nama penyewa, tipe kamar yang dipilih, tanggal check-in dan check-out, lama menginap, tarif kamar per malam, serta total biaya pemesanan yang diperoleh dari function `hitung_biaya()`. Ini adalah output akhir yang menampilkan seluruh ringkasan pemesanan.

-----------------------------------------------

**-Hasil Output-**

<img width="2164" height="1209" alt="Screenshot 2026-09-23 014629" src="https://github.com/user-attachments/assets/cf8330f1-dd84-444a-b1fd-caccffba178a" />

**Terima Kasih!**
