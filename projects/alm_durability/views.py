from django.shortcuts import render


def project_detail(request):
    return render(request, "alm_durability/detail.html")
