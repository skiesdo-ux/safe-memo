# SafeMemo (Python)
SafeMemo adalah program sederhana yang dibuat untuk mengamankan catatan pribadi menggunakan enkripsi simetris AES. Catatan dienkripsi sebelum disimpan ke dalam file sehingga tidak dapat dibaca langsung. Kunci enkripsi dihasilkan dari password pengguna menggunakan PBKDF2 agar lebih aman dan tidak disimpan langsung di dalam program


## Daftar Isi
- Fitur
- Arsitektur Keamanan
- Cara Download & Install
- Cara Menjalankan Program
- Struktur Project
- Standar Keamanan

## Fitur

### Fitur Keamanan
- AES Encryption (Fernet)
- PBKDF2 Key Derivation (100.000 iterasi)
- Kunci Dinamis berbasis password
- Salt acak untuk setiap enkripsi
- Proteksi dari brute-force sederhana

### Mode Penggunaan
- Enkripsi catatan teks
- Dekripsi catatan terenkripsi
- Penyimpanan file `.enc`


## Arsitektur Keamanan
```
┌────────────────────────────────────────────────────────────────────────────┐
│                               ALUR ENKRIPSI                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│   Password Pengguna                                                        │
│          │                                                                 │
│          ▼                                                                 │
│   ┌───────────────────┐                                                    │
│   │      PBKDF2       │◀── Salt (16 bytes, random)                        │ 
│   │   SHA-256 Hash    │                                                    │
│   │  100.000 iterasi  │                                                    │
│   └─────────┬─────────┘                                                    │
│             │                                                              │
│             ▼                                                              │
│     Derived Key (256-bit)                                                  │
│             │                                                              │
│             ▼                                                              │
│   ┌────────────────────────────┐                                           │
│   │      AES (Fernet Mode)      │                                          │
│   │  Enkripsi + Autentikasi     │                                          │
│   └─────────────┬──────────────┘                                           │
│                 │                                                          │
│                 ▼                                                          │
│          Ciphertext Terenkripsi                                            │
│                 │                                                          │
│                 ▼                                                          │
│   ┌────────────────────────────┐                                           │
│   │     File .enc (Binary)      │                                          │
│   │ [ salt | encrypted_data ]   │                                          │
│   └────────────────────────────┘                                           │
│                                                                            │
│   Output: File catatan terenkripsi                                         │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```


## Cara Download & Install

### Prasyarat
- Python 3.8 atau lebih tinggi
- Git
- pip

### Clone Repository
```bash
git clone https://github.com/username/SafeMemo.git
cd SafeMemo
```

### Install Dependency
```bash
pip install -r requirements.txt
```

## Cara Menjalankan Program
```bash
python safememo.py
```

## Struktur Project
```
SafeMemo/
│
├── core/
│   ├── __init__.py
│   ├── crypto_core.py
│   ├── kdf.py
│   └── utils.py
│
├── cli_text.py
├── cli_file.py
├── gui_app.py
├── tamper_demo.py
├── requirements.txt
├── README.md
└── .gitignore

```



