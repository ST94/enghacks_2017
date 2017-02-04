from django.shortcuts import render


def index(request):
    args = {
        'site_title': 'Homepage',
    }
    return render(request, "website/index.html", args)
