# Samuel Farrel | 2206826614 | PBP-D

# TUGAS 2

## Link Aplikasi
#### SF Autoparts
[Link](https://sfautoparts.adaptable.app/main/) menuju aplikasi

## Cara mengimplementasikan checklist :
1. Membuat project django dengan virtual enviroment pada directory yang sudah dipilih untuk project:
   - Mengaktifkan virtual enviroment agar tidak menganggu dependencies lain, dengan command:
   
   ```
   env\Scripts\activate.bat
   ```

   - Membuat file `requirements.txt` pada direktori yang sama berisi dependencies yang perlu diinstall untuk project Django
   - Menginstall dependencies dengan command `pip install -r requirements.txt`
   - Menginisiasi project django baru dengan command `django-admin startproject sf_autoparts`
   - Mengubah setting `ALLOWED_HOST` pada `settings.py` dengan menambahkan `"*"` untuk allow host deployment
   - Membuat file `.gitignore` berisi daftar file yang akan diignore oleh aktivitas Github (`pull,push,commit`)
   
2. Membuat aplikasi `main`
   - Menginisiasi aplikasi `main` dengan command `python manage.py startapp main`
   - Membuat folder baru bernama `templates` pada folder aplikasi `main`
   - Membuat file `main.html` pada folder `templates`
     - `main.hmtl` akan menjadi tampilan utama website yang ditampilkan kepada pengguna

3. Routing agar dapat menjalankan aplikasi `main`
   - Membuat file `urls.py` pada folder aplikasi `main` yang berisi:
      - ```
        app_name = main
        urlpatterns = [
                      path('', show_main, name='show_main'),
        ]
        ```
   - Mengedit file `urls.py` pada folder `sf_autoparts` (folder project):
     - Menambahkan `path('main/', include('main.urls'))` pada list `urlpatterns`
    
4. Membuat model `item` pada aplikasi `main`
   - Menginisiasi `item` dengan kode `class Item(models.Model):`, dan dengan attribute:
     - `name` berupa `CharField`
     - `amount` berupa `IntegerField`
     - `description` berupa `TextField`
     - `car` berupa `CharField`
     - `production_date` berupa `DateField`
     - `price` berupa `IntegerField`
   - Setelah selesai mengedit model, saya melakukan migrasi model dengan command
     `python manage.py makemigrations`
   - Setelah migrasi, apply migration ke database dengan command `python manage.py migrate`

5. Melakukan perubahan pada file `views.py` dengan :
   - Membuat fungsi `show-main` yang:
     - memiliki dictionary bernama `context` berisi data yang akan ditampilkan di html yaitu `nama_aplikasi`, `nama`, dan `kelas`
     - mereturn fungsi `render(request, "main.html", context)` untuk menampilkan `main.html` menggunakan data dari `context` ketika ada `request` dari user.

6. Mendeploy project melalui `adaptable.io`
   - Melakukan `add,push,commit` changes pada github project
   - Mendeploy project via adaptable dengan settings sesuai tutorial
  
## Bagan request client ke web aplikasi berbasis Django dan responnya
<img src="/Others/Tugas 2/bagan django.jpg">
   

## Mengapa kita menggunakan virtual enviroment?
- Virtual enviroment kita gunakan ketika kita ingin menggunakan dependencies yang berbeda-beda pada tiap project yang kita buat di OS (operating system) yang sama. Dengan mengaktifkan virtual enviroment, dependencies suatu project berada pada enviroment yang terpisah sehingga tidak terjadi bentrok dengan project lainnya.
- Sehingga, kita tetap dapat membuat project Django tanpa virtual enviroment, tetapi ada kemungkinan dependencies bentrok dengan project lainnya.

## Perbedaan MVC, MVT, dan MVVM
- MVC :
  - **Model**       : mengelola data dan berinteraksi dengan database      
  - **View**        : menampilkan respon sebagai tanggapan pada input pengguna
  - **Controller**  : menerima input dari pengguna dan mengopernya kepada view atau model
    
- MVT :
  - **Model**       : memiliki fungsi yang sama seperti pada MVC
  - **View**        : fungsinya juga untuk menampilkan respon, tetapi respopn yang ditampilkan berupa template HTML yang diberikan data
  - **Template**    : template HTML dengan data yang diambil dari model, dan akan ditampilkan oleh view
  
- MVVVM :
  - **Model**       : sama seperti pada MVC dan MVT
  - **View**        : sama seperti pada MVC dan MVT
  - **View Model**  : berfungsi sebagai penghubung antara model dan view, mengatur data yang akan ditampilkan pada tampilan

Perbedaan yang terdapat pada ketiga arsitektur teresebut memiliki kelebihan dan kekurangan masing-masing, sehingga pemilihan arsitektur development disesuaikan dengan framework yang digunakan dan aplikasi yang akan dibuat


# TUGAS 3
## Perbedaan Form `post` dan `get` pada Django
- Post :
  - Data yang dikirim oleh pengguna tidak ditampilkan pada url, sehingga form ini cocok untuk informasi sensitif seperti username atau password karena lebih aman
  - Tidak memiliki batasan kapasitas data
  - Form post dikirim secara langsung server, tanpa disimpan pada _cache_ browser
- Get :
  - Data dapat dilihat dalam URL (data sebagai parameter URL), sehingga tidak cocok untuk data sensitif karena lebih rentan
  - Memiliki batas kapasitas data
  - Dapat di-_cache_ sehingga jika suatu proses terulang, akan lebih cepat prosesnya
 
## Perbedaan Utama XML, JSON, dan HTML
- **XML** biasanya digunakan untuk proses pengiriman data yang kompleks karena XML dapat memiliki struktur yang sangat kompleks dan spesifik
- **JSON** sangat cocok untuk proses data yang ringan pada web atau aplikasi karena JSON memiliki sintaks yang mudah untuk dibaca dan kompatibel dengan banyak bahasa
- **HTML** digunakan untuk membuat dan menampilkan (merender) tampilan web kepada pengguna

## Mengapa JSON Sering Digunakan dalam pertukaran data antara aplikasi web modern?
Seperti yang sudah saya tuliskan pada jawaban pertanyaan sebelumnya, JSON sangat mudah untuk dibaca manusia dan memiliki kompatibel dengan banyak bahasa pemrograman. JSON juga cocok untuk framework yang digunakan oleh web modern serta platform server. Kemudahan yang diberikan JSON kepada pengguna adalah alasan yang membuat JSON sering digunakan dalam pertukaran data web modern.
  
## Cara Mengimplementasikan Checklist :
1. Membuat form untuk menginput barang pada aplikasi:
   - Pada folder aplikasi `main`, saya membuat file `forms.py` yaitu form yang akan menginput item baru dengan data sesuai yang diinput
     - `forms.py` memiliki class ItemForm sebagai berikut:
     
     ```python
     class ItemForm(ModelForm):
     class Meta:
        model = Item
        fields = ['name', 'amount', 'description','car','price']
     ```

     - model merupakan bentuk objek yang akan disimpan ketika form disubmit
     - fields adalah field dari model Item yang akan diminta inputnya pada form  

   -  Membuat file `create_item.html` pada folder `template` di folder app `main`:
        - File ini akan menampilkan form dalam bentuk tabel, berdasarkan `fields` yang sudah kita tulis pada `forms.py`
        - `create_item.html` berisi kode berikut:
     
        ```html
         {% extends 'form.html' %} 
         
         {% block content %}
         <h1>Add New Item</h1>
         
         <form method="POST">
             {% csrf_token %}
             <table>
                 {{ form.as_table }}
                 <tr>
                     <td></td>
                     <td>
                         <input type="submit" value="Add Item"/>
                     </td>
                 </tr>
             </table>
         </form>
         
         {% endblock %}
        ```
   - Membuat function `create_item` pada `views.py` sebagai berikut:
     ```python
     def create_item(request):
       form = ItemForm(request.POST or None)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "create_item.html", context)
     ```
   - Memodifikasi function `show_main` pada `views.py` dengan menambahkan `'items' : items` pada `context`:
     - `items = Item.objects.all()` --> items merupakan semua object Item yang ada

2. Menambahkan 5 Fungsi `views` untuk melihat daftar objek:
   - Membuat funsgi pada `views.py` untuk masing-masing format:
     - HTML (sudah pernah dibuat sebelumnya, hanya ada beberapa tambahan):
       ```python
       def show_main(request):
          items = Item.objects.all()
          
          context = {
              'nama_aplikasi':'SF Autoparts',
              'nama': 'Samuel Farrel',
              'kelas': 'PBP-D',
              'items' : items
          }
      
          return render(request, "main.html", context)
       ```

     - XML (menampilkan seluruh item dalam bentuk XML)
       ```python
       def show_xml(request):
          data = Item.objects.all()
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
       
     - JSON (menampilkan seluruh item dalam bentuk JSON)
       ```python
       def show_json(request):
          data = Item.objects.all()
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
           
     - XML by ID (menampilkan item based on id dalam bentuk XML)
       ```python
       def show_xml_by_id(request, id):
          data = Item.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
       
     - JSON by ID (menampilkan item based on id dalam bentuk JSON)
       ```python
       def show_json_by_id(request, id):
          data = Item.objects.filter(pk=id)
          return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```
       
3. Membuat routing url untuk masing-masing `views`:
   - Mengimport seluruh `views` pada `urls.py` aplikasi `main`
     ```python
     from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
     ```
   - Menambahkan _path url_ tiap `views` pada `urlpatterns`
     ```python
      ....
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
      ....
     ```

## Screenshot Akses URL melalui Postman
- HTML:
  <img src="/Others/Tugas 3/messageImage_1695127765769.jpg">
- XML:
  <img src="/Others/Tugas 3/messageImage_1695127780661.jpg">
- JSON:
  <img src="/Others/Tugas 3/messageImage_1695127803119.jpg">
- XML by ID:
  <img src="/Others/Tugas 3/messageImage_1695127790241.jpg">
- JSON by ID:
  <img src="/Others/Tugas 3/messageImage_1695127816290.jpg">


# TUGAS 4
## Apa itu Django UserCreationForm?
- Definisi :
  Django `UserCreationForm` adalah _built-in form_ yang terdapat pada Django. Form ini dapat digunakan untuk membuat akun pengguna baru dengan field yang diisi berupa `username, password, confirm password`
- Kelebihan :
  - Mudah untuk digunakan karena form ini berupa template yang sudah disediakan Django, sehingga kita hanya perlu mengimport `UserCreationForm` dan mengimplementasikannya pada aplikasi kita
  - Cocok untuk objek `model` default user di django yaitu `User` sehingga kita tidak susah untuk menggunakan objek user yang dibuat oleh `UserCreationForm`
  - Error handling atau validasi untuk input pengguna saat membuat akun telah dihandle oleh `UserCreationForm` ini, sehingga kita tidak perlu membuat conditional branch lagi
- Kekurangan :
  - Personalisasi atau kustomisasi yang minim terhadap tampilan form
  - Tampilan yang sangat sederhana dan terkesan membosankan untuk dilihat oleh pengguna
  - Tidak bisa menambah fitur autentikasi dan field tamnbahan, untuk melakukannya kita harus mengkostumisasi `UserCreationForm` dengan membuat class baru tetapi akan memnjadi sulit dan mematahkan alasan utama untuk menggunakan `UserCreationForm`
 
##  Perbedaan antara autentikasi dan otorisasi dalam konteks Django
- Autentikasi : proses untuk memverifikasi apakah pengguna yang mencoba masuk sesuai dengan orang yang dia claim sebagai dirinya (verifikasi identitas)
- Otorisasi : pembatasan terhadap apa yang dapat dan tidak dapat dilakukan oleh user yang sudah terautentikasi untuk masuk (access rights)
- Kedua hal ini penting untuk menjaga aplikasi diakses orang-orang yang tidak seharusnya mengakses dan membuat data/privasi pengguna lebih aman karena tidak semua user dapat mengakses data masing-masing pengguna (dibatasi)

## Apa itu _cookies_ dalam aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?
- Cookies adalah data atau text berukuran kecil yang dikirim oleh web dan disimpan di browser pengguna untuk menyimpan informasi mengenai user seperti _activity, preferences, login information_
- Jika kita menggunakan _session_ pada Django:
  - Pertama, data disimpan di server terlebih dahulu.
  - Django kemudian membuat data tersebut menjadi _session key_ berupa string random sepanjang 32 character
  - String tersebut kemudian dikirim ke browser sebagai cookie bernama _sessionid_
  - Pada request berikutnya, browser akan mengirim cookie _sessionid_ kepada server dan digunakan Django untuk mengambil session data dan dapat diakses pada kode kita.

##  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
- Secara _default_, jika penggunaan _cookies_ digunakan untuk mentimpan data yang bersifat non-rahasia, maka seharusnya _cookies_ cukup aman untuk digunakan dalam aplikasi web
- Walaupun begitu, masih ada risiko yang mungkin terjadi:
  - _Unencrypted cookies_ yang digunakan untuk mentimpan data rahasia rentan untuk diretas
  - Penyisipan script berbahaya ke dalam cookies pengguna
  - _Session fixation_ yaitu penggunaan cookies session pengguna yang tidak diperbarui untuk attempt login
  - Penggunaan _cookies_ untuk membypass proses otorisas

## Cara Mengimplementasikan Checklist :
1. Mengimplementasikan fungsi registrasi, login, dan logout
   - Aktifkan virtual enviroment
   - Fungsi **registrasi**:
     - Membuat fungsi baru untuk `register` pada file `views.py` dengan memanfaatkan `UserCreationForm` yang sudah diimport dari Django
     - Fungsi akan meminta calon user untuk mengisi field username, password, dan pengulangan password
       ```python
       form = UserCreationForm()
       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Akun anda berhasil dibuat!')
               return redirect('main:login')
       context = {'form':form}
       return render(request, 'register.html', context)
       ```
     - Membuat file baru pada folder `template` untuk halaman register (form registrasi ditampilkan sebagai tabel):
       ```python
       {% extends 'form.html' %}

         {% block meta %}
             <title>Register</title>
         {% endblock meta %}
         
         {% block content %}  
         
         <div class = "login">
             
             <h1>Register</h1>  
         
                 <form method="POST" >  
                     {% csrf_token %}  
                     <table>  
                         {{ form.as_table }}  
                         <tr>  
                             <td></td>
                             <td><input type="submit" name="submit" value="Daftar"/></td>  
                         </tr>  
                     </table>  
                 </form>
         
             {% if messages %}  
                 <ul>   
                     {% for message in messages %}  
                         <li>{{ message }}</li>  
                         {% endfor %}  
                 </ul>   
             {% endif %}
         
         </div>  
         
         {% endblock content %}
       ```
     - Menambahkan _path url_ untuk fungsi register pada `urls.py`:
       ```python
       ...
       path('register/', register, name='register'),
       ...
       ```
   - Fungsi **login**:
     - Membuat fungsi baru yaitu `login_user` pada `views.py`
     - Fungsi ini memanfaatkan method bawaan Django yaitu `authenticate` untuk autentikasi user dan `login`
       ```python
       def login_user(request):
          if request.method == 'POST':
              username = request.POST.get('username')
              password = request.POST.get('password')
              user = authenticate(request, username=username, password=password)
              if user is not None:
                  login(request, user)
                  return redirect('main:show_main')
              else:
                  messages.info(request, 'Maaf, username atau password salah, mohon coba kembali.')
          context = {}
          return render(request, 'login.html', context)
       ```
     - Membuat file baru `login.html` pada folder `template` untuk halaman login
       ```python
       {% extends 'form.html' %}

         {% block meta %}
             <title>Login</title>
         {% endblock meta %}
         
         {% block content %}
         
         <div class = "login">
         
             <h1>Login</h1>
         
             <form method="POST" action="">
                 {% csrf_token %}
                 <table>
                     <tr>
                         <td>Username: </td>
                         <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                     </tr>
                             
                     <tr>
                         <td>Password: </td>
                         <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                     </tr>
         
                     <tr>
                         <td></td>
                         <td><input class="btn login_btn" type="submit" value="Login"></td>
                     </tr>
                 </table>
             </form>
         
             {% if messages %}
                 <ul>
                     {% for message in messages %}
                         <li>{{ message }}</li>
                     {% endfor %}
                 </ul>
             {% endif %}     
                 
             Belum mempunyai akun? <a href="{% url 'main:register' %}">Register Now</a>
         
         </div>
         
         {% endblock content %}
       ```
     - Menambahkan _path url_ untuk fungsi login pada `urls.py`:
       ```python
       ...
       path('login/', login_user, name='login'),
       ...
       ```
   - Fungsi **logout**
     - Membuat fungsi `logout_user` pada `vies.py` yang memanfaatkan method bawaan `logout` dari Django
     - Fungsi ini akan memproses request logout user dan mengembalikan pengguna pada halaman login
       ```python
       def logout_user(request):
          logout(request)
          return redirect('main:login')
       ```
     - Menambahkan tombol untuk logout pada `main.html` dengan menambahkan kode:
       ```python
       <a href="{% url 'main:logout' %}">
          <button>
              Logout
          </button>
       </a>
       ```
     - Menambahkan _path url_ untuk fungsi logout pada `urls.py`:
       ```python
       ...
       path('logout/', logout_user, name='logout'),
       ...
       ```
   - Merestriksi halaman main (ketika web dibuka, pengguna perlu login (autentikasi) terlebih dahulu sebelum masuk ke main page)
     - Mengimport `login_required` dari Django pada file `views.py`
     - Menambahkan kode berikut di atas method `show_main`
       ```python
       ....
       @login_required(login_url='/login')
       def show_main(request):
       ....
       ```
2. Membuat 2 akun pengguna dengan masing-masing akun mempunya 3 _dummy data_ dari model yang sudah dibuat
   - Akun pertama :
     <img src="/Others/Tugas 4/User 1.jpg">
   - Akun kedua :
     <img src="/Others/Tugas 4/User 2.jpg">

3. Menghubungi model `Item` dengan `User`
   - Mengimport `User` pada file `models.py` di folder `main`
     ```python
     from django.contrib.auth.models import User
     ```
   - Menambahkan attribute `user` pada model `Item` dengan memanfaatkan `ForeignKey`
     ```python
     ...
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     ...
     ```
   - Mengubah fungsi `create_item` pada `views.py` agar menyimpan informasi user yang membuat item terlebih dahulu, baru menyimpan item pada database
     ```python
     def create_item(request):
       form = ItemForm(request.POST or None)
   
       if form.is_valid() and request.method == "POST":
           item = form.save(commit=False)
           item.user = request.user
           item.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "create_item.html", context)
     ```
   - Mengubah fungsi `show_main` pada `views.py` agar memfilter produk sesuai user dan merubah context sesuai user yang login
     ```python
     def show_main(request):
       items = Item.objects.filter(user=request.user)
       
       context = {
           'nama_aplikasi':'SF Autoparts',
           'nama': request.user.username,
     ...
     ```
   - Lakukan migrasi pada database setelah melakukan perubahan pada model `Item` dan set _default value_ user dengan 1
3. Menerapkan cookies untuk detail informasi _user_
   - Mengimport beberapa modul dan method dari Django pada `views.py` di folder `main` yang akan diperlukan
     ```python
     import datetime
     from django.http import HttpResponseRedirect
     from django.urls import reverse
     ```
   - Mengubah kode pada fungsi `login_user` agar ketika login menyimpan informasi `last_login`:
     ```python
     ...
     if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
     ...
     ```
   - Menambahkan context untuk `last_login` pada fungsi `show_main` dengan
     ```python
     context={
     ...
     'last_login':request.COOKIES['last_login'],
     ...
     }
     ```
   - Mengubah kode pada fungsi `logout_user` agar cookies di-_delete_ ketika melakukan logout
     ```python
     def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
     ```
   - Menampilkan informasi last login pada `main` page pengguna, dengan menambahkan
     ```python
     ...
     <h5>Sesi terakhir login: {{ last_login }}</h5>
     ...
     ```

# TUGAS 5
## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
- Element Selector (penulisan tidak diawali apapun):
  - Untuk memilih semua elemen dengan tag yang sudah dipilih (contoh memilih semua elemen `h1`)
  - Cocok digunakan jika kita ingin mengkostumisasi elemen yang memiliki tag yang sama dengan gaya yang sama

- Class Selector (penulisan diawali .) :
  - Untuk memilih semua elemen dengan class yang sama sesuai yang dipilih (contoh memilih semua elemen `p` yang memiliki class `highlighted`)
  - Cocok digunakan untuk memberikan style yang sama pada beberapa elemen dengan class yang sama

- Id Selector (penulisan diawali .) :
  - Untuk memilih elemen dengan ID yang dipilih, ID bersifat unik dalam satu page sehingga hanya 1 elemen yang dipilih
  - Cocok digunakan jika ingin memberikan suatu elemen kostumisasi yang berbeda dari yang lain (style khusus)

- Universal selector (penulisan dengan *):
  - Untuk memilih seluruh elemen yang ada pada HTML
  - Digunakan secara lebih berhati-hati karena dapat mempengaruhi seluruh halaman
 
## Penjelasan HTML5 Tag
- `<header>` : Digunakan untuk mendefinisikan header atau bagian atas dari sebuah elemen HTML, sering digunakan untuk menyertakan judul, logo, dan navigasi situs
- `<nav>` : Digunakan untuk menandakan bagian navigasi dari sebuah dokumen, sering digunakan untuk membuat menu atau daftar tautan ke halaman-halaman lain dalam situs
- `<aside>` : Digunakan untuk mengelompokkan konten yang berkaitan dengan konten utama, tetapi dapat dianggap sebagai konten sampingan atau tambahan (semacam side box)
- `<section>` : Digunakan untuk mengelompokkan konten dalam sebuah dokumen HTML. Biasanya digunakan untuk mengelompokkan konten yang terkait dalam sebuah bagian halaman
- `<article>` : Digunakan untuk menunjukkan bahwa konten tersebut adalah artikel yang berdiri sendiri
- `<footer>`: Digunakan untuk mendefinisikan footer atau bagian bawah dari sebuah elemen HTML
- `<video>` : Digunakan untuk memasukkan pemutaran video dalam halaman web.
- `<audio>` : Digunakan untuk memasukkan pemutaran audio dalam halaman web.

## Perbedaan Margin dan Padding
- Margin :
  - Margin merupakan ruang yang ada di bagian luar elemen, atau jarak antara suatu elemen dengan elemen-elemen di sekitarnya
  - Dengan begitu, margin juga mempengaruhi tata letak elemen di sekitarnya
  - Margin berupa fill kosong (tidak mempunyai warna yang dapat dilihat)
    
- Padding :
  - Padding merupakan ruang di dalam elemen, atau jarak antara batas elemen (outline) dengan konten di dalamnya
  - Padding hanya memengaruhi tata letak elemen itu sendiri dan kontennya
  - Padding memiliki fill yang dapat diberi warna
 
## Perbedaan Tailwind dan Bootstrap
- Tailwind :
  - Komponen tidak siap pakai, tampilan page dan styling kita buat dari utility class yang telah disediakan oleh Tailwind
  - Tailwind menghasilkan file yang lebih kecil karena hanya menggunakan class yang dibutuhkan
  - Tailwind memiliki kustomisasi yang lebih besar dan fleksibel
  - Cocok digunakan jika ingin membuat tampilan web yang memiliki tampilan sesuai keinginan dan memiliki waktu lebih banyak untuk developnya
- Bootstrap :
  - Menyediakan komponen siap pakai yang dapat kita gunakan dan kustomisasi lebih lanjut
  - Ukuran file bootstrap cenderung lebih besar karena banyaknya komponen yang disediakan
  - Tampilan template bootstrap sudah cukup baik dan masih dapat dikostumisasi lebih lanjut
  - Cocok digunakan jika kita ingin membuat tampilan web dengan cepat dan konsisten dengan template bawaan
 
## Cara implementasi checklist
1. Menginstall bootstrap pada aplikasi
   - Menambahkan kode berikut pada template `base.html` di `root` folder yang nantinya akan kita extend untuk template aplikasi kita
     ```html
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
     <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
     ```
2. Mengkostumisasi template pada aplikasi `main` dengan mengganti dan menambahkan elemen bootstrap dan membuatnya berfungsi
   - `create_item.html` dikostumisasi dengan membuat form dengan tampilan yang lebih menarik menggunakan card dan background gradient
     ```html
     {% extends 'base.html' %}
      {% block meta %}
      <style>
          .gradient-custom {
              /* fallback for old browsers */
            background: #2844a1;
            max-width: 100%; /* Make it full-width on smaller screens */
            margin: 0 auto; /* Center the container horizontally */
            
            /* Chrome 10-25, Safari 5.1-6 */
            background: -webkit-linear-gradient(to right, #2844a1,rgb(189, 229, 255));
            max-width: 100%; /* Make it full-width on smaller screens */
            margin: 0 auto; /* Center the container horizontally */
            
            /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
            background: linear-gradient(to right, rgb(40, 68, 161),rgb(189, 229, 255));
            color: white;
            max-width: 100%; /* Make it full-width on smaller screens */
            margin: 0 auto; /* Center the container horizontally */
            padding : 20px;
            min-height: 100vh;
          }
      </style>
      {% endblock meta %}
      
      {% block content %}
      <section class="gradient-custom">
          <div class="px-4 py-5 px-md-5 text-center text-lg-start">
            <div class="container">
              <div class="row gx-lg-5 align-items-center">
                <div class="col-lg-6 mx-auto mb-5 mb-lg-0">
                  <div class="card">
                    <div class="card-body py-5 px-md-5" >
                      <h2 class="fw-bold mb-2 text-uppercase" style="text-align: center; color:#2844a1">Add New Product</h2>
                      <br><br>
                      <form method="POST" >  
                      {% csrf_token %}  
                      <div class="row">
          
                          <!-- Name input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Nama produk anda :</label>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="text" name="name" class="form-control" placeholder="Name" />
                          </div>
      
                          <!-- Amount input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Jumlah produk yang ingin dimasukkan :</label>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="text" name="amount" class="form-control" placeholder="Amount" />
                          </div>
      
                          <!-- Description input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Deskripsi produk anda :</label>
                          <label class="form-label" for="form3Example2" style="color: rgb(166, 166, 166);">Maksimal 255 character</label>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="text" name="description" class="form-control" placeholder="Description" />
                          </div>
      
                          <!-- Car input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Mobil yang cocok untuk produk anda :</label>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="text" name="car" class="form-control" placeholder="Car" />
                          </div>
      
                          <!-- Price input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Harga produk :</label>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="text" name="price" class="form-control" placeholder="Price" />
                          </div>
      
          
                          <!-- Submit button -->
                          <button type="submit" name="submit" value="Add Item" class="btn btn-primary btn-block mb-4" style="background-color: #2844a1 ;color:#ffffff">Add Item</button>  
      
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </section>
      {% endblock %}
     ```
   - `login.html` dikostumisasi dengan membuat form dengan tampilan yang lebih menarik dan background gradient
     ```html
     {% extends 'base.html' %}

      {% block meta %}
          <title>Login</title>
          <style>
            .gradient-custom {
              /* fallback for old browsers */
              background: #2844a1;
              
              /* Chrome 10-25, Safari 5.1-6 */
              background: -webkit-linear-gradient(to right, #2844a1, aqua);
              
              
              /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
              background: linear-gradient(to right, rgb(40, 68, 161),aqua);
              min-height: 100vh;
              }
              
          </style>
            {% endblock meta %}
            
            {% block content %}
            
            <div class = "login">
              <section class="vh-100 gradient-custom">
                <div class="container py-5 h-100">
                  <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-12 col-md-8 col-lg-6 col-xl-5">
                      <div class="card" style="background-color: #ffffff; border-radius: 1rem; color: #2844a1;">
                        <div class="card-body p-5 text-center">
                          <div class="mb-md-5 mt-md-4 pb-5">
                            <div>
                              <form method="POST" action="">
                                {% csrf_token %}
                                <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                                <p class="text-50 mb-5" style="color: black;">Silahkan masukkan username dan password anda!</p>
                  
                                <div class="form-outline form-white mb-4">
                                  <input type="text" name="username" placeholder="Username" class="form-control" />
                                </div>
                  
                                <div class="form-outline form-white mb-4">
                                  <input type="password" name="password" placeholder="Password" class="form-control"/>
                                </div>
            
                                {% if messages %}
                                  {% for message in messages %}
                                      <p>{{ message }}</p>
                                  {% endfor %}
                                {% endif %}    
                  
                                <button class="btn btn-lg px-5" type="submit" value="Login" style="outline: #2844a1; ">Login<a ></button>
                  
                              </form>
                      
                          </div>
                        </div>
              
                          <div>
                            <p class="mb-0">Belum mempunyai akun? <a href="{% url 'main:register' %}" class="text-aqua-50 fw-bold">Buat Akun</a>
                            </p>
                          </div>
              
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
            </div>
            
         {% endblock content %}
     ```
   - `main.html` dikostumisasi agar produk-produk ditampilkan dalam bentuk card dengan tombol di dalamnya dan tampilan dibuat lebih clean
     ```html
     {% extends 'base.html' %}

      {% block meta %}
          <title>Register</title>
          <style>
              .gradient-custom {
                /* fallback for old browsers */
              background: #2844a1;
              max-width: 100%; /* Make it full-width on smaller screens */
              margin: 0 auto; /* Center the container horizontally */
              
              /* Chrome 10-25, Safari 5.1-6 */
              background: -webkit-linear-gradient(to right, #2844a1,rgb(189, 229, 255));
              max-width: 100%; /* Make it full-width on smaller screens */
              margin: 0 auto; /* Center the container horizontally */
              
              /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
              background: linear-gradient(to right, rgb(40, 68, 161),rgb(189, 229, 255));
              color: white;
              max-width: 100%; /* Make it full-width on smaller screens */
              margin: 0 auto; /* Center the container horizontally */
              padding : 20px;
              min-height: 100vh;
              }
            </style>
      {% endblock meta %}
      
      {% block content %}
      <section class="gradient-custom">
          <br>
          <h2>Welcome, </h2>
          <h3>{{nama}}</h3>
          <h3>{{kelas}}</h3>
      
          <br />
          
          <h3>Inventory Status: </h3>
          <p>Kamu menyimpan {{ items|length }} item pada aplikasi ini</p>
      
          <br>
          <a href="{% url 'main:create_item' %}">
              <button href="{% url 'main:create_item' %}" class="btn" style="background-color: rgb(123, 215, 215) ;color:#ffffff">Tambahkan Produk Baru</button>
          </a>
          <br><br>
          <br />
      
          <div class="row">
              {% for item in items %}
                  <div class="col-md-4 mb-4">
                      <div class="card" {% if forloop.last %}style="background-color: rgb(189, 229, 255)"{% endif %}>
                          <div class="card-body">
                              <h5 class="card-title">{{ item.name }}</h5>
                              <p class="card-text">
                                  <strong>Amount:</strong> {{ item.amount }}<br>
                                  <strong>Description:</strong> {{ item.description }}<br>
                                  <strong>Car:</strong> {{ item.car }}<br>
                                  <strong>Date Made:</strong> {{ item.production_date }}<br>
                                  <strong>Price:</strong> {{ item.price }}<br>
                              </p>
                              <form method="POST" action="{% url 'main:decrement_item' item.id %}">
                                  {% csrf_token %}
                                  <button type="submit" class="btn" style="margin: 5px; background-color: #2844a1 ;color:#ffffff">Kurangi Stok</button>
                              </form>
                              <form method="POST" action="{% url 'main:increment_item' item.id %}">
                                  {% csrf_token %}
                                  <button type="submit" class="btn" style="margin: 5px; background-color: #2844a1 ;color:#ffffff">Tambah Stok</button>
                              </form>
                              <form method="POST" action="{% url 'main:delete_item' item.id %}">
                                  {% csrf_token %}
                                  <button type="submit" class="btn" style="margin: 5px; background-color: #a12828 ;color:#ffffff">Hapus</button>
                              </form>
                          </div>
                      </div>
                  </div>
              {% endfor %}
          </div>
      </section>
      {% endblock content %}
     ```
   - `register.html`dikostumisasi dengan membuat form dengan tampilan yang lebih menarik menggunakan card dan background gradient dengan beberapa elemen tambahan
     ```html
     {% extends 'base.html' %}

      {% block meta %}
          <title>Register</title>
          <style>
              .gradient-custom {
                /* fallback for old browsers */
                background: #2844a1;
                max-width: 100%; /* Make it full-width on smaller screens */
                margin: 0 auto; /* Center the container horizontally */
                padding : 20px;
                
                /* Chrome 10-25, Safari 5.1-6 */
                background: -webkit-linear-gradient(to right, #2844a1, aqua);
                max-width: 100%; /* Make it full-width on smaller screens */
                margin: 0 auto; /* Center the container horizontally */
                padding : 20px;
                
                
                /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
                background: linear-gradient(to right, rgb(40, 68, 161),aqua);
                max-width: 100%; /* Make it full-width on smaller screens */
                min-height: 100vh;
                margin: 0 auto; /* Center the container horizontally */
                padding : 20px;
              }
            </style>
      {% endblock meta %}
      
      {% block content %}  
      <section class="gradient-custom">
          <div class="px-4 py-5 px-md-5 text-center text-lg-start">
            <div class="container">
              <div class="row gx-lg-5 align-items-center">
                <div class="col-lg-6 mb-5 mb-lg-0">
                  <h1 class="my-5 display-3 fw-bold ls-tight" style="color: #ffffff">
                    Your first step <br />
                    <span class="text" style="color: aqua;">in SF Autoparts</span>
                  </h1>
                  <p style="color: hsl(0, 0%, 100%)">
                      a robust and efficient software solution designed to streamline the management of automobile parts. 
                      SF Autoparts effectively organize, track, and manage their extensive range of automobile components and accessories.
                  </p>
                </div>
        
                <div class="col-lg-6 mb-5 mb-lg-0">
                  <div class="card">
                    <div class="card-body py-5 px-md-5" >
                      <h2 class="fw-bold mb-2 text-uppercase" style="text-align: center; color:#2844a1">Register</h2>
                      <br><br>
                      <form method="POST" >  
                      {% csrf_token %}  
                      <div class="row">
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Your desired account username :</label>
                          <br>
                          <br>
                          <div class="col-md-6 mb-4">
                              <div class="form-outline">
                              <input type="text" name="username" class="form-control" placeholder="Username"/>
                              </div>
                          </div>
                          </div>
                          <br>
          
                          <!-- Password input -->
                          <label class="form-label" for="form3Example2" style="font-weight: bold;">Password for your account :</label>
                          <label class="form-label" for="form3Example2" style="color: rgb(166, 166, 166);">Use an uncommon one and don't be too similar with your private information. Can't be entirely numeric and contains at least 8 character</label>
                          <br>
                          <br>
                          <div class="form-outline mb-4">
                          <input type="password" name="password1" class="form-control" placeholder="Password" />
                          </div>
      
                          <!-- Password input -->
                          <div class="form-outline mb-4">
                          <input type="password" name="password2" class="form-control" placeholder="Repeat your password" />
                          </div>
      
                          {% if messages %}
                            {% for message in messages %}
                                <p>{{ message }}</p>
                            {% endfor %}
                          {% endif %}    
          
                          <!-- Submit button -->
                          <button type="submit" name="submit" value="Daftar" class="btn btn-primary btn-block mb-4" style="background-color: #2844a1 ;color:#ffffff">Register</button>  
      
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>      
      {% endblock content %}
     ```
3. Menambahkan navbar pada aplikasi:
   - Menambahkan kode berikut pada bagian atas block content template yang memiliki navbar
     ```html
     <nav class="navbar" style="background-color: rgb(208, 236, 255)"> 
          <div class="container-fluid">
              <a class="navbar-brand" href="#" style="font-weight: bold;">SF Autoparts</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation" >
                <span class="navbar-toggler-icon" style="color: white;"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav">
                  <a class="nav-link" href="{% url 'main:create_item' %}">Add Item</a>
                  <a class="nav-link" href="{% url 'main:logout' %}">Logout</a>
                  <br>
                  <span class="navbar-text" style="font-weight: bolder;">Sesi terakhir login: {{ last_login }}</span>
                </div>
          </div>
      </nav>
     ```

# Tugas 6
## Perbedaan asynchronous dengan synchronous programming
- Asynchronus Programming :
  - Task dieksekusi secara *non blocking* dimana task dieksekusi secara bersamaan (task dapat berjalan tanpa menunggu task lainnya selesai)
  - Memungkinkan untuk menjalankan beberapa task pada waktu yang bersamaan berguna untuk program yang akan lebih efisien jika tidak menunggu suatu task selesai terlebih dahulu
  - Melibatkan penggunaan callback, promises, atau sintaksis async/await untuk menentukan apa yang harus terjadi setelah operasi selesai, dibanding menunggu hingga selesai

- Synchronus Programming :
  - Task dieksekusi secara *blocking* dimana task dieksekusi satu per satu dan setiap task harus selesai terlebih dahulu sebelum task selanjutnya dijalankan
  - Ketika sebuah task menghadapi operasi yang mungkin memerlukan waktu, ia menunggu operasi tersebut selesai sebelum melanjutkan sehingga terkadang program dengan synchronus programming kurang efisien
  - Lebih mudah untuk ditulis dan dipahami karena eksekusi program bersifat linear (tidak menggunakan callback, dll)

## Paradigma *event-driven programming* dan contohnya
- Maksud dari paradigma *event-driven programming* adalah pendekatan pemrograman dimana eksekusi program diatur oleh *event* atau suatu kejadian yang terjadi pada aplikasi tersebut. 
- Pada *event-driven programming*, biasanya objek atau komponen yang terdapat dalam program memiliki event yang dapat memicu tindakan atau fungsi tertentu. Ketika event terjadi, program memanggil fungsi yang dipicu dengan event tersebut.
- Contohnya pada tugas ini adalah penerapan tombol add product :
  - ketika tombol dengan ID `button_add` diklik (event click terjadi), fungsi `addProduct` akan dipanggil
    ```javascript
    document.getElementById("button_add").onclick = addProduct;
    ```

## Penerapan asynchronous programming pada AJAX
- Penerapan asynchronous programming pada AJAX adalah pendekatan di mana permintaan data ke server atau operasi I/O lainnya dalam konteks web dilakukan secara asynchronous sehingga eksekusi program dapat berlanjut tanpa harus menunggu respons dari server. 
- Contohnya update konten pada suatu halaman dapat dilakukan tanpa refresh page sehingga page tetap berjalan secara responsif ketika proses berjalan.

## Fetch API dan Library JQuery
- Fetch API lebih ringan, penulisan kode asynchronus sesimpel synchronus (sintaks mudah), dibuat khusus untuk AJAX, dan merupakan *bulit-in* di banyak browser tetapi tidak didukung pada beberapa browser
- JQuery memiliki sintaks yang lebih mudah, fitur yang lebih lengkap karena dibuat bukan hanya untuk AJAX, dan memiliki *cross-browser compatibility* sehingga bekerja baik pada berbagai browser, tetapi JQuery ini memang lebih berat.

Saya pribadi lebih memilih untuk menggunakan Fetch API dalam konteks AJAX karena lebih ringan dan menurut saya sintaks yang digunakan untuk asyncronus programming dengan Fetch API juga mudah untuk dipahami, serta Fetch API memang sudah dikembangkan sedemikian rupa untuk penggunaan AJAX.

## Implementasi Checklist
1. Mengubah tugas 5 menjadi menggunakan AJAX :
  - AJAX GET :
    - Mengubah card agar mendukung AJAX GET
      ```javascript
      const cardBackground = index === items.length - 1 ? 'background-color: rgb(189, 229, 255)' : '';
      `<div class="col-md-4 mb-4">
          <div class="card" style="${cardBackground}">
              <div class="card-body">
                  <h5 class="card-title"> ${item.fields.name}</h5>
                  <p class="card-text">
                      <strong>Amount:</strong> ${item.fields.amount}<br>
                      <strong>Description:</strong> ${item.fields.description}<br>
                      <strong>Car:</strong> ${item.fields.car}<br>
                      <strong>Date Made:</strong> ${item.fields.production_date}<br>
                      <strong>Price:</strong> ${item.fields.price}<br>
                  </p>
                  <a href="decrement/${item.pk}" class="btn" style="margin: 5px; background-color: #2844a1; color: #ffffff">Kurangi Stok</a>
                  <a href="increment/${item.pk}" class="btn" style="margin: 5px; background-color: #2844a1; color: #ffffff">Tambah Stok</a>
                  <a href="delete/${item.pk}" class="btn" style="margin: 5px; background-color: #a12828; color: #ffffff">Hapus</a>
              </div>
          </div>
      </div>`;
      ```
    - Mengubah div untuk card pada main html menjadi berikut (div kosong dengan id `row_card_items` yang nantinya akan ditambahkan)
      ```html
      <div class="row" id="row_card_items">
      </div>
      ```
    - Pengambilan task menggunakan AJAX GET (menambahkan card pada template untuk tiap item yang didapat dan update counter item saat refreshItems)
      ```javascript
          async function refreshItems() {
            document.getElementById("row_card_items").innerHTML = ""
            const items= await getItems()
            let htmlString = ``;
            items.forEach((item, index) => {
                const cardBackground = index === items.length - 1 ? 'background-color: rgb(189, 229, 255)' : '';
                htmlString += `<div class="col-md-4 mb-4">
                    <div class="card" style="${cardBackground}">
                        <div class="card-body">
                            <h5 class="card-title"> ${item.fields.name}</h5>
                            <p class="card-text">
                                <strong>Amount:</strong> ${item.fields.amount}<br>
                                <strong>Description:</strong> ${item.fields.description}<br>
                                <strong>Car:</strong> ${item.fields.car}<br>
                                <strong>Date Made:</strong> ${item.fields.production_date}<br>
                                <strong>Price:</strong> ${item.fields.price}<br>
                            </p>
                            <a href="decrement/${item.pk}" class="btn" style="margin: 5px; background-color: #2844a1; color: #ffffff">Kurangi Stok</a>
                            <a href="increment/${item.pk}" class="btn" style="margin: 5px; background-color: #2844a1; color: #ffffff">Tambah Stok</a>
                            <a href="delete/${item.pk}" class="btn" style="margin: 5px; background-color: #a12828; color: #ffffff">Hapus</a>
                        </div>
                    </div>
                </div>`;
            });
            jumlahItem = items.length
            document.getElementById("row_card_items").innerHTML = htmlString
            document.getElementById("counter_item").innerHTML = `Kamu menyimpan ${jumlahItem} item pada aplikasi ini`
            document.getElementById("row_card_items").innerHTML = htmlString
        }
      ```


  - AJAX POST :
    - Membuat tombol yang membuka sebuah modal dengan form untuk menambahkan item pada `main.html`
      ```html
      <a class="nav-link" data-bs-toggle="modal" data-bs target="#exampleModal">Add Item by AJAX</a>
      ``` 
    - Modal yang akan dibuka (form untuk mengisi attribute pada item baru yang ingin dibuat)
      ```html
      <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
              <div class="modal-content">
                  <div class="modal-header">
                      <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                      <form id="form" onsubmit="return false;">
                          {% csrf_token %}
                          <div class="mb-3">
                              <label for="name" class="col-form-label">Name:</label>
                              <input type="text" class="form-control" id="name" name="name"></input>
                          </div>
                          <div class="mb-3">
                              <label for="amount" class="col-form-label">Amount:</label>
                              <input type="number" class="form-control" id="amount" name="amount"></input>
                          </div>
                          <div class="mb-3">
                              <label for="description" class="col-form-label">Description:</label>
                              <textarea class="form-control" id="description" name="description"></textarea>
                          </div>
                          <div class="mb-3">
                              <label for="car" class="col-form-label">Car:</label>
                              <input class="form-control" id="car" name="car"></input>
                          </div>
                          <div class="mb-3">
                              <label for="price" class="col-form-label">Price:</label>
                              <input class="form-control" id="price" name="price"></input>
                          </div>
                      </form>
                  </div>
                  <div class="modal-footer">
                      <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                      <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                  </div>
              </div>
          </div>
      </div>
      ```
    - Membuat fungsi baru pada `views.py` untuk menambahkan item pada database
      ```python
      @csrf_exempt
      def create_item_ajax(request):
          if request.method == 'POST':
              name = request.POST.get("name")
              amount = request.POST.get("amount")
              description = request.POST.get("description")
              car = request.POST.get("car")
              price = request.POST.get("price")
              user = request.user

              new_item = Item(name=name, amount=amount,description=description,car=car,price=price,user=user)
              new_item.save()

              return HttpResponse(b"CREATED", status=201)

          return HttpResponseNotFound()
      ```
    - Menambahkan fungsi tersebut pada routing path url pada `urls.py` dengan path `/create-ajax/`, dengan menambahkan :
      ```python
      path('create-ajax/',create_item_ajax,name='create_item_ajax')
      ```
    - Menyambungkan fungsi dengan modal yang sudah dibuat dengan menambahkan function berikut pada bagian `script` di file `main.html`
      ```javascript
          function addItem() {
            fetch("{% url 'main:create_item_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshItems)

            document.getElementById("form").reset()
            return false
        }
        document.getElementById("button_add").onclick = addItem
      ```
    - Pada kode tersebut, method addItem akan dijalankan ketika `button_add` ditekan dan setelah item diadd, card akan direfresh secara asinkronus dan form pada modal akan dikosongkan kembali

2. Melakukan setting untuk deployment sesuai dengan petunjuk tutorial 2 tetapi variable secret `DOKKU_APP_NAME` valuenya diganti menjadi `samuel-farrel-tugas`

3. Melakukan perintah `collecstatic` dengan menjalankan perintah
    ```
    python manage.py collectstatic
    ```