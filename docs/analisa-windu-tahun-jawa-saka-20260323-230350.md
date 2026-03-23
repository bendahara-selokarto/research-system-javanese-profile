# Analisa Windu, Nama Tahun Jawa, Tahun Saka, dan Hal Terkait

Waktu analisa: 2026-03-23 23:03:50 WIB
Nama file: analisa-windu-tahun-jawa-saka-20260323-230350.md

## Ringkasan utama

- Tahun Saka adalah era kronologis yang dimulai pada 78 M. Britannica mencatat era ini dipakai luas di India dan juga muncul pada prasasti Sanskerta di Indonesia.
- Kalender Jawa Sultan Agungan bukan salinan langsung kalender Saka lama. Kraton Yogyakarta menjelaskan bahwa Sultan Agung mempertahankan kelanjutan angka tahun Saka tetapi mengubah sistem hitung tahunnya menjadi lunar agar selaras dengan kalender Hijriah.
- Titik jangkar paling penting untuk sistem ini adalah 1 Sura Alip 1555 Jawa yang disejajarkan dengan 1 Muharram 1043 H dan 8 Juli 1633 M.
- Windu adalah siklus delapan tahun. Nama tahunnya berurutan: Alip, Ehe, Jimawal, Je, Dal, Be, Wawu, Jimakir.
- Di atas windu ada kurup. Dari sumber yang saya gunakan, urutan kurup yang relevan untuk sistem ini adalah Aahgi, Amiswon, Aboge, Asapon, lalu Anenhing. Kurup dipakai untuk menyelaraskan kalender Jawa terhadap akumulasi selisih harian dalam jangka panjang.

## Uraian analitis

### 1. Hubungan Saka, Hijriah, dan Jawa Sultan Agungan

Menurut Kraton Yogyakarta, Sultan Agung melakukan reformasi kalender dengan tetap meneruskan penomoran tahun Saka tetapi memakai dasar hitung lunar yang diselaraskan dengan Hijriah. Ini menjelaskan mengapa angka tahun Jawa tampak seperti kelanjutan Saka, tetapi logika pergantian bulannya mengikuti pola Islam Jawa, bukan pola Saka India dalam bentuk lamanya.

Artikel "Pengaruh Islam Terhadap Kalender Masyarakat Jawa" di Garuda Kemdikbud mendukung narasi ini: reformasi tersebut merupakan hasil akulturasi, bukan penghapusan total unsur lama.

### 2. Windu dan nama tahun Jawa

Dalam satu windu terdapat delapan nama tahun:

1. Alip
2. Ehe
3. Jimawal
4. Je
5. Dal
6. Be
7. Wawu
8. Jimakir

Urutan ini saya pakai langsung ke sistem hitungan repo ini karena sumber Kraton dan literatur falak yang saya cek konsisten pada urutan tersebut, walau ejaan bisa sedikit berbeda, misalnya Jimawal/Jim Awal dan Jimakir/Jim Akir.

### 3. Windu besar dan kurup

Dalam praktik tradisional Jawa, windu tidak berdiri sendiri. Ada pengelompokan empat windu besar: Kuntara, Sangara, Sancaya, dan Adi.

Di level yang lebih besar lagi ada kurup. Sumber falak UIN Malang dan Kraton Jogja menyebut urutan kurup historis sebagai berikut:

- Aahgi: Alip Jumat Legi, mulai 1555 AJ
- Amiswon: Alip Kamis Kliwon, mulai 1627 AJ
- Aboge: Alip Rebo Wage, mulai 1747 AJ
- Asapon: Alip Selasa Pon, mulai 1867 AJ
- Anenhing: Alip Senin Pahing, mulai 1987 AJ

Analisa saya: kurup adalah mekanisme koreksi jangka panjang. Ketika siklus lunar Jawa terus berjalan, akumulasi selisih hari harus dibetulkan agar jatuhnya awal tahun tidak melenceng terlalu jauh. Karena itu kurup bukan ornamen terminologi, melainkan bagian dari struktur hitungan kalender.

### 4. Tahun panjang dan tahun pendek

Dari artikel falak UIN Malang, pola tahun panjang tidak tunggal untuk semua kurup:

- Pada Aahgi dan Amiswon, tahun panjang jatuh pada Ehe, Dal, dan Jimakir.
- Pada Aboge dan Asapon, tahun panjang jatuh pada Ehe, Je, dan Jimakir.

Itu sebabnya dua tabel populer tentang taun wuntu kadang tampak berbeda. Perbedaannya bisa berasal dari kurup yang dijadikan acuan. Untuk integrasi sistem, saya memakai pembagian ini dan menambahkan pengecualian akhir-kurup Aboge sebagaimana dibahas di literatur falak.

### 5. Batas kehati-hatian untuk hitungan exact

Literatur falak yang saya temukan juga menunjukkan bahwa setelah fase Asapon, detail urutan tahun panjang pada Anenhing tidak selalu disajikan secara baku di sumber populer. Implementasi final di repo ini karena itu memakai dua jangkar sumber yang eksplisit: epoch Sultan Agungan 8 Juli 1633 untuk fase awal, dan jangkar Asapon 25 Maret 1936 untuk fase modern. Dari dua jangkar itu, sistem menurunkan hitungan taun, windu, dan kurup modern tanpa melepaskan referensi sejarah yang dipakai.

Ini adalah keputusan implementasi saya, bukan kutipan langsung sumber. Tujuannya menjaga sistem tidak memberi kepastian semu pada fase yang aturan bakunya tidak saya pegang dari sumber primer yang sama kuat.

## Integrasi ke sistem repo ini

Perubahan yang dimasukkan ke sistem:

- Menambah hitungan tahun Jawa exact berbasis jangkar 8 Juli 1633 / 1 Sura Alip 1555 AJ.
- Menambah identitas nama taun, nomor tahun Jawa, windu, posisi tahun dalam windu, jenis taun (wuntu atau wastu), dan kurup.
- Menambahkan catatan pada output dokumen bahwa angka tahun Jawa Sultan Agungan meneruskan penomoran Saka.
- Menjaga hitungan sistem berpijak pada dua jangkar sumber, lalu menurunkan informasi taun, windu, dan kurup dari sana agar referensi 1936 dan 2023 sama-sama cocok.

## Sumber

- Kraton Yogyakarta, "Kalender Jawa Sultan Agungan": https://www.kratonjogja.id/ragam/21-kalender-jawa-sultan-agungan/
- Kraton Yogyakarta, "Hajad Kawula Dalem Mubeng Beteng 1 Sura Jimawal 1957": https://www.kratonjogja.id/peristiwa/1274-hajad-kawula-dalem-mubeng-beteng-1-sura-jimawal-1957-kembali-diselenggarakan-secara-langsung/
- UIN Maulana Malik Ibrahim Malang, "Penyesuaian Kalender Saka dengan Kalender Hijriyah dan Aplikasinya dalam Penentuan Awal Bulan Qomariyah": https://syariah.uin-malang.ac.id/ar/penyesuaian-kalender-saka-dengan-kalender-hijriyah-dan-aplikasinya-dalam-penentuan-awal-bulan-qomariyah/
- Garuda Kemdikbud, "Pengaruh Islam Terhadap Kalender Masyarakat Jawa": https://download.garuda.kemdikbud.go.id/article.php?article=1093555&title=Pengaruh+Islam+Terhadap+Kalender+Masyarakat+Jawa&val=6177
- Encyclopaedia Britannica, "Saka era": https://www.britannica.com/topic/Saka-era
- Encyclopaedia Britannica, "Chronology: Reckonings dated from a historical event": https://www.britannica.com/topic/chronology/Reckonings-dated-from-a-historical-event

