"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.logout,name='logout'),
    path('add_cof/', views.add_cof,name='add_cof'),
    path('edit_cof/', views.edit_cof,name='edit_cof'),
    path('delete_cof/', views.delete_cof,name='delete_cof'),
    path('cof/<cof_id>', views.cof_detail,name='cof_detail'),
    path('cof_ext/<cof_id>', views.add_cof_ext,name='cof_ext'),
    path('delete_cofext/', views.delete_cofext,name='delete_cofext'),
    path('edit_cofext/<cofext_id>', views.edit_cofext,name='edit_cofext'),
]
