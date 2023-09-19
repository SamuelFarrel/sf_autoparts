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
   - Mengimport seluruh `views.py` pada `urls.py` aplikasi `main`
     ```python
     from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
     ```
   - Menambahkan _path url_ tiap views pada `urlpatterns`
     ```python
      ....
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
      ....
     ```

## Screenshot Akses URL melalui Postman

