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
