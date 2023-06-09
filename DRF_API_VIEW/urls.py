"""DRF_API_VIEW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from api import views
from CRUD_DRF_API_VIEW import views


# ==================================This will work with the function based API Views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('studAPI/',views.hellow_world),
#     path('stuapi/',views.studentAPI),
#     path('stuapi/<int:pk>',views.studentAPI)
# ]

#=============================== This will work with the Class Based API View==============================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuapi/',views.StudentAPI.as_view()),
    path('stuapi/<int:pk>',views.StudentAPI.as_view()),
]