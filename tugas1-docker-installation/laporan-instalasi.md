# Laporan Instalasi Docker — Cloud Computing

Nama   : Rafhan Mazaya Fathurrahman
NIM    : 101012300238
Kelas  : BS1TT-47-REG-GAB01
Dosen  : Cahyo Alhazim
Repo   : https://github.com/fhanyuh/cloud-computing-docker-101012300238

## 1. Versi Docker Terpasang

```bash
docker --version
docker compose version
```

| Komponen | Versi |
|---|---|
| Docker Engine | 29.7.2 (Community) |
| Docker Compose | v5.5.0 |
| Container Runtime | containerd v2.3.3 / runc 1.4.3 |

![](screenshots/01-docker-version.png)

## 2. Verifikasi Docker Berjalan (hello-world)

```bash
docker run --rm hello-world
```

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

![](screenshots/02-docker-hello-world.png)

## 3. Lab Simulasi VPC (IaaS) — Materi Pertemuan 1

```bash
docker network create --subnet=192.168.50.0/24 vpc-local-101012300238
docker run -d --name nginx-vpc-101012300238 --net vpc-local-101012300238 \
  --ip 192.168.50.10 -p 8085:80 nginx:alpine
docker network inspect vpc-local-101012300238 \
  --format "VPC: {{.Name}} | Subnet: {{(index .IPAM.Config 0).Subnet}} | Gateway: {{(index .IPAM.Config 0).Gateway}}"
docker inspect nginx-vpc-101012300238 \
  --format "Container: {{.Name}} | IP Statis: {{(index .NetworkSettings.Networks \"vpc-local-101012300238\").IPAddress}}"
curl -s -I http://localhost:8085
```

| Parameter | Nilai |
|---|---|
| Subnet VPC | 192.168.50.0/24 |
| Gateway | 192.168.50.1 |
| IP Statis Kontainer | 192.168.50.10 |
| Respons HTTP | HTTP/1.1 200 OK |

![](screenshots/03-iaas-vpc-network.png)

```bash
docker stop nginx-vpc-101012300238
docker rm nginx-vpc-101012300238
docker network rm vpc-local-101012300238
```
