# Tools Vlite - Ethical Hacking Collection

Tools Vlite adalah kumpulan script Python untuk keperluan **ethical hacking** yang terdiri dari beberapa tools populer, yaitu:
- **Nmap**
- **Nikto**
- **SQLmap**
- **Hydra**
- **Metasploit Framework**

Tools ini dirancang untuk dapat digunakan pada berbagai platform, termasuk **Termux**, **Linux**, **Windows**, dan **macOS**. Setiap tool memiliki fungsionalitas yang berbeda, dan kamu bisa memanfaatkannya untuk melakukan pengujian keamanan terhadap sistem yang sah (dengan izin).

## Daftar Isi
1. [Deskripsi Tools](#deskripsi-tools)
2. [Prasyarat](#prasyarat)
3. [Instalasi](#instalasi)
4. [Penggunaan](#penggunaan)
    - [Nmap](#nmap)
    - [Nikto](#nikto)
    - [SQLmap](#sqlmap)
    - [Hydra](#hydra)
    - [Metasploit Framework](#metasploit-framework)
5. [Peringatan](#peringatan)
6. [Lisensi](#lisensi)

## Deskripsi Tools

### 1. **Nmap**
**Nmap** adalah salah satu tools jaringan paling terkenal untuk memetakan jaringan dan mengecek port yang terbuka pada sistem yang diuji. Nmap dapat digunakan untuk:
- Pemindaian port.
- Deteksi sistem operasi.
- Deteksi layanan yang berjalan pada port tertentu.

### 2. **Nikto**
**Nikto** adalah scanner web yang digunakan untuk mengidentifikasi potensi kerentanannya di aplikasi web, seperti konfigurasi yang salah, versi perangkat lunak yang rentan, dan banyak lainnya.

### 3. **SQLmap**
**SQLmap** adalah tool otomatis untuk mengeksploitasi kerentanannya di aplikasi web yang rentan terhadap SQL injection. SQLmap memungkinkan kamu untuk:
- Menyisipkan SQL untuk mengambil data dari database.
- Mengeksekusi perintah melalui SQL injection.

### 4. **Hydra**
**Hydra** adalah alat serangan brute force yang mendukung berbagai protokol untuk mencoba password yang lemah atau menebak password melalui serangan brute force.

### 5. **Metasploit Framework**
**Metasploit Framework** adalah framework eksploitasi yang memungkinkan pengguna untuk mengembangkan dan menjalankan eksploitasi terhadap sistem yang rentan.

## Prasyarat

Sebelum memulai, pastikan kamu memiliki prasyarat berikut:
- **Python 3.x** (terinstal di sistem)
- **pip** (untuk instalasi library Python)
- **Termux** (untuk perangkat Android)
- **Metasploit Framework** (khusus untuk Metasploit)

### Platform yang Didukung:
- **Termux** (Android)
- **Linux** (Ubuntu, Kali, dll.)
- **Windows** (menggunakan WSL atau Command Prompt)
- **macOS**

## Instalasi

1. **Clone repositori ini ke mesin lokal:**
git clone https://github.com/MasAdii/tools_Vlite.git cd tools_Vlite


2. **Instal dependensi Python (jika ada):**
Jika tools membutuhkan dependensi Python tertentu, instal menggunakan pip:
pip install -r requirements.txt


Pastikan kamu memiliki **`requirements.txt`** dengan dependensi yang diperlukan.

3. **Untuk Metasploit (jika menggunakan Metasploit), instal secara terpisah.**
Ikuti instruksi resmi dari [Metasploit](https://metasploit.help.rapid7.com/docs/installing-the-metasploit-framework) untuk menginstal di sistem kamu.

4. **Perangkat khusus (misalnya Termux):**
Di Termux, kamu bisa menginstal dependencies seperti `nmap`, `hydra`, dll. menggunakan paket-paket Termux:

pkg install nmap hydra


## Penggunaan

Setelah repositori ini terinstal, kamu bisa menjalankan berbagai tools dari terminal. Berikut adalah cara penggunaan tiap tool.

### **Nmap**
Untuk memindai jaringan atau port:

python nmap_tool.py -t 192.168.1.1 -p 80,443

Gantilah `192.168.1.1` dengan IP target yang ingin kamu pindai.

### **Nikto**
Untuk menjalankan pemindaian Nikto terhadap aplikasi web:

python nikto_tool.py -url http://example.com

Gantilah `http://example.com` dengan URL aplikasi web target.

### **SQLmap**
Untuk mengeksploitasi potensi SQL Injection:
python sqlmap_tool.py -url "http://example.com/vuln_page?id=1"

Gantilah `http://example.com/vuln_page?id=1` dengan URL yang terindikasi rentan terhadap SQL Injection.

### **Hydra**
Untuk menjalankan serangan brute force:
python hydra_tool.py -t 192.168.1.1 -p 22 -w /path/to/wordlist.txt

Gantilah `192.168.1.1` dengan IP target, `22` dengan port, dan `/path/to/wordlist.txt` dengan lokasi wordlist yang kamu gunakan.

### **Metasploit Framework**
Untuk menggunakan Metasploit, ikuti langkah-langkah ini setelah menginstalnya:
msfconsole use exploit/windows/smb/ms08_067_netapi set RHOST 192.168.1.1 run


## Peringatan

**Penting:** Gunakan alat-alat ini hanya di jaringan atau sistem yang kamu miliki atau miliki izin untuk diuji. Pengujian keamanan tanpa izin yang sah dapat melanggar hukum dan peraturan setempat. Penggunaan alat ini untuk tujuan jahat atau tidak sah adalah ilegal dan bertanggung jawab sepenuhnya kepada pengguna.

## Lisensi

Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.
