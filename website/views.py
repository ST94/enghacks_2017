from django.http import HttpResponseForbidden
from django.shortcuts import render


def index(request):
    args = {
        'site_title': 'Homepage',
    }
    return render(request, "website/index.html", args)


def result(request):
    if request.method:
        return render(request, "website/display.html", {'site_title': 'Result'})
    else:
        return HttpResponseForbidden()
