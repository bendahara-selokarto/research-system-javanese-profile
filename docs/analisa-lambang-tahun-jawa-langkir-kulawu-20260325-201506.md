# Analisa Lambang Tahun Jawa: Langkir dan Kulawu

Waktu analisa: 2026-03-25 20:15:06 WIB
Nama file: analisa-lambang-tahun-jawa-langkir-kulawu-20260325-201506.md

## Ringkasan utama

- Dalam kalender Jawa Sultan Agungan, `lambang` adalah siklus tahun tingkat atas yang berjalan `8 tahun` per lambang, dengan dua nama: `Kulawu` dan `Langkir`. Karena hanya ada dua nama, total siklus lambang adalah `16 tahun`.
- Sumber Kraton Yogyakarta menegaskan bahwa epoch kalender Jawa Sultan Agungan, yaitu `1 Sura Alip 1555 AJ = 8 Juli 1633 M`, berada pada `Windu Kuntara Lambang Kulawu`.
- Preprint arXiv oleh Karjanto dan Beauducel memberi tabel pasangan `windu -> lambang` yang eksplisit: `Adi -> Langkir`, `Kuntara -> Kulawu`, `Sangara/Sengara -> Langkir`, `Sancaya -> Kulawu`.
- Implikasi implementasi: karena repo ini sudah menghitung `windu`, `lambang` bisa diturunkan secara deterministik dari `windu_name`, asalkan parity-nya diikat ke jangkar `1555 AJ = Kuntara Kulawu`.
- `Langkir` dan `Kulawu` juga muncul sebagai nama `wuku` dalam pawukon. Jadi di level model data, `lambang` tidak boleh dicampur dengan field `wuku`.

## Uraian analitis

### 1. Apa itu lambang dalam siklus tahun Jawa

Kraton Yogyakarta menjelaskan bahwa selain siklus `taun` dan `windu`, ada pula `lambang`. Kraton menyebut empat nama windu dan menambahkan bahwa tiap windu "memiliki lambang sendiri, Kulawu dan Langkir", dengan umur `8 tahun` untuk masing-masing lambang dan siklus total `16 tahun`.

Ini berarti `lambang` bukan sinonim dari `windu`. Keduanya sama-sama bergerak dalam unit `8 tahun`, tetapi total siklusnya berbeda:

- `windu`: 4 nama, total `32 tahun`
- `lambang`: 2 nama, total `16 tahun`

EPJ Web of Conferences juga merangkum hal yang sama: dua unit waktu terpanjang dalam kalender Jawa adalah `windu` dan `lambang`; keduanya sama-sama berdurasi `8 tahun`, tetapi lambang hanya memiliki dua jenis, yaitu `langkir` dan `kulawu`.

### 2. Jangkar parity yang penting: 1555 AJ

Masalah praktisnya bukan pada eksistensi `lambang`, melainkan pada penentuan kapan satu windu berpasangan dengan `Kulawu` atau `Langkir`.

Beberapa sumber populer hanya mengatakan bahwa lambang bergantian tiap windu. Pernyataan itu belum cukup untuk implementasi exact, karena tanpa jangkar awal kita tidak tahu apakah `Kuntara` harus dipasangkan ke `Kulawu` atau `Langkir`.

Sumber Kraton memberi jangkar yang kita butuhkan:

- `1 Sura Alip 1555 AJ`
- setara dengan `8 Juli 1633 M`
- jatuh pada `Windu Kuntara Lambang Kulawu`

Begitu parity awal ini diketahui, pola sesudahnya menjadi deterministik.

### 3. Pasangan windu dan lambang yang dapat dipakai

Karjanto dan Beauducel merangkum pasangan berikut:

| Windu | Lambang |
| --- | --- |
| Adi | Langkir |
| Kuntara | Kulawu |
| Sangara / Sengara | Langkir |
| Sancaya | Kulawu |

Jika urutan siklus repo tetap berangkat dari epoch `1555 AJ` yang sekarang sudah dipakai, maka pola berulangnya adalah:

1. `Kuntara -> Kulawu`
2. `Sangara -> Langkir`
3. `Sancaya -> Kulawu`
4. `Adi -> Langkir`
5. kembali ke `Kuntara -> Kulawu`

Catatan ejaan:

- Kraton menulis `Sangara`.
- Preprint arXiv menulis `Sengara`.
- Untuk integrasi sistem, ini sebaiknya diperlakukan sebagai varian ejaan dari label yang sama.

### 4. Hubungan dengan model repo saat ini

Repo saat ini sudah memiliki model `JavaneseYearCycle` dengan field:

- `year_name`
- `windu_name`
- `windu_year_number`
- `kurup_code`

dan belum memiliki field `lambang_name`.

Karena fungsi `_build_year_cycle()` sudah selalu menghasilkan `windu_name`, penambahan `lambang_name` secara teknis sederhana. Aturan minimumnya bisa dibuat seperti ini:

```text
Kuntara -> Kulawu
Sangara -> Langkir
Sancaya -> Kulawu
Adi -> Langkir
```

atau, jika ingin bergantung pada indeks windu dari epoch repo:

```text
offset_windu = floor((year_number - 1555) / 8)
lambang = "Kulawu" jika offset_windu genap, selain itu "Langkir"
```

Saya menilai pendekatan `mapping by windu_name` lebih aman dibaca karena:

- lebih eksplisit
- tidak rawan salah jika urutan label windu nanti dirapikan
- langsung mengikuti tabel sumber

### 5. Risiko salah tafsir yang perlu dihindari

Ada dua titik rawan:

1. `Langkir` dan `Kulawu` juga merupakan nama `wuku`.
   Jadi kalimat seperti "tahun ini Langkir" dan "hari ini wuku Langkir" menunjuk dua lapisan siklus yang berbeda.

2. Sumber populer sering menyebut lambang hanya "bergantian".
   Tanpa jangkar `1555 AJ = Kuntara Kulawu`, implementasi bisa bergeser satu fase penuh dan seluruh hasil lambang akan terbalik.

### 6. Rekomendasi integrasi untuk repo ini

- Tambahkan `lambang_name` ke `JavaneseYearCycle`.
- Turunkan nilainya langsung dari `windu_name` memakai tabel pasangan di atas.
- Tampilkan `lambang` pada ringkasan `summary`, `common_uses["siklus_tahun_jawa"]`, dan output dokumen di `javanese_profile.py`.
- Simpan terminologi `wuku` dan `lambang` pada field terpisah karena `Langkir/Kulawu` muncul di kedua sistem.

## Kesimpulan kerja

Untuk repo ini, keputusan yang paling defensible adalah:

- menerima `lambang` sebagai bagian sah dari siklus tahun Jawa Sultan Agungan
- mengikat parity lambang ke jangkar Kraton `1555 AJ = Kuntara Kulawu`
- menurunkan `lambang` dari `windu_name`, bukan dari asumsi populer yang tidak menyebut titik awal

Dengan dasar itu, sistem bisa menambah `lambang` tanpa mengubah logika taun, windu, atau kurup yang sudah ada.

## Sumber

- Kraton Yogyakarta, "Kalender Jawa Sultan Agungan": https://www.kratonjogja.id/ragam/21-kalender-jawa-sultan-agungan/
- Karjanto, N. dan Beauducel, F., "An ethnoarithmetic excursion into the Javanese calendar" (arXiv 2012.10064): https://arxiv.org/abs/2012.10064
- Versi HTML ar5iv untuk tabel windu-lambang: https://ar5iv.labs.arxiv.org/html/2012.10064
- EPJ Web of Conferences, "The Javanese Calendar System" (ringkasan hasil pencarian DOI 10.1051/epjconf/202024007007): https://doi.org/10.1051/epjconf/202024007007
