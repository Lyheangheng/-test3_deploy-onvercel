from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def gallery_single(request):
    return render(request, 'gallery-single.html')

def services(request):
    return render(request, 'services.html')

def starter_page(request):
    return render(request, 'starter-page.html')

# def INDEX1(request):
#     return render(request, 'INDEX1.html')