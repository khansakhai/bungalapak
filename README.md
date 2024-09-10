# Bungalapak
Proyek Django untuk tugas mata kuliah Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Khansa Khairunisa - 2306153462.

Tautan menuju PWS deployment dapat diakses [di sini](http://khansa-khairunisa31-bungalapak.pbp.cs.ui.ac.id/).

## Tugas 2 
Pada tugas ini, akan dilakukan implementasi dari konsep *Model-View-Template* (MVT) pada Django.

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
Git merupakan sistem kontrol versi (Version Control System) yang berfungsi untuk melacak setiap perubahan pada kode dalam pengembangan perangkat lunak, memungkinkan pengembang untuk bekerja secara kolaboratif, mengelola proyek secara efisien, dan menghindari konflik. Setiap perubahan kode akan tersimpan di dalam *history* yang dapat diakses ataupun di-revert jika diperlukan. Selain itu, pengembang juga dapat bekerja dalam branch terpisah (branching) dan menggabungkan perubahan tersebut ke dalam kode utama (merging), sehingga setiap anggota tim dapat bekerja pada repositori yang sama secara bersamaan. 

### Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dijadikan permulaan pembelajaran pengembangan perangkat lunak terutama pada mata kuliah Pemrograman Berbasis Platform karena framework ini di tulis dalam bahasa Python, yang di mana sudah kami pelajari dari perkuliahan di semester satu. Selain itu, Django memiliki struktur yang lengkap, terorganisir, dan ramah bagi pemula. Django mengikuti pola *Model-View-Template* (MVT) yang memudahkan pengguna dalam memahami arsitektur aplikasi website. Django juga memiliki fitur atau modul lainnya, seperti autentikasi pengguna, pengelolaan URL, dan manajemen basis data (ORM).

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai *Object-Relational Mapping* (ORM) karena berfungsi untuk memetakan objek Python ke struktur basis data. Dengan ORM, tabel dalam basis data direpresentasikan sebagai kelas, dan kolom tabel sebagai atribut kelas. Ini memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan pemrograman Python, tanpa perlu menulis SQL secara langsung, sehingga memudahkan pengelolaan data dan menjaga kode agar tetap konsisten dan mudah dipahami. 