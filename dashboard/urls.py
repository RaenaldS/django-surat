from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",dashboard, name="dashboard"),
    path("suket-belum-menikah/",suketbelummenikah,  name="suketbelummenikah"),
    path("suket-belum-menikah/edit/<int:id>",edit_suketbelummenikah,  name="edit_suketbelummenikah"),
    path("suket-belum-menikah/delete/<int:id>",delete_suketbelummenikah,  name="delete_suketbelummenikah"),
    path("suket-tidak-mampu/",sukettidakmampu,  name="sukettidakmampu"),
    path("suket-tidak-mampu/edit/<int:id>",edit_sukettidakmampu,  name="edit_sukettidakmampu"),
    path("suket-tidak-mampu/delete/<int:id>",delete_sukettidakmampu,  name="delete_sukettidakmampu"),
    path("skck/",skck,  name="skck"),
    path("skck/edit/<int:id>",edit_skck,  name="edit_skck"),
    path("skck/delete/<int:id>",delete_skck,  name="delete_skck"),
    path("suket-ktp-beda-nama/",suketktpbedanama,  name="suketktpbedanama"),
    path("suket-ktp-beda-nama/edit/<int:id>",edit_suketktpbedanama,  name="edit_suketktpbedanama"),
    path("suket-ktp-beda-nama/delete/<int:id>",delete_suketktpbedanama,  name="delete_suketktpbedanama"),
    path("suket-ahli-waris/",suketahliwaris,  name="suketahliwaris"),
    path("suket-ahli-waris/edit/<int:id>",edit_suketahliwaris,  name="edit_suketahliwaris"),
    path("suket-ahli-waris/delete/<int:id>",delete_suketahliwaris,  name="delete_suketahliwaris"),
    path("suket-MTQ/",suketMTQ,  name="suketMTQ"),
    path("suket-MTQ/edit/<int:id>",edit_suketMTQ,  name="edit_suketMTQ"),
    path("suket-MTQ/delete/<int:id>",delete_suketMTQ,  name="delete_suketMTQ"),
    path("suket-kehilangan/",suketkehilangan,  name="suketkehilangan"),
    path("suket-kehilangan/edit/<int:id>",edit_suketkehilangan,  name="edit_suketkehilangan"),
    path("suket-kehilangan/delete/<int:id>",delete_suketkehilangan,  name="delete_suketkehilangan"),
    path("suket-kelahiran/",suketkelahiran,  name="suketkelahiran"),
    path("suket-kelahiran/edit/<int:id>",edit_suketkelahiran,  name="edit_suketkelahiran"),
    path("suket-kelahiran/delete/<int:id>",delete_suketkelahiran,  name="delete_suketkelahiran"),
    path("suket-kematian/",suketkematian,  name="suketkematian"),
    path("suket-kematian/edit/<int:id>",edit_suketkematian,  name="edit_suketkematian"),
    path("suket-kematian/delete/<int:id>",delete_suketkematian,  name="delete_suketkematian"),
    path("suket-penghasilan-tidak-tetap/",suketpenghasilantidaktetap,  name="suketpenghasilantidaktetap"),
    path("suket-penghasilan-tidak-tetap/edit/<int:id>",edit_suketpenghasilantidaktetap,  name="edit_suketpenghasilantidaktetap"),
    path("suket-penghasilan-tidak-tetap/delete/<int:id>",delete_suketpenghasilantidaktetap,  name="delete_suketpenghasilantidaktetap"),
    path("suket-usaha/",suketusaha,  name="suketusaha"),
    path("suket-usaha/edit/<int:id>",edit_suketusaha,  name="edit_suketusaha"),
    path("suket-usaha/delete/<int:id>",delete_suketusaha,  name="delete_suketusaha"),
    path("suket-vaksin-nikah/",suketvaksinnikah,  name="suketvaksinnikah"),
    path("suket-vaksin-nikah/edit/<int:id>",edit_suketvaksinnikah,  name="edit_suketvaksinnikah"),
    path("suket-vaksin-nikah/delete/<int:id>",delete_suketvaksinnikah,  name="delete_suketvaksinnikah"),
    path("suket-pindah-nikah/",suketpindahnikah,  name="suketpindahnikah"),
    path("suket-pindah-nikah/edit/<int:id>",edit_suketpindahnikah,  name="edit_suketpindahnikah"),
    path("suket-pindah-nikah/delete/<int:id>",delete_suketpindahnikah,  name="delete_suketpindahnikah"),
    path("suket-rekomendasi-kelompok-tani/",suketrekkeltani,  name="suketrekkeltani"),
    path("suket-rekomendasi-kelompok-tani/edit/<int:id>",edit_suketrekkeltani,  name="edit_suketrekkeltani"),
    path("suket-rekomendasi-kelompok-tani/delete/<int:id>",delete_suketrekkeltani,  name="delete_suketrekkeltani"),
    path("tambah-pengumuman/", pengumuman, name="pengumuman"),
    path("tambah-pengumuman/edit/<int:id>", edit_pengumuman, name="edit_pengumuman"),
    path("tambah-pengumuman/delete/<int:id>", delete_pengumuman, name="delete_pengumuman")
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)