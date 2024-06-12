# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index', views.index, name='index'),
# ]


# urls.py
from django.urls import path
from notification import views

urlpatterns = [
    path('', views.index, name='index'),
]
