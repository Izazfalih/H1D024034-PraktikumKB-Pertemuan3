# Laporan Praktikum Kecerdasan Buatan - Pertemuan 3

### PRAKTIKUM ACARA 3

- **Nama:** Izaz Falih
- **NIM:** H1D024034

---

### STUDI KASUS SATU: UDIN PET SHOP

Studi kasus ini bertujuan untuk mengoptimalkan persediaan stok makanan hewan peliharaan.

#### Variabel Input

1. **Barang Terjual:** 0 - 100 unit
2. **Permintaan:** 0 - 300 unit
3. **Harga Per Item:** 0 - 100.000 rupiah
4. **Profit:** 0 - 4.000.000 rupiah

#### Variabel Output

- **Stok Makanan:** 0 - 1.000 unit

#### Hasil Perhitungan

- **Input:**
  - Barang Terjual: 80 unit
  - Permintaan: 255 unit
  - Harga Per Item: 25.000 rupiah
  - Profit: 3.500.000 rupiah

- **Hasil Akhir Stok Makanan:** 831 unit

![Visualisasi Hasil Kasus 1](Visualiasasi%20Grafik/Output%20Stok%20Makanan.png)

**Penjelasan Grafik:**
Grafik di atas menunjukkan fungsi keanggotaan untuk variabel output **Stok Makanan** yang terdiri dari kategori 'sedang' dan 'banyak'. Nilai output sistem fuzzy sebesar 8.31. Karena menggunakan skala 0–10, maka setelah dikonversi ke skala asli (0–1000), diperoleh nilai sebesar **831 unit**, yang termasuk kategori stok banyak. Hasil ini merepresentasikan nilai tegas (crisp) dari stok makanan yang harus disediakan berdasarkan kombinasi input barang terjual, permintaan, harga, dan profit yang telah dimasukkan.

---

### STUDI KASUS DUA: PELAYANAN MASYARAKAT KOTA SEJAHTERA

Studi kasus ini bertujuan untuk menentukan tingkat kepuasan layanan pengaduan masyarakat.

#### Variabel Input

1. **Kejelasan Informasi:** 0 - 100
2. **Kejelasan Persyaratan:** 0 - 100
3. **Kemampuan Petugas:** 0 - 100
4. **Ketersediaan Sarana dan Prasarana:** 0 - 100

#### Variabel Output

- **Kepuasan Pelayanan:** 0 - 400

#### Analisis Implementasi

- **Input yang diuji:**
  - Kejelasan Informasi: 80
  - Kejelasan Persyaratan: 60
  - Kemampuan Petugas: 50
  - Ketersediaan Sarpras: 90
- **Hasil Akhir Kepuasan Pelayanan:** 214.82

![Himpunan Fuzzy Output Kasus 2](Visualiasasi%20Grafik/Output%20Kepuasan.png)

**Penjelasan Grafik:**
Grafik di atas menampilkan himpunan fuzzy untuk variabel output **Kepuasan Pelayanan** dengan lima kategori: 'tidak memuaskan', 'kurang memuaskan', 'cukup memuaskan', 'memuaskan', dan 'sangat memuaskan'. Diperoleh nilai sebesar **214.82**, yang termasuk kategori "cukup memuaskan" dan "memuaskan". Hasil ini merepresentasikan nilai tegas (crisp) dari kepuasan pelayanan berdasarkan kombinasi input kejelasan informasi, kejelasan persyaratan, kemampuan petugas, dan ketersediaan sarana dan prasarana yang telah dimasukkan.

---

### KESIMPULAN

Implementasi Logika Fuzzy Mamdani telah berhasil dilakukan untuk kedua studi kasus. Program telah dilengkapi dengan visualisasi grafik untuk setiap variabel. Semua grafik visualisasi dan kode sumber telah tersedia di repositori ini.
