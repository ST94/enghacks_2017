from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^major/', views.majors, name="majors-api"),
    #url(r'^option/', views.options, name="options-api"),
   	#url(r'^search/', views.search, name="search-api"),
]

