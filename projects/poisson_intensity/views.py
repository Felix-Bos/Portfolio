from django.shortcuts import render


def project_detail(request):
    return render(request, "poisson_intensity/detail.html")
