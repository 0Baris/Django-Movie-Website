# MovieApp

MovieApp, Django framework kullanılarak geliştirilmiş bir film sitesidir. Bu uygulama, filmleri kategorilere göre listelemenizi, arama yapmanızı ve film detaylarını görüntülemenizi sağlar.

## Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/0baris/movieapp.git
   cd movieapp
   ```

2. Sanal bir ortam oluşturun ve etkinleştirin:
   ```bash
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # MacOS/Linux
   source env/bin/activate
   ```

3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Veritabanı migrasyonlarını uygulayın:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Yönetici kullanıcı oluşturun:
   ```bash
   python manage.py createsuperuser
   ```

6. Geliştirme sunucusunu başlatın:
   ```bash
   python manage.py runserver
   ```

7. Tarayıcınızda `http://127.0.0.1:8000/` adresine gidin.

## Proje Yapısı

- 

movies

: Uygulama ana dizini.
  - `models.py`: Veritabanı modelleri.
  - `views.py`: Görünümler.
  - `urls.py`: URL yönlendirmeleri.
  - `templates/`: HTML şablonları.
    - `index.html`: Anasayfa şablonu.
    - `movies.html`: Filmler sayfası şablonu.
    - `category.html`: Kategori sayfası şablonu.
    - `details.html`: Film detayları şablonu.
    - `partials/`: Parçalı şablonlar.
      - `_navbar.html`: Navigasyon barı.
      - `_category.html`: Kategori listesi.
      - `_movie.html`: Film kartı.

