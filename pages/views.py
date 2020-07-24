from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect('shops:catalogue')
    #return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
