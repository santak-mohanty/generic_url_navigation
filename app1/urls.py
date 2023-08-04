from django.urls import path
from app1.views import *

app_name="app1"

urlpatterns = [
    path("page1/",page1,name="page1")
]
