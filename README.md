# Bungalapak
Proyek Django untuk tugas mata Pemrograman Berbasis Platform Ganjil 2024/2025. Dibuat oleh Khansa Khairunisa - 2306153462

Link untuk PWS deployment dapat diakses [di sini](http://khansa-khairunisa31-bungalapak.pbp.cs.ui.ac.id/).

## Tugas 2 
Pada tugas ini, kami akan mengimplementasikan konsep *Model-View-Template* (MVT) pada Django

### Langkah Implementasi Checklist
Berikut adalah langkah-langkah yang saya lakukan untuk mengimplementasi checklist dari Tugas 2.

#### Membuat proyek Django
1. Buat direktori baru dengan nama `bungalapak` dan masuk ke direktori tersebut
2. Buat *virtual environment* di dalam direktori tersebut dengan menjalankan perintah berikut di terminal.
```
py -m venv env
```
3. Kemudian, aktifkan dengan menggunakan perintah berikut.
```
env\Scripts\activate
```
4. Di dalam direktori yang sama, buat berkas `requirements.txt` menggunakan IDE Visual Studio Code dan tambahkan beberapa *depedencies* yang diperlukan sebagai berikut.
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
5. Lakukan instalasi terhadap *depedencies* yang ada dengan menjalankan perintah berikut.
```
pip install -r requirements.txt
```
6. Buat proyek Django bernama `bungalapak` dengan menjalankan perintah berikut.
```
django-admin startproject bungalapak .
```
7. Tambahkan kedua string berikut pada variabel `ALLOWED_HOSTS` di berkas `settings.py` untuk keperluan deployment.
```
...
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
...
```
8. Buat *repository* GitHub baru bernama `bungalapak` dengan visibilitas *public*. 
9. Inisiasi direktori lokal `bungalapak` sebagai *repository* Git dengan menjalankan perintah berikut pada direktori `bungalapak`.
```
git init
```
10. Di dalam direktori yang sama, buat berkas `.gitignore` menggunakan IDE Visual Studio Code dan isilah berkas tersebut dengan teks berikut.
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml
.DS_Store

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod]
*$py.class

# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

# celery
celerybeat-schedule.*

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# mkdocs documentation
/site

# mypy
.mypy_cache/

# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project

# sftp configuration file
sftp-config.json

# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings

# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history
```
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

### Membuat aplikasi dengan nama main pada proyek tersebut
14. Buat aplikasi baru bernama `main` dalam proyek `bungalapak` dengan menjalankan perintah berikut.
```
python manage.py startapp main
```
15. Tambahkan string `main` pada variabel `INSTALLED_APPS` di berkas `settings.py`
```
INSTALLED_APPS = [
    ...,
    'main'
]
```