# Repositori Tugas Praktikum Cloud Computing

Nama   : Rafhan Mazaya Fathurrahman
NIM    : 101012300238
Kelas  : BS1TT-47-REG-GAB01
Dosen  : Cahyo Alhazim
Repo   : https://github.com/fhanyuh/cloud-computing-docker-101012300238

---

## Daftar Tugas Praktikum

### 1. Tugas 1 — Instalasi Docker Engine & Simulasi Jaringan VPC (IaaS)
Direktori: [`tugas1-docker-installation/`](./tugas1-docker-installation/)
- Laporan PDF: [`tugas1-docker-installation/laporan-instalasi.pdf`](./tugas1-docker-installation/laporan-instalasi.pdf)
- Laporan Markdown: [`tugas1-docker-installation/laporan-instalasi.md`](./tugas1-docker-installation/laporan-instalasi.md)
- Log Eksekusi: [`tugas1-docker-installation/logs/`](./tugas1-docker-installation/logs/)
- Screenshot: [`tugas1-docker-installation/screenshots/`](./tugas1-docker-installation/screenshots/)

### 2. Tugas 2 — Hands-On Docker Lifecycle, Dockerfile, & Docker Compose
Direktori: [`tugas-docker-101012300238/`](./tugas-docker-101012300238/)
- Laporan PDF: [`tugas-docker-101012300238/laporan-handson.pdf`](./tugas-docker-101012300238/laporan-handson.pdf)
- Laporan Markdown: [`tugas-docker-101012300238/laporan-handson.md`](./tugas-docker-101012300238/laporan-handson.md)
- Kode Sumber: [`app.py`](./tugas-docker-101012300238/app.py), [`Dockerfile`](./tugas-docker-101012300238/Dockerfile), [`docker-compose.yml`](./tugas-docker-101012300238/docker-compose.yml)
- Log Eksekusi: [`tugas-docker-101012300238/logs/`](./tugas-docker-101012300238/logs/)
- Screenshot: [`tugas-docker-101012300238/screenshots/`](./tugas-docker-101012300238/screenshots/)

### 3. Tugas 3 — Hands-On CI/CD Pipeline (Jenkins, GitHub, Docker, dan ngrok)
File utama di root repositori (sesuai spesifikasi modul) dan laporan di [`cicd/`](./cicd/):
- Kode Aplikasi REST API: [`app.py`](./app.py)
- Definisi Image Docker (`HEALTHCHECK`): [`Dockerfile`](./Dockerfile)
- Konfigurasi Build Context: [`.dockerignore`](./.dockerignore)
- Definisi Pipeline-as-Code: [`Jenkinsfile`](./Jenkinsfile)
- Laporan PDF: [`cicd/laporan-cicd.pdf`](./cicd/laporan-cicd.pdf)
- Laporan Markdown: [`cicd/laporan-cicd.md`](./cicd/laporan-cicd.md)
- Log Eksekusi: [`cicd/logs/`](./cicd/logs/)
- Screenshot: [`cicd/screenshots/`](./cicd/screenshots/)

---

## Struktur Direktori Repositori

```text
.
├── app.py                              # Python REST API (CRUD + filter ?q= + detail /messages/<id>)
├── Dockerfile                          # Image python:3.11-slim + Docker HEALTHCHECK
├── .dockerignore                       # Mengabaikan file non-aplikasi dari build context
├── Jenkinsfile                         # Declarative Pipeline 5 stage + tag BUILD_NUMBER, sha, latest
├── README.md                           # Dokumentasi utama repositori
├── cicd/                               # Dokumentasi dan bukti praktikum CI/CD
│   ├── laporan-cicd.md
│   ├── laporan-cicd.pdf
│   ├── logs/
│   └── screenshots/
├── tugas1-docker-installation/         # Dokumentasi dan bukti Tugas 1
└── tugas-docker-101012300238/          # Dokumentasi dan bukti Tugas 2
```

---

## Panduan Pengujian Aplikasi REST API (Tugas 3)

### 1. Build dan Jalankan Container Secara Manual
```bash
docker build -t python-crud-api:manual .
docker volume create production-api-data
docker run -d --name production-api-container \
  -p 5000:5000 \
  -v production-api-data:/var/lib/backend_data \
  python-crud-api:manual
```

### 2. Uji Endpoint API
```bash
# Health check
curl -i http://localhost:5000/health

# Tambah pesan (POST)
curl -i -X POST http://localhost:5000/messages \
  -H 'Content-Type: application/json' \
  -d '{"message":"Data praktikum CI/CD NIM 101012300238"}'

# Baca seluruh pesan (GET)
curl -s http://localhost:5000/messages

# Filter pesan berdasarkan kata kunci (GET ?q=)
curl -s "http://localhost:5000/messages?q=101012300238"

# Baca detail pesan berdasarkan indeks (GET /messages/<index>)
curl -s http://localhost:5000/messages/0

# Hapus pesan berdasarkan indeks (DELETE)
curl -i -X DELETE "http://localhost:5000/messages?index=0"
```
