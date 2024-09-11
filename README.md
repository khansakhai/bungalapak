# Bungalapak
Proyek Django untuk tugas mata kuliah Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Khansa Khairunisa - 2306153462.

Tautan menuju PWS deployment dapat diakses [di sini](http://khansa-khairunisa31-bungalapak.pbp.cs.ui.ac.id/).

## Tugas 2 
Pada tugas ini, akan dilakukan implementasi dari konsep *Model-View-Template* (MVT) pada Django.

### Langkah Implementasi Checklist
Berikut adalah langkah-langkah yang saya lakukan untuk mengimplementasikan checklist dari Tugas 2.

#### Membuat proyek Django
1. Langkah pertama, saya membuat direktori baru dengan nama `bungalapak` dan masuk ke dalam direktori tersebut.
2. Setelah itu, saya membuat *virtual environment* dengan menjalankan perintah berikut di terminal.
    ```
    py -m venv env
    ```
3. Kemudian, mengaktifkannya dengan menggunakan perintah berikut.
    ```
    env\Scripts\activate
    ```
4. Di dalam direktori yang sama, saya membuat berkas `requirements.txt` menggunakan IDE Visual Studio Code dan menambahkan beberapa *dependencies* yang diperlukan sebagai berikut.
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
5. Setelah itu, saya melakukan instalasi terhadap *dependencies* yang dibutuhkan dengan menjalankan perintah berikut.
    ```
    pip install -r requirements.txt
    ```
6. Untuk membuat proyek Django bernama `bungalapak`, saya menjalankan perintah berikut.
    ```
    django-admin startproject bungalapak .
    ```
7. Setelah itu, saya menambahkan string `"localhost"` dan `"127.0.0.1"` pada variabel `ALLOWED_HOSTS` di berkas `settings.py` untuk keperluan deployment.
8. Saya membuat *repository* GitHub baru bernama `bungalapak` dengan visibilitas *public*. 
9. Kemudian, saya menginisiasi direktori lokal `bungalapak` sebagai *repository* Git dengan menjalankan perintah berikut pada direktori `bungalapak`.
    ```
    git init
    ```
10. Di dalam direktori yang sama, saya membuat berkas `.gitignore` menggunakan IDE Visual Studio Code dan meng-copy-paste kode yang dibutuhkan dari tutorial.
11. Setelah itu, saya membuat *branch* utama baru bernama `master` dengan menjalankan perintah berikut.
    ```
    git branch -M master
    ```
12. Untuk menghubungkan direktori lokal dengan *repository* GitHub, saya menjalankan perintah berikut.
    ```
    git remote add origin https://github.com/khansakhai/bungalapak.git
    ```
13. Kemudian, saya melakukan `add`, `commit`, dan `push` dari direktori *repository* lokal dengan menggunakan perintah berikut.
    ```
    git add .
    git commit -m "UPDATE .gitignore"
    git push -u origin master
    ```

#### Membuat aplikasi dengan nama main
14. Untuk membuat aplikasi baru bernama `main` dalam proyek `bungalapak`, saya menjalankan perintah berikut.
    ```
    python manage.py startapp main
    ```
15. Kemudian, saya menambahkan nama aplikasi `'main'` pada variabel `INSTALLED_APPS` di berkas `settings.py`

#### Melakukan routing pada proyek
16. Agar proyek dapat menjalankan aplikasi `main`, route proyek perlu dikonfigurasi. Untuk itu, saya membuka berkas `urls.py` yang terdapat di dalam direktori proyek `bungalapak` dan melakukan beberapa perubahan kode sebagai berikut.
    ```
    from django.urls import path, include

    urlpatterns = [
        ...
        path('', include('main.urls')),
        ...
    ]
    ```
    Saya mengimpor include agar berkas routing ini dapat mengimpor atau menyertakan route yang sudah didefinisikan oleh aplikasi lain ke dalam routing utama proyek, yaitu `urls.py` aplikasi `main`. Dengan menggunakan `path('', include('main.urls'))`, semua permintaan ke URL utama akan langsung dipetakan ke route yang didefinisikan dalam dalam berkas `urls.py` aplikasi `main`, sehingga pengguna tidak perlu menambahkan `/main` pada URL untuk mengakses halaman aplikasi `main`.

#### Membuat model pada aplikasi main
17. Untuk membuat model, saya memodifikasi berkas `models.py` pada direktori aplikasi `main` dengan model bernama `Product` yang memiliki atribut `name`, `price`, dan `description`. Berikut adalah kode yang saya tambahkan.
    ```
    class Product(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
    ```
    Model ini memiliki atribut `name` yang berupa CharField dengan panjang maksimal 255, `price` yang berupa IntegerField, dan `description` yang berupa TextField. Ketiga atribut tersebut nantinya akan digunakan untuk mendefinisikan sebuah *item* yang ada pada aplikasi. 
18. Setelah itu, saya membuat migrasi model dan melakukan migrasi ke dalam basis data lokal dengan menjalankan perintah berikut.
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    Dengan perintah tersebut, penambahan model sudah 'tertanam' pada aplikasi dan basis data sudah disesuaikan. 

#### Membuat fungsi pada views.py
19. Setelah mendefinisikan model, saya membuat direktori baru bernama `templates` di dalam direktori aplikasi `main` dan membuat berkas baru bernama `main.html` di dalam direktori `templates`. 
20. Kemudian, saya menambahkan berkas `main.html` dengan nama aplikasi, nama, dan kelas. Berikut adalah kode yang saya tambahkan.
    ```
    <h1>{{ app_name }}</h1>

    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ```
21. Setelah mendefinisikan template, kita perlu mengintegrasikannya dengan view. Untuk itu, pada  berkas `views.py` pada direktori aplikasi `main`, saya menambahkan fungsi `show_main` yang akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai dengan template. Di dalamnya, saya menambahkan *dictionary* yang berisi data yang akan dikirimkan ke tampilan, mencakup nama aplikasi, nama, dan kelas. Berikut adalah kode yang saya tambahkan.
    ```
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name' : 'Bungalapak',
            'name' : 'Khansa Khairunisa',
            'class' : 'PBP C'
        }

        return render(request, "main.html", context)
    ```
    Pertama, saya mengimpor fungsi `render` dari modul `django.shortcuts` agar dapat melakukan render pada tampilan HTML menggunakan data yang ada. Kemudian, pada fungsi `show_main`, terdapat dictionary `context` yang berisi data yang ingin saya tampilkan pada aplikasi saya. Setelah itu, saya mengembalikan `render(request, "main.html", context)`, yang di mana fungsi `render()` ini akan me-render data pada `context` ke template `main.html` agar ditampilkan sebagai data yang dinamis. 

#### Membuat routing pada urls.py aplikasi main
22. Agar aplikasi `main` dapat dijalankan pada proyek, kita perlu melakukan konfigurasi pada aplikasi `main` itu sendiri. Untuk itu, saya membuat berkas `urls.py` di dalam direktori aplikasi `main` dan menambahkan berkas dengan kode berikut.
    ```
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    Untuk mendefinisikan pola URL aplikasi `main`, kita menggunakan `path` dari `django.urls` dan memanggil `path('', show_main, name="show_main")` untuk mendefinisikan fungsi `show_main` dari `main.views` sebagai tampilan yang akan dimunculkan ketika URL aplikasi diakses.

#### Melakukan deployment ke PWS
23. Untuk melakukan deployment ke PWS, saya membuka website PWS dan membuat proyek baru bernama `bungalapak`. 
24. Kemudian, saya menambahkan URL deployment PWS pada variabel `ALLOWED_HOSTS` di berkas `settings.py`. 
25. Setelahnya, saya melakukan `add`, `commit`, dan `push` perubahan tersebut ke *repository* GitHub
26. Setelah melakukan push, saya menjalankan perintah yang terdapat pada informasi *Project Command* di halaman PWS. 
27. Kemudian, saya menjalankan perintah berikut.
    ```
    git branch -M master
    ```
28. Setelah menunggu beberapa menit, aplikasi saya sudah terdeploy dan dapat diakses melalui tautan deployment PWS.

### Bagan alur MVT
![MVT Diagram](images/mvt_diagram.png)
Proses dimulai ketika client atau browser mengirimkan permintaan HTTP ke ke server. Permintaan ini diarahkan ke URL routing yang didefinisikan dalam berkas `urls.py`. Berdasarkan URL yang diminta, Django akan mengarahkan permintaan ini ke fungsi atau kelas yang sesuai di berkas `views.py`. Fungsi view ini kemudian melakukan *query* ke basis data menggunakan model yang didefinisikan di berkas `models.py`, untuk mengakses atau memanipulasi data yang diperlukan. Data yang diperoleh selanjutnya diproses dan diteruskan ke template HTML, yang ditentukan dalam berkas template, seperti `main.html`. Template ini akan me-render data menjadi format HTML yang kemudian dikirimkan sebagai respons dari fungsi view kepada client, sehingga client dapat melihat halaman yang diminta. 

### Fungsi git dalam pengembangan perangkat lunak
Git merupakan sistem kontrol versi (Version Control System) yang berfungsi untuk melacak setiap perubahan pada kode dalam pengembangan perangkat lunak, memungkinkan pengembang untuk bekerja secara kolaboratif, mengelola proyek secara efisien, dan menghindari konflik. Setiap perubahan kode akan tersimpan di dalam *history* yang dapat diakses ataupun di-revert jika diperlukan. Selain itu, pengembang juga dapat bekerja dalam branch terpisah (branching) dan menggabungkan perubahan tersebut ke dalam kode utama (merging), sehingga setiap anggota tim dapat bekerja pada repositori yang sama secara bersamaan. 

### Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django dijadikan permulaan pembelajaran pengembangan perangkat lunak terutama pada mata kuliah Pemrograman Berbasis Platform karena framework ini di tulis dalam bahasa Python, yang di mana sudah kami pelajari dari perkuliahan di semester satu. Selain itu, Django memiliki struktur yang lengkap, terorganisir, dan ramah bagi pemula. Django mengikuti pola *Model-View-Template* (MVT) yang memudahkan pengguna dalam memahami arsitektur aplikasi website. Django juga memiliki fitur atau modul lainnya, seperti autentikasi pengguna, pengelolaan URL, dan manajemen basis data (ORM).

### Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai *Object-Relational Mapping* (ORM) karena berfungsi untuk memetakan objek Python ke struktur basis data. Dengan ORM, tabel dalam basis data direpresentasikan sebagai kelas, dan kolom tabel sebagai atribut kelas. Ini memungkinkan pengembang untuk berinteraksi dengan basis data menggunakan pemrograman Python, tanpa perlu menulis SQL secara langsung, sehingga memudahkan pengelolaan data dan menjaga kode agar tetap konsisten dan mudah dipahami. 