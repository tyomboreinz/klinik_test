"""klinik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from kliniks.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pegawai),
    path('pegawai', pegawai, name='pegawai'),
    path('pegawai/tambah', pegawai_tambah, name='pegawai_tambah'),
    path('pegawai/edit/<int:id_pegawai>', pegawai_edit, name='pegawai_edit'),
    path('pegawai/hapus/<int:id_pegawai>', pegawai_hapus, name='pegawai_hapus'),

    path('poli', poli, name='poli'),
    path('poli/tambah', poli_tambah, name='poli_tambah'),
    path('poli/edit/<int:id_poli>', poli_edit, name='poli_edit'),
    path('poli/hapus/<int:id_poli>', poli_hapus, name='poli_hapus'),

    path('jadwal', jadwal, name='jadwal'),
    path('jadwal/cetak', jadwal_cetak, name='jadwal_cetak'),
    path('jadwal/tambah', jadwal_tambah, name='jadwal_tambah'),
    path('jadwal/edit/<int:id_jadwal>', jadwal_edit, name='jadwal_edit'),
    path('jadwal/hapus/<int:id_jadwal>', jadwal_hapus, name='jadwal_hapus'),

    path('cetak', coba_cetak, name='cetak'),

]
