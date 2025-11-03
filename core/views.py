from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def cv(request):
    return render(request, "core/cv.html")


def contact(request):
    return render(request, "core/contact.html")
