from django.contrib import admin
from .models import *
# Register your models here.

class AdSuketBelumMenikah(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "ttl", "suku", "agama", "nik", "alamat", "date", "status"]

admin.site.register(SuketBelumMenikah, AdSuketBelumMenikah)

class AdSuketTidakMampu(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "ttl", "suku", "agama", "nik", "alamat", "pekerjaan", "date", "status"]

admin.site.register(SuketTidakMampu, AdSuketTidakMampu)

class AdSKCK(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "ttl", "suku", "agama", "nik", "alamat", "pekerjaan", "kawin", "pendidikanterakhir", "date", "status", "scanktp"]

admin.site.register(SKCK, AdSKCK)

class AdSuketKTPBedaNama(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "ttl", "agama", "alamat", "pekerjaan", "date", "status"]

admin.site.register(SuketKTPBedaNama, AdSuketKTPBedaNama)

class AdSuketAhliWaris(admin.ModelAdmin):
    list_display = ["penulis", "nama1", "ttl1", "alamat1", "nama2", "ttl2", "alamat2", "nama3", "ttl3", "alamat3","nama4", "ttl4", "alamat4", "date", "status"]


admin.site.register(SuketAhliWaris, AdSuketAhliWaris)

class AdSuketMTQ(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "ttl", "suku", "agama", "alamat", "pekerjaan", "date", "status"]

admin.site.register(SuketMTQ, AdSuketMTQ)

class AdSuketKehilangan(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jenis_kelamin", "umur", "alamat", "pekerjaan", "barang1", "barang2", "barang3", "tempat1", "tempat2", "date", "status"]

admin.site.register(SuketKehilangan, AdSuketKehilangan)

class AdSuketKelahiran(admin.ModelAdmin):
   list_display = [
        "penulis", 
        "namab", 
        "jenis_kelaminb", 
        "tanggal_lahirb", 
        "tempat_lahirb", 
        "agamab", 
        "alamatb", 
        "anakke", 
        "namaa", 
        "umura", 
        "pekerjaana", 
        "alamata", 
        "namai", 
        "umuri", 
        "pekerjaani", 
        "alamati", 
        "date", 
        "status", 
        "kkb", 
        "scanfcbnb", 
        "scanfcktportub", 
        "scanfcktpsaksib1", 
        "scanfcktpsaksib2", 
        "kkd", 
        "kk_ktportud", 
        "scanfcktpsaksid1", 
        "scanfcktpsaksid2"
    ]


admin.site.register(SuketKelahiran, AdSuketKelahiran)

class AdSuketKematian(admin.ModelAdmin):
    list_display = [
        'penulis',
        'nama',
        'nip',
        'jabatan',
        'nokk',
        'namaalm',
        'nikalm',
        'ttlalm',
        'agamaalm',
        'anakkealm',
        'ibualm',
        'ayahalm',
        'pekerjaanalm',
        'kewarganegaraanalm',
        'alamatalm',
        'tanggal_kematian',
        'jam_kematian',
        'tempat_kematian',
        'penyebab_kematian',
        'tmptmakam',
        'tanggal_pmkn',
        'jam_pmkn',
        'pengantarrt',
        'scankk',
        'date',
        'status',
    ]

admin.site.register(SuketKematian, AdSuketKematian)

class AdSuketPenghasilanTidakTetap(admin.ModelAdmin):
   list_display = (
        'penulis',
        'nama',
        'umur',
        'pekerjaan',
        'alamat',
        'date',
        'status',
        'pengantarrt',
        'scankk',
    )

admin.site.register(SuketPenghasilanTidakTetap, AdSuketPenghasilanTidakTetap)

class AdSuketUsaha(admin.ModelAdmin):
    list_display = [
        'penulis',
        'nama',
        'umur',
        'pekerjaan',
        'alamat',
        'jenisusaha',
        'tahunberdiri',
        'jumlahmodal',
        'alamatusaha',
        'npnpwp',
        'notelepon',
        'jumlahkaryawan',
        'keterangan',
        'date',
        'status',
        'pengantarrt',
        'scanktp',
        'fotousaha',
    ]

admin.site.register(SuketUsaha, AdSuketUsaha)

class AdSuketVaksinNikah(admin.ModelAdmin):
    list_display = [
            'penulis',
            'nama',
            'jenis_kelamin',
            'ttl',
            'agama',
            'pekerjaan',
            'alamat',
            'date',
            'status',
        ]
admin.site.register(SuketVaksinNikah, AdSuketVaksinNikah)

class AdSuketPindahNikah(admin.ModelAdmin):
    list_display = [
            "penulis", 
            "nama1", 
            "jenis_kelamin1", 
            "ttl1", 
            "alamat1", 
            "pekerjaan1", 
            "nama2", 
            "jenis_kelamin2", 
            "ttl2", 
            "alamat2", 
            "pekerjaan2", 
            "date", 
            "status"
        ]
admin.site.register(SuketPindahNikah, AdSuketPindahNikah)

class AdSuketRekKelTani(admin.ModelAdmin):
    list_display = ["penulis", "nama", "jabatan", "sekretariat", "tempat", "bantuan", "tujuan", "date", "status"]
admin.site.register(SuketRekKelTani, AdSuketRekKelTani)

class Adpengumuman(admin.ModelAdmin):
    list_display = ["penulis", "judul", "konten", "date", "picture"]
    
admin.site.register(Pengumuman, Adpengumuman)
