import datetime
import json
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponseNotFound, JsonResponse
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    context = {
        'nama_aplikasi':'SF Autoparts',
        'nama': request.user.username,
        'kelas': 'PBP-D',
        'items' : items,
        'last_login':request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun anda berhasil dibuat!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Maaf, username atau password salah, mohon coba kembali.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def increment_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.amount += 1
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_item(request, id):
    item = get_object_or_404(Item, pk=id)
    if item.amount > 0:
        item.amount -= 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def get_product_json(request):
    item_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', item_item))

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

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            description = data["description"],
            car = data["car"],
            amount = int(data["amount"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)