# Bungalapak
Proyek Django untuk tugas mata Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Khansa Khairunisa - 2306153462.

Link untuk PWS deployment dapat diakses [di sini](http://khansa-khairunisa31-bungalapak.pbp.cs.ui.ac.id/).

## Tugas 2 
Pada tugas ini, kami akan mengimplementasikan konsep *Model-View-Template* (MVT) pada Django.

### Langkah Implementasi Checklist
Berikut adalah langkah-langkah yang saya lakukan untuk mengimplementasi checklist dari Tugas 2.

#### Membuat proyek Django
1. Buat direktori baru dengan nama `bungalapak` dan masuk ke direktori tersebut.
2. Buat *virtual environment* di dalam direktori tersebut dengan menjalankan perintah berikut di terminal.
    ```
    py -m venv env
    ```
3. Kemudian, aktifkan dengan menggunakan perintah berikut.
    ```
    env\Scripts\activate
    ```
4. Di dalam direktori yang sama, buat berkas `requirements.txt` menggunakan IDE Visual Studio Code dan tambahkan beberapa *dependencies* yang diperlukan sebagai berikut.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Lakukan instalasi terhadap *dependencies* yang ada dengan menjalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```
6. Buat proyek Django bernama `bungalapak` dengan menjalankan perintah berikut.
    ```
    django-admin startproject bungalapak .
    ```
7. Tambahkan string `"localhost"` dan `"127.0.0.1"` pada variabel `ALLOWED_HOSTS` di berkas `settings.py` untuk keperluan deployment.
8. Buat *repository* GitHub baru bernama `bungalapak` dengan visibilitas *public*. 
9. Inisiasi direktori lokal `bungalapak` sebagai *repository* Git dengan menjalankan perintah berikut pada direktori `bungalapak`.
    ```
    git init
    ```
10. Di dalam direktori yang sama, buat berkas `.gitignore` menggunakan IDE Visual Studio Code.
11. Buat *branch* utama baru bernama `master` dengan menjalankan perintah berikut.
    ```
    git branch -M master
    ```
12. Hubungkan *repository* lokal dengan *repository* GitHub dengan menggunakan perintah berikut.
    ```
    git remote add origin https://github.com/khansakhai/bungalapak.git
    ```
13. Lakukan `add`, `commit`, dan `push` dari direktori *repository* lokal dengan menggunakan perintah berikut.
    ```
    git add .
    git commit -m "UPDATE .gitignore"
    git push -u origin master
    ```

#### Membuat aplikasi dengan nama main pada proyek tersebut
14. Buat aplikasi baru bernama `main` dalam proyek `bungalapak` dengan menjalankan perintah berikut.
    ```
    python manage.py startapp main
    ```
15. Tambahkan string `'main'` pada variabel `INSTALLED_APPS` di berkas `settings.py`

#### Membuat Template
16. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` dan buat berkas baru bernama `main.html` di dalam direktori `templates`. 
17. Isi berkas `main.html` dengan nama aplikasi yaitu, bungalapak, nama, dan kelas.

#### Membuat Model
18. Buka berkas `models.py` pada direktori aplikasi `main` dan isi berkas tersebut dengan model bernama `Product` yang memiliki atribut `name`, `price`, dan `description`. 
19. Buat migrasi model dan lakukan migrasi ke dalam basis data lokal dengan menjalankan perintah berikut.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

#### Menghubungkan View dengan Template
20. Buka berkas `views.py` pada direktori aplikasi `main` dan tambahkan fungsi `show_main` yang akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai dengan template. Di dalamnya, tambahkan *dictionary* yang berisi data yang akan dikirimkan ke tampilan, mencakup nama dan kelas

#### Mengonfigurasi routing URL
21. Buat berkas `urls.py` di dalam direktori aplikasi `main` dan isi berkas dengan kode berikut.
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
22. Kemudian, buka berkas `urls.py` yang terdapat di dalam direktori proyek `bungalapak` dan lakukan perubahan kode sebagai berikut.
    ```
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```

#### Melakukan deployment ke PWS
23. Untuk melakukan deployment ke PWS, buka website PWS dan buat proyek baru bernama `bungalapak`. 
24. Tambahkan URL deployment PWS pada variabel `ALLOWED_HOSTS` di berkas `settings.py`. 
25. Lakukan `add`, `commit`, dan `push` perubahan tersebut ke *repository* GitHub
26. Jalankan perintah yang terdapat pada informasi *Project Command* di halaman PWS. 
27. Kemudian, jalankan perintah berikut.
    ```
    git branch -M master
    ```
28. Selesai!

### Bagan

### Fungsi git dalam pengembangan perangkat lunak

### Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

### Mengapa model pada Django disebut sebagai ORM?
