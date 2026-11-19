# Portal Latihan Interaktif & Try Out OSN SD (Kemendikdasmen 2025)

Platform bank soal digital resmi dan interaktif yang diekstraksi langsung dari dokumen **Buku Kumpulan Soal OSN Olimpiade Sains Nasional Jenjang SD/MI/Sederajat 2025** yang diterbitkan oleh **Pusat Prestasi Nasional (Puspresnas) & Balai Pengembangan Talenta Indonesia (BPTI)** Kementerian Pendidikan Dasar dan Menengah.

---

## 🌟 Fitur Utama Web

1. **Dual Mode:**
   - **Mode Latihan Mandiri (Practice Mode):**
     - Filter instan per Mata Pelajaran (Matematika, IPA, IPS) dan Jenjang (Kabupaten, Provinsi, Semifinal, Final).
     - Tombol **💡 Petunjuk (Hint)** untuk memandu alur berpikir anak tanpa membocorkan jawaban.
     - Tombol **📝 Cara Penyelesaian & Pembahasan Lengkap** dengan rendering rumus matematika KaTeX ($\LaTeX$).
     - Umpan balik interaktif langsung (warna hijau jika benar, merah jika salah).
   - **Mode Try Out (Simulasi Ujian Resmi):**
     - Pemilihan mapel, tingkat seleksi, jumlah soal (10, 20, 30), dan durasi (15, 30, 60 menit).
     - *Countdown Timer* aktif dengan peringatan waktu.
     - Palet nomor soal ujian (terjawab, belum, ragu-ragu).
     - Rekapitulasi nilai otomatis (skor skala 100, jumlah benar, dan evaluasi salah).
     - Tombol *Review Pembahasan Try Out* untuk mempelajari ulang soal-soal ujian tadi.

2. **Format Rumus Matematika Cantik (KaTeX):**
   - Mendukung pecahan bertumpuk, eksponen, akar, dan simbol geometri ($\triangle ABC, \perp, \pi, \pmod n$).

3. **100% Offline-Ready (Tanpa Install Server Apapun):**
   - Cukup **klik dua kali** file `index.html`, web langsung berjalan di browser (Google Chrome, Microsoft Edge, Firefox) karena data sudah dibundel dalam `data/bank_soal_data.js` untuk menghindari kendala CORS lokal.

---

## 📁 Struktur Direktori

```
osn-sd/
├── index.html                  # Aplikasi web interaktif siap pakai
├── generate_bank_soal.py       # Script python ekstraksi dari PDF ke JSON
├── parse_all.py                # Utilitas parser PyMuPDF
├── README.md                   # Dokumentasi teknis & panduan
├── data/
│   ├── bank_soal_lengkap.json  # Database terpadu (350 soal)
│   ├── bank_soal_data.js       # Format JavaScript untuk offline standalone
│   ├── matematika.json         # Bank Soal Matematika (71 soal + pembahasan)
│   ├── ipa.json                # Bank Soal IPA (160 soal + pembahasan)
│   ├── ips.json                # Bank Soal IPS (119 soal + pembahasan)
│   └── metadata.json           # Rincian metadata resmi buku Puspresnas
└── images/                     # Direktori diagram & gambar soal
```

---

## 📊 Rekapitulasi Bank Soal yang Tersedia

Total soal yang berhasil diekstraksi dan disusun secara terstruktur: **350 Soal**

| Mata Pelajaran | Kabupaten (OSN-K) | Provinsi (OSN-P) | Semifinal | Final (Nasional) | Total Soal |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **📐 Matematika** | 30 Soal | 20 Soal | 15 Soal | 6+ Soal | **71 Soal** |
| **🔬 IPA** | 60 Soal | 30 Soal | 11 Soal | 59 Soal | **160 Soal** |
| **🌏 IPS** | 60 Soal | 40 Soal | 19 Soal | - | **119 Soal** |
| **TOTAL** | **150 Soal** | **90 Soal** | **45 Soal** | **65 Soal** | **350 Soal** |

---

## 🛠️ Skema Data JSON untuk Pengembangan Lanjutan

Jika Anda ingin menghubungkan data ini ke framework modern (seperti **Next.js**, **React**, **Vue**, atau backend **Supabase/PostgreSQL**), gunakan format objek JSON berikut:

```json
{
  "id": "OSN-SD-MAT-KAB-01",
  "nomor": 1,
  "mapel": "Matematika",
  "bab": "BAB 1: OSN Tingkat Kabupaten",
  "tingkat": "Kabupaten",
  "tipe": "pilihan_ganda",
  "topik": "Teori Bilangan & Pecahan",
  "tingkat_kesulitan": "Sedang",
  "pertanyaan": "Terdapat bilangan-bilangan sebagai berikut: 75% ; 0,745 ; 67/100 ; 2/3. Jika bilangan-bilangan tersebut diurutkan dari nilai terkecil hingga terbesar, maka urutannya adalah ….",
  "pilihan": [
    { "label": "A", "text": "2/3 ; 67/100 ; 0,745 ; 75%" },
    { "label": "B", "text": "67/100 ; 2/3 ; 0,745 ; 75%" },
    { "label": "C", "text": "2/3 ; 0,745 ; 67/100 ; 75%" },
    { "label": "D", "text": "67/100 ; 0,745 ; 2/3 ; 75%" }
  ],
  "kunci_jawaban": "A",
  "petunjuk": "Ubah semua pecahan dan persen ke dalam bentuk desimal setara untuk membandingkan nilainya.",
  "pembahasan": "75% = 0,75\n0,745 = 0,745\n67/100 = 0,67\n2/3 = 0,6666...\nJadi jika diurutkan dari terkecil hingga terbesar adalah: 2/3 ; 67/100 ; 0,745 ; 75% (Opsi A)."
}
```

---

## 🚀 Panduan Menjalankan Web

1. **Jalankan Secara Langsung (Desktop):**
   - Buka folder `c:\Users\LILI\OneDrive - PDK Jateng\Dokumen\osn-sd\`
   - Klik dua kali file `index.html`.
   - Web langsung terbuka di peramban tanpa perlu koneksi internet atau instalasi program tambahan.

2. **Deploy ke Web Hosting (Gratis via Vercel / GitHub Pages / Netlify):**
   - Unggah seluruh folder `osn-sd` ke repositori GitHub.
   - Sambungkan ke Vercel atau Netlify, pilih direktori root, dan klik *Deploy*.
   - Web latihan Anda langsung bisa diakses oleh anak dari tablet, iPad, maupun handphone di mana saja!
