import json

from courses.models import *
from django.http import HttpResponse
from django.core import serializers

def majors(request):
    data = {
        'major': [d.name for d in Course.objects.all()]
    }
    return HttpResponse(json.dumps(data), content_type="application/json")


def options(request):
    data = serializers.serialize("json", Option.objects.all())
    return HttpResponse(data, content_type="application/json")


def search(request):
    url_params = request.GET.QueryDict
    if url_params["major"] is not None and url_params["option"] is not None:
        major = url_params["major"]
        option = url_params["option"]
        data = Course.objects.filter(Major=major, Option=option)
        
    

