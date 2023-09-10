from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama_aplikasi':'SF Autoparts',
        'nama': 'Samuel Farrel',
        'kelas': 'PBP-D',
    }

    return render(request, "main.html", context)
