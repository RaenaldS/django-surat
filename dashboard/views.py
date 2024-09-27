from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from django.shortcuts import get_object_or_404
from .models import *
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
# Create your views here.

def dashboard(request):
    template_name = "backend/dashboard.html"
    
    return render(request, template_name)

def suketbelummenikah(request):
    template_name = "backend/suketbelummenikah.html"
    
    suket = SuketBelumMenikah.objects.all()
    
    if request.method == "POST":
       
        SuketBelumMenikah.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat")
        )
    
        return redirect('suketbelummenikah')
    
    context={
        "suket":suket
    }
    
    return render(request, template_name, context)

def edit_suketbelummenikah(request,id):
    template_name = "backend/suketbelummenikah.html"
    
    suket_id = SuketBelumMenikah.objects.get(id=id)
    
    if request.method == "POST":
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.date=timezone.now()
        
        suket_id.save()
        
        return redirect('suketbelummenikah')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

def delete_suketbelummenikah(request,id):
    SuketBelumMenikah.objects.get(id=id).delete()
    
    return redirect('suketbelummenikah')

def sukettidakmampu(request):
    template_name = "backend/sukettidakmampu.html"
    
    suket = SuketTidakMampu.objects.all()
    
    if request.method == "POST":
       
        SuketTidakMampu.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan= request.POST.get("inputPekerjaan")
        )
    
        return redirect('sukettidakmampu')
    
    context={
        "suket":suket
    }
    
    return render(request, template_name, context)

def edit_sukettidakmampu(request,id):
    template_name = "backend/sukettidakmampu.html"
    
    suket_id = SuketTidakMampu.objects.get(id=id)
    
    if request.method == "POST":
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        pekerjaan= request.POST.get("inputPekerjaan")
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.date=timezone.now()
        suket_id.pekerjaan= pekerjaan
        
        suket_id.save()
        
        return redirect('sukettidakmampu')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

def delete_sukettidakmampu(request,id):
    SuketTidakMampu.objects.get(id=id).delete()
    
    return redirect('sukettidakmampu')

def skck(request):
    template_name = "backend/skck.html"
    
    suket = SKCK.objects.all()
    
    if request.method == "POST":
       
        myfile = request.FILES.get("gambar")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        url = fs.url(filename)
        gambar = url
        
        SKCK.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            nik=request.POST.get("inputNIK"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan= request.POST.get("inputPekerjaan"),
            kawin = request.POST.get("inputKawin"),
            pendidikanterakhir = request.POST.get("inputPendidikanterakhir"),
            scanktp = gambar,
        )
    
        return redirect('skck')
    
    context={
        "suket":suket
    }
    
    return render(request, template_name, context)

def edit_skck(request,id):
    template_name = "backend/skck.html"
    
    suket_id = SKCK.objects.get(id=id)
    
    if request.method == "POST":
        penulis=request.user
        nama=request.POST.get("inputNama")
        jenis_kelamin=request.POST.get("inputjk")
        ttl=request.POST.get("inputTtl")
        suku=request.POST.get("inputSuku")
        agama=request.POST.get("inputAgama")
        nik=request.POST.get("inputNIK")
        alamat=request.POST.get("inputAlamat")
        pekerjaan= request.POST.get("inputPekerjaan")
        kawin = request.POST.get("inputKawin")
        pendidikanterakhir = request.POST.get("inputPendidikanterakhir")
        # Mengecek apakah ada file baru yang di-upload
        myfile = request.FILES.get("gambar")
        
        if myfile:
            # Jika ada file baru yang di-upload, simpan file baru
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            suket_id.scanktp = url  # Mengupdate hanya jika ada file baru
        
        suket_id.penulis=penulis
        suket_id.nama=nama
        suket_id.jenis_kelamin=jenis_kelamin
        suket_id.ttl=ttl
        suket_id.suku=suku
        suket_id.agama=agama
        suket_id.nik=nik
        suket_id.alamat=alamat
        suket_id.date=timezone.now()
        suket_id.pekerjaan= pekerjaan
        suket_id.kawin= kawin
        suket_id.pendidikanterakhir= pendidikanterakhir
       
        
        suket_id.save()
        
        return redirect('skck')
    
    context = {
        "value" : suket_id
    }
    
    
    return render(request, template_name, context)

def delete_skck(request,id):
    SKCK.objects.get(id=id).delete()
    
    return redirect('skck')

def suketktpbedanama(request):
    template_name = "backend/suketktpbedanama.html"
    
    suket = SuketKTPBedaNama.objects.all()
    
    if request.method == "POST":
        # Membuat SuketKTPBedaNama baru
        SuketKTPBedaNama.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            agama=request.POST.get("inputAgama"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan")
        )
    
        return redirect('suketktpbedanama')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit SuketKTPBedaNama
def edit_suketktpbedanama(request, id):
    template_name = "backend/suketktpbedanama.html"
    
    suket_id = SuketKTPBedaNama.objects.get(id=id)
    
    if request.method == "POST":
        # Mengedit data SuketKTPBedaNama
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        ttl = request.POST.get("inputTtl")
        agama = request.POST.get("inputAgama")
        alamat = request.POST.get("inputAlamat")
        pekerjaan = request.POST.get("inputPekerjaan")
        
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.ttl = ttl
        suket_id.agama = agama
        suket_id.alamat = alamat
        suket_id.pekerjaan = pekerjaan
        suket_id.date = timezone.now() 
        
        suket_id.save()
        
        return redirect('suketktpbedanama')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)


def delete_suketktpbedanama(request, id):
 
    SuketKTPBedaNama.objects.get(id=id).delete()
    
    return redirect('suketktpbedanama')

def suketahliwaris(request):
    template_name = "backend/suketahliwaris.html"
    
    suket = SuketAhliWaris.objects.all()
    
    if request.method == "POST":
        # Membuat SuketAhliWaris baru
        SuketAhliWaris.objects.create(
            penulis=request.user,
            nama1=request.POST.get("inputNama1"),
            ttl1=request.POST.get("inputTtl1"),
            alamat1=request.POST.get("inputAlamat1"),
            nama2=request.POST.get("inputNama2"),
            ttl2=request.POST.get("inputTtl2"),
            alamat2=request.POST.get("inputAlamat2"),
            nama3=request.POST.get("inputNama3"),
            ttl3=request.POST.get("inputTtl3"),
            alamat3=request.POST.get("inputAlamat3"),
            nama4=request.POST.get("inputNama4"),
            ttl4=request.POST.get("inputTtl4"),
            alamat4=request.POST.get("inputAlamat4")
        )
    
        return redirect('suketahliwaris')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit SuketAhliWaris
def edit_suketahliwaris(request, id):
    template_name = "backend/suketahliwaris.html"
    
    suket_id = SuketAhliWaris.objects.get(id=id)
    
    if request.method == "POST":
        # Mengedit data SuketAhliWaris
        penulis = request.user
        nama1 = request.POST.get("inputNama1")
        ttl1 = request.POST.get("inputTtl1")
        alamat1 = request.POST.get("inputAlamat1")
        nama2 = request.POST.get("inputNama2")
        ttl2 = request.POST.get("inputTtl2")
        alamat2 = request.POST.get("inputAlamat2")
        nama3 = request.POST.get("inputNama3")
        ttl3 = request.POST.get("inputTtl3")
        alamat3 = request.POST.get("inputAlamat3")
        nama4 = request.POST.get("inputNama4")
        ttl4 = request.POST.get("inputTtl4")
        alamat4 = request.POST.get("inputAlamat4")
        
        suket_id.penulis = penulis
        suket_id.nama1 = nama1
        suket_id.ttl1 = ttl1
        suket_id.alamat1 = alamat1
        suket_id.nama2 = nama2
        suket_id.ttl2 = ttl2
        suket_id.alamat2 = alamat2
        suket_id.nama3 = nama3
        suket_id.ttl3 = ttl3
        suket_id.alamat3 = alamat3
        suket_id.nama4 = nama4
        suket_id.ttl4 = ttl4
        suket_id.alamat4 = alamat4
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        
        suket_id.save()
        
        return redirect('suketahliwaris')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus SuketAhliWaris
def delete_suketahliwaris(request, id):
    # Menghapus data berdasarkan id
    SuketAhliWaris.objects.get(id=id).delete()
    
    return redirect('suketahliwaris')

def suketMTQ(request):
    template_name = "backend/suketMTQ.html"
    
    suket = SuketMTQ.objects.all()
    
    if request.method == "POST":
        # Membuat SuketMTQ baru
        SuketMTQ.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            suku=request.POST.get("inputSuku"),
            agama=request.POST.get("inputAgama"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan")
        )
    
        return redirect('suketMTQ')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit SuketMTQ
def edit_suketMTQ(request, id):
    template_name = "backend/suketMTQ.html"
    
    suket_id = SuketMTQ.objects.get(id=id)
    
    if request.method == "POST":
        # Mengedit data SuketMTQ
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        ttl = request.POST.get("inputTtl")
        suku = request.POST.get("inputSuku")
        agama = request.POST.get("inputAgama")
        alamat = request.POST.get("inputAlamat")
        pekerjaan = request.POST.get("inputPekerjaan")
        
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.ttl = ttl
        suket_id.suku = suku
        suket_id.agama = agama
        suket_id.alamat = alamat
        suket_id.pekerjaan = pekerjaan
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        
        suket_id.save()
        
        return redirect('suketMTQ')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus SuketMTQ
def delete_suketMTQ(request, id):
    # Menghapus data berdasarkan id
    SuketMTQ.objects.get(id=id).delete()
    
    return redirect('suketMTQ')

def suketkehilangan(request):
    template_name = "backend/suketkehilangan.html"
    
    suket = SuketKehilangan.objects.all()
    
    if request.method == "POST":
        # Membuat SuketKehilangan baru
        SuketKehilangan.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            umur=request.POST.get("inputUmur"),
            alamat=request.POST.get("inputAlamat"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            barang1=request.POST.get("inputBarang1"),
            barang2=request.POST.get("inputBarang2"),
            barang3=request.POST.get("inputBarang3"),
            tempat1=request.POST.get("inputTempat1"),
            tempat2=request.POST.get("inputTempat2")
        )
    
        return redirect('suketkehilangan')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit SuketKehilangan
def edit_suketkehilangan(request, id):
    template_name = "backend/suketkehilangan.html"
    
    suket_id = SuketKehilangan.objects.get(id=id)
    
    if request.method == "POST":
        # Mengedit data SuketKehilangan
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        umur = request.POST.get("inputUmur")
        alamat = request.POST.get("inputAlamat")
        pekerjaan = request.POST.get("inputPekerjaan")
        barang1 = request.POST.get("inputBarang1")
        barang2 = request.POST.get("inputBarang2")
        barang3 = request.POST.get("inputBarang3")
        tempat1 = request.POST.get("inputTempat1")
        tempat2 = request.POST.get("inputTempat2")
        
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.umur = umur
        suket_id.alamat = alamat
        suket_id.pekerjaan = pekerjaan
        suket_id.barang1 = barang1
        suket_id.barang2 = barang2
        suket_id.barang3 = barang3
        suket_id.tempat1 = tempat1
        suket_id.tempat2 = tempat2
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        
        suket_id.save()
        
        return redirect('suketkehilangan')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus SuketKehilangan
def delete_suketkehilangan(request, id):
    # Menghapus data berdasarkan id
    SuketKehilangan.objects.get(id=id).delete()
    
    return redirect('suketkehilangan')

def suketkelahiran(request):
    template_name = "backend/suketkelahiran.html"
    
    suket = SuketKelahiran.objects.all()
    
    if request.method == "POST":
        # Menyimpan file-file yang di-upload
        kkb_file = request.FILES.get("kkb")
        fs = FileSystemStorage()
        if kkb_file:
            kkb_filename = fs.save(kkb_file.name, kkb_file)
            kkb_url = fs.url(kkb_filename)
        else:
            kkb_url = None
        
        scanfcbnb_file = request.FILES.get("scanfcbnb")
        if scanfcbnb_file:
            scanfcbnb_filename = fs.save(scanfcbnb_file.name, scanfcbnb_file)
            scanfcbnb_url = fs.url(scanfcbnb_filename)
        else:
            scanfcbnb_url = None

        scanfcktportub_file = request.FILES.get("scanfcktportub")
        if scanfcktportub_file:
            scanfcktportub_filename = fs.save(scanfcktportub_file.name, scanfcktportub_file)
            scanfcktportub_url = fs.url(scanfcktportub_filename)
        else:
            scanfcktportub_url = None

        # Simpan sisa file serupa di bawah ini
        scanfcktpsaksib1_file = request.FILES.get("scanfcktpsaksib1")
        if scanfcktpsaksib1_file:
            scanfcktpsaksib1_filename = fs.save(scanfcktpsaksib1_file.name, scanfcktpsaksib1_file)
            scanfcktpsaksib1_url = fs.url(scanfcktpsaksib1_filename)
        else:
            scanfcktpsaksib1_url = None

        scanfcktpsaksib2_file = request.FILES.get("scanfcktpsaksib2")
        if scanfcktpsaksib2_file:
            scanfcktpsaksib2_filename = fs.save(scanfcktpsaksib2_file.name, scanfcktpsaksib2_file)
            scanfcktpsaksib2_url = fs.url(scanfcktpsaksib2_filename)
        else:
            scanfcktpsaksib2_url = None
            
        kkd_file = request.FILES.get("kkd")
        kkd_url = fs.url(fs.save(kkd_file.name, kkd_file)) if kkd_file else None

        kk_ktportud_file = request.FILES.get("kk_ktportud")
        kk_ktportud_url = fs.url(fs.save(kk_ktportud_file.name, kk_ktportud_file)) if kk_ktportud_file else None

        scanfcktpsaksid1_file = request.FILES.get("scanfcktpsaksid1")
        scanfcktpsaksid1_url = fs.url(fs.save(scanfcktpsaksid1_file.name, scanfcktpsaksid1_file)) if scanfcktpsaksid1_file else None

        scanfcktpsaksid2_file = request.FILES.get("scanfcktpsaksid2")
        scanfcktpsaksid2_url = fs.url(fs.save(scanfcktpsaksid2_file.name, scanfcktpsaksid2_file)) if scanfcktpsaksid2_file else None

        # Menyimpan data SuketKelahiran
        SuketKelahiran.objects.create(
            penulis=request.user,
            namab=request.POST.get("inputNamaB"),
            jenis_kelaminb=request.POST.get("inputJenisKelaminB"),
            tanggal_lahirb=request.POST.get("inputTanggalLahirB"),
            tempat_lahirb=request.POST.get("inputTempatLahirB"),
            agamab=request.POST.get("inputAgamaB"),
            alamatb=request.POST.get("inputAlamatB"),
            anakke=request.POST.get("inputAnakKe"),
            namaa=request.POST.get("inputNamaA"),
            umura=request.POST.get("inputUmurA"),
            pekerjaana=request.POST.get("inputPekerjaanA"),
            alamata=request.POST.get("inputAlamatA"),
            namai=request.POST.get("inputNamaI"),
            umuri=request.POST.get("inputUmurI"),
            pekerjaani=request.POST.get("inputPekerjaanI"),
            alamati=request.POST.get("inputAlamatI"),
            kkb=kkb_url,
            scanfcbnb=scanfcbnb_url,
            scanfcktportub=scanfcktportub_url,
            scanfcktpsaksib1=scanfcktpsaksib1_url,
            scanfcktpsaksib2=scanfcktpsaksib2_url,
            kkd=kkd_url,
            kk_ktportud=kk_ktportud_url,
            scanfcktpsaksid1=scanfcktpsaksid1_url,
            scanfcktpsaksid2=scanfcktpsaksid2_url
        )
    
        return redirect('suketkelahiran')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit SuketKelahiran
def edit_suketkelahiran(request, id):
    template_name = "backend/suketkelahiran.html"
    
    suket_id = SuketKelahiran.objects.get(id=id)
    
    if request.method == "POST":
        # Menyimpan file baru jika ada
        kkb_file = request.FILES.get("kkb")
        fs = FileSystemStorage()
        if kkb_file:
            kkb_filename = fs.save(kkb_file.name, kkb_file)
            kkb_url = fs.url(kkb_filename)
            suket_id.kkb = kkb_url  # Mengupdate hanya jika ada file baru
        
        scanfcbnb_file = request.FILES.get("scanfcbnb")
        if scanfcbnb_file:
            scanfcbnb_filename = fs.save(scanfcbnb_file.name, scanfcbnb_file)
            scanfcbnb_url = fs.url(scanfcbnb_filename)
            suket_id.scanfcbnb = scanfcbnb_url

        scanfcktportub_file = request.FILES.get("scanfcktportub")
        if scanfcktportub_file:
            scanfcktportub_filename = fs.save(scanfcktportub_file.name, scanfcktportub_file)
            scanfcktportub_url = fs.url(scanfcktportub_filename)
            suket_id.scanfcktportub = scanfcktportub_url

        # Simpan sisa file serupa di bawah ini
        scanfcktpsaksib1_file = request.FILES.get("scanfcktpsaksib1")
        if scanfcktpsaksib1_file:
            scanfcktpsaksib1_filename = fs.save(scanfcktpsaksib1_file.name, scanfcktpsaksib1_file)
            scanfcktpsaksib1_url = fs.url(scanfcktpsaksib1_filename)
            suket_id.scanfcktpsaksib1 = scanfcktpsaksib1_url

        scanfcktpsaksib2_file = request.FILES.get("scanfcktpsaksib2")
        if scanfcktpsaksib2_file:
            scanfcktpsaksib2_filename = fs.save(scanfcktpsaksib2_file.name, scanfcktpsaksib2_file)
            scanfcktpsaksib2_url = fs.url(scanfcktpsaksib2_filename)
            suket_id.scanfcktpsaksib2 = scanfcktpsaksib2_url
        
        kkd_file = request.FILES.get("kkd")
        if kkd_file:
            kkd_url = fs.url(fs.save(kkd_file.name, kkd_file))
            suket_id.kkd = kkd_url

        kk_ktportud_file = request.FILES.get("kk_ktportud")
        if kk_ktportud_file:
            kk_ktportud_url = fs.url(fs.save(kk_ktportud_file.name, kk_ktportud_file))
            suket_id.kk_ktportud = kk_ktportud_url

        scanfcktpsaksid1_file = request.FILES.get("scanfcktpsaksid1")
        if scanfcktpsaksid1_file:
            scanfcktpsaksid1_url = fs.url(fs.save(scanfcktpsaksid1_file.name, scanfcktpsaksid1_file))
            suket_id.scanfcktpsaksid1 = scanfcktpsaksid1_url

        scanfcktpsaksid2_file = request.FILES.get("scanfcktpsaksid2")
        if scanfcktpsaksid2_file:
            scanfcktpsaksid2_url = fs.url(fs.save(scanfcktpsaksid2_file.name, scanfcktpsaksid2_file))
            suket_id.scanfcktpsaksid2 = scanfcktpsaksid2_url

        # Mengedit data SuketKelahiran
        suket_id.penulis = request.user
        suket_id.namab = request.POST.get("inputNamaB")
        suket_id.jenis_kelaminb = request.POST.get("inputJenisKelaminB")
        suket_id.tanggal_lahirb = request.POST.get("inputTanggalLahirB")
        suket_id.tempat_lahirb = request.POST.get("inputTempatLahirB")
        suket_id.agamab = request.POST.get("inputAgamaB")
        suket_id.alamatb = request.POST.get("inputAlamatB")
        suket_id.anakke = request.POST.get("inputAnakKe")
        suket_id.namaa = request.POST.get("inputNamaA")
        suket_id.umura = request.POST.get("inputUmurA")
        suket_id.pekerjaana = request.POST.get("inputPekerjaanA")
        suket_id.alamata = request.POST.get("inputAlamatA")
        suket_id.namai = request.POST.get("inputNamaI")
        suket_id.umuri = request.POST.get("inputUmurI")
        suket_id.pekerjaani = request.POST.get("inputPekerjaanI")
        suket_id.alamati = request.POST.get("inputAlamatI")
        suket_id.date = timezone.now()  # Mengupdate tanggal saat edit
        
        suket_id.save()
        
        return redirect('suketkelahiran')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus SuketKelahiran
def delete_suketkelahiran(request, id):
    SuketKelahiran.objects.get(id=id).delete()
    
    return redirect('suketkelahiran')

def suketkematian(request):
    template_name = "backend/suketkematian.html"
    
    suket = SuketKematian.objects.all()
    
    if request.method == "POST":
       
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")
        
        fs = FileSystemStorage()

        # Jika ada file pengantar RT yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            url_pengantar = fs.url(filename_pengantar)
        else:
            url_pengantar = None
        
        # Jika ada file scan KK yang di-upload
        if myfile_scankk:
            filename_scankk = fs.save(myfile_scankk.name, myfile_scankk)
            url_scankk = fs.url(filename_scankk)
        else:
            url_scankk = None
        
        # Membuat objek SuketKematian baru
        SuketKematian.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            nip=request.POST.get("inputNIP"),
            jabatan=request.POST.get("inputJabatan"),
            nokk=request.POST.get("inputNoKK"),
            namaalm=request.POST.get("inputNamaAlm"),
            nikalm=request.POST.get("inputNIKAlm"),
            ttlalm=request.POST.get("inputTTLAlm"),
            agamaalm=request.POST.get("inputAgamaAlm"),
            anakkealm=request.POST.get("inputAnakkeAlm"),
            ibualm=request.POST.get("inputIbuAlm"),
            ayahalm=request.POST.get("inputAyahAlm"),
            pekerjaanalm=request.POST.get("inputPekerjaanAlm"),
            kewarganegaraanalm=request.POST.get("inputKewarganegaraanAlm"),
            alamatalm=request.POST.get("inputAlamatAlm"),
            tanggal_kematian=request.POST.get("inputTanggalKematian"),
            jam_kematian=request.POST.get("inputJamKematian"),
            tempat_kematian=request.POST.get("inputTempatKematian"),
            penyebab_kematian=request.POST.get("inputPenyebabKematian"),
            tmptmakam=request.POST.get("inputTempatMakam"),
            tanggal_pmkn=request.POST.get("inputTanggalPemakaman"),
            jam_pmkn=request.POST.get("inputJamPemakaman"),
            pengantarrt=url_pengantar,
            scankk=url_scankk,
        )
    
        return redirect('suketkematian')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Kematian
def edit_suketkematian(request, id):
    template_name = "backend/suketkematian.html"
    
    suket_id = SuketKematian.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        nip = request.POST.get("inputNIP")
        jabatan = request.POST.get("inputJabatan")
        nokk = request.POST.get("inputNoKK")
        namaalm = request.POST.get("inputNamaAlm")
        nikalm = request.POST.get("inputNIKAlm")
        ttlalm = request.POST.get("inputTTLAlm")
        agamaalm = request.POST.get("inputAgamaAlm")
        anakkealm = request.POST.get("inputAnakkeAlm")
        ibualm = request.POST.get("inputIbuAlm")
        ayahalm = request.POST.get("inputAyahAlm")
        pekerjaanalm = request.POST.get("inputPekerjaanAlm")
        kewarganegaraanalm = request.POST.get("inputKewarganegaraanAlm")
        alamatalm = request.POST.get("inputAlamatAlm")
        tanggal_kematian = request.POST.get("inputTanggalKematian")
        jam_kematian = request.POST.get("inputJamKematian")
        tempat_kematian = request.POST.get("inputTempatKematian")
        penyebab_kematian = request.POST.get("inputPenyebabKematian")
        tmptmakam = request.POST.get("inputTempatMakam")
        tanggal_pmkn = request.POST.get("inputTanggalPemakaman")
        jam_pmkn = request.POST.get("inputJamPemakaman")

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")
        fs = FileSystemStorage()

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            suket_id.pengantarrt = fs.url(filename_pengantar)
        
        # Jika ada file scan KK baru yang di-upload
        if myfile_scankk:
            filename_scankk = fs.save(myfile_scankk.name, myfile_scankk)
            suket_id.scankk = fs.url(filename_scankk)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.nip = nip
        suket_id.jabatan = jabatan
        suket_id.nokk = nokk
        suket_id.namaalm = namaalm
        suket_id.nikalm = nikalm
        suket_id.ttlalm = ttlalm
        suket_id.agamaalm = agamaalm
        suket_id.anakkealm = anakkealm
        suket_id.ibualm = ibualm
        suket_id.ayahalm = ayahalm
        suket_id.pekerjaanalm = pekerjaanalm
        suket_id.kewarganegaraanalm = kewarganegaraanalm
        suket_id.alamatalm = alamatalm
        suket_id.tanggal_kematian = tanggal_kematian
        suket_id.jam_kematian = jam_kematian
        suket_id.tempat_kematian = tempat_kematian
        suket_id.penyebab_kematian = penyebab_kematian
        suket_id.tmptmakam = tmptmakam
        suket_id.tanggal_pmkn = tanggal_pmkn
        suket_id.jam_pmkn = jam_pmkn
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketkematian')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Kematian
def delete_suketkematian(request, id):
    SuketKematian.objects.get(id=id).delete()
    return redirect('suketkematian')

def suketpenghasilantidaktetap(request):
    template_name = "backend/suketpenghasilantidaktetap.html"
    
    suket = SuketPenghasilanTidakTetap.objects.all()
    
    if request.method == "POST":
        # Mengambil file yang diupload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")
        
        fs = FileSystemStorage()

        # Jika ada file pengantar RT yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            url_pengantar = fs.url(filename_pengantar)
        else:
            url_pengantar = None
        
        # Jika ada file scan KK yang di-upload
        if myfile_scankk:
            filename_scankk = fs.save(myfile_scankk.name, myfile_scankk)
            url_scankk = fs.url(filename_scankk)
        else:
            url_scankk = None
        
        # Membuat objek SuketPenghasilanTidakTetap baru
        SuketPenghasilanTidakTetap.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            umur=request.POST.get("inputUmur"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat"),
            pengantarrt=url_pengantar,
            scankk=url_scankk,
        )
    
        return redirect('suketpenghasilantidaktetap')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Penghasilan Tidak Tetap
def edit_suketpenghasilantidaktetap(request, id):
    template_name = "backend/suketpenghasilantidaktetap.html"
    
    suket_id = SuketPenghasilanTidakTetap.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        umur = request.POST.get("inputUmur")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scankk = request.FILES.get("scankk")
        fs = FileSystemStorage()

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            suket_id.pengantarrt = fs.url(filename_pengantar)
        
        # Jika ada file scan KK baru yang di-upload
        if myfile_scankk:
            filename_scankk = fs.save(myfile_scankk.name, myfile_scankk)
            suket_id.scankk = fs.url(filename_scankk)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.umur = umur
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketpenghasilantidaktetap')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Penghasilan Tidak Tetap
def delete_suketpenghasilantidaktetap(request, id):
    SuketPenghasilanTidakTetap.objects.get(id=id).delete()
    return redirect('suketpenghasilantidaktetap')

def suketusaha(request):
    template_name = "backend/suketusaha.html"
    
    suket = SuketUsaha.objects.all()
    
    if request.method == "POST":
        # Mengambil file yang diupload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scanktp = request.FILES.get("scanktp")
        myfile_fotousaha = request.FILES.get("fotousaha")
        
        fs = FileSystemStorage()

        # Jika ada file pengantar RT yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            url_pengantar = fs.url(filename_pengantar)
        else:
            url_pengantar = None
        
        # Jika ada file scan KTP yang di-upload
        if myfile_scanktp:
            filename_scanktp = fs.save(myfile_scanktp.name, myfile_scanktp)
            url_scanktp = fs.url(filename_scanktp)
        else:
            url_scanktp = None
        
        # Jika ada file foto usaha yang di-upload
        if myfile_fotousaha:
            filename_fotousaha = fs.save(myfile_fotousaha.name, myfile_fotousaha)
            url_fotousaha = fs.url(filename_fotousaha)
        else:
            url_fotousaha = None
        
        # Membuat objek SuketUsaha baru
        SuketUsaha.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            umur=request.POST.get("inputUmur"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat"),
            jenisusaha=request.POST.get("inputJenisUsaha"),
            tahunberdiri=request.POST.get("inputTahunBerdiri"),
            jumlahmodal=request.POST.get("inputJumlahModal"),
            alamatusaha=request.POST.get("inputAlamatUsaha"),
            npnpwp=request.POST.get("inputNpwp"),
            notelepon=request.POST.get("inputNoTelepon"),
            jumlahkaryawan=request.POST.get("inputJumlahKaryawan"),
            keterangan=request.POST.get("inputKeterangan"),
            pengantarrt=url_pengantar,
            scanktp=url_scanktp,
            fotousaha=url_fotousaha,
        )
    
        return redirect('suketusaha')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Usaha
def edit_suketusaha(request, id):
    template_name = "backend/suketusaha.html"
    
    suket_id = SuketUsaha.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        umur = request.POST.get("inputUmur")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")
        jenisusaha = request.POST.get("inputJenisUsaha")
        tahunberdiri = request.POST.get("inputTahunBerdiri")
        jumlahmodal = request.POST.get("inputJumlahModal")
        alamatusaha = request.POST.get("inputAlamatUsaha")
        npnpwp = request.POST.get("inputNpwp")
        notelepon = request.POST.get("inputNoTelepon")
        jumlahkaryawan = request.POST.get("inputJumlahKaryawan")
        keterangan = request.POST.get("inputKeterangan")

        # Mengecek apakah ada file baru yang di-upload
        myfile_pengantar = request.FILES.get("pengantarrt")
        myfile_scanktp = request.FILES.get("scanktp")
        myfile_fotousaha = request.FILES.get("fotousaha")
        fs = FileSystemStorage()

        # Jika ada file pengantar RT baru yang di-upload
        if myfile_pengantar:
            filename_pengantar = fs.save(myfile_pengantar.name, myfile_pengantar)
            suket_id.pengantarrt = fs.url(filename_pengantar)
        
        # Jika ada file scan KTP baru yang di-upload
        if myfile_scanktp:
            filename_scanktp = fs.save(myfile_scanktp.name, myfile_scanktp)
            suket_id.scanktp = fs.url(filename_scanktp)
        
        # Jika ada file foto usaha baru yang di-upload
        if myfile_fotousaha:
            filename_fotousaha = fs.save(myfile_fotousaha.name, myfile_fotousaha)
            suket_id.fotousaha = fs.url(filename_fotousaha)
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.umur = umur
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.jenisusaha = jenisusaha
        suket_id.tahunberdiri = tahunberdiri
        suket_id.jumlahmodal = jumlahmodal
        suket_id.alamatusaha = alamatusaha
        suket_id.npnpwp = npnpwp
        suket_id.notelepon = notelepon
        suket_id.jumlahkaryawan = jumlahkaryawan
        suket_id.keterangan = keterangan
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketusaha')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Usaha
def delete_suketusaha(request, id):
    SuketUsaha.objects.get(id=id).delete()
    return redirect('suketusaha')

def suketvaksinnikah(request):
    template_name = "backend/suketvaksinnikah.html"
    
    suket = SuketVaksinNikah.objects.all()
    
    if request.method == "POST":
        # Membuat objek SuketVaksinNikah baru
        SuketVaksinNikah.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jenis_kelamin=request.POST.get("inputjk"),
            ttl=request.POST.get("inputTtl"),
            agama=request.POST.get("inputAgama"),
            pekerjaan=request.POST.get("inputPekerjaan"),
            alamat=request.POST.get("inputAlamat")
        )
    
        return redirect('suketvaksinnikah')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Vaksin Nikah
def edit_suketvaksinnikah(request, id):
    template_name = "backend/suketvaksinnikah.html"
    
    suket_id = SuketVaksinNikah.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        jenis_kelamin = request.POST.get("inputjk")
        ttl = request.POST.get("inputTtl")
        agama = request.POST.get("inputAgama")
        pekerjaan = request.POST.get("inputPekerjaan")
        alamat = request.POST.get("inputAlamat")
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jenis_kelamin = jenis_kelamin
        suket_id.ttl = ttl
        suket_id.agama = agama
        suket_id.pekerjaan = pekerjaan
        suket_id.alamat = alamat
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketvaksinnikah')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Vaksin Nikah
def delete_suketvaksinnikah(request, id):
    SuketVaksinNikah.objects.get(id=id).delete()
    return redirect('suketvaksinnikah')

def suketpindahnikah(request):
    template_name = "backend/suketpindahnikah.html"
    
    suket = SuketPindahNikah.objects.all()
    
    if request.method == "POST":
        # Membuat objek SuketPindahNikah baru
        SuketPindahNikah.objects.create(
            penulis=request.user,
            nama1=request.POST.get("inputNama1"),
            ttl1=request.POST.get("inputTtl1"),
            jenis_kelamin1=request.POST.get("inputJenisKelamin1"),
            agama1=request.POST.get("inputAgama1"),
            pekerjaan1=request.POST.get("inputPekerjaan1"),
            alamat1=request.POST.get("inputAlamat1"),
            nama2=request.POST.get("inputNama2"),
            ttl2=request.POST.get("inputTtl2"),
            jenis_kelamin2=request.POST.get("inputJenisKelamin2"),
            agama2=request.POST.get("inputAgama2"),
            pekerjaan2=request.POST.get("inputPekerjaan2"),
            alamat2=request.POST.get("inputAlamat2")
        )
    
        return redirect('suketpindahnikah')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Pindah Nikah
def edit_suketpindahnikah(request, id):
    template_name = "backend/suketpindahnikah.html"
    
    suket_id = SuketPindahNikah.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama1 = request.POST.get("inputNama1")
        ttl1 = request.POST.get("inputTtl1")
        jenis_kelamin1 = request.POST.get("inputJenisKelamin1")
        agama1 = request.POST.get("inputAgama1")
        pekerjaan1 = request.POST.get("inputPekerjaan1")
        alamat1 = request.POST.get("inputAlamat1")
        nama2 = request.POST.get("inputNama2")
        ttl2 = request.POST.get("inputTtl2")
        jenis_kelamin2 = request.POST.get("inputJenisKelamin2")
        agama2 = request.POST.get("inputAgama2")
        pekerjaan2 = request.POST.get("inputPekerjaan2")
        alamat2 = request.POST.get("inputAlamat2")
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama1 = nama1
        suket_id.ttl1 = ttl1
        suket_id.jenis_kelamin1 = jenis_kelamin1
        suket_id.agama1 = agama1
        suket_id.pekerjaan1 = pekerjaan1
        suket_id.alamat1 = alamat1
        suket_id.nama2 = nama2
        suket_id.ttl2 = ttl2
        suket_id.jenis_kelamin2 = jenis_kelamin2
        suket_id.agama2 = agama2
        suket_id.pekerjaan2 = pekerjaan2
        suket_id.alamat2 = alamat2
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketpindahnikah')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Pindah Nikah
def delete_suketpindahnikah(request, id):
    SuketPindahNikah.objects.get(id=id).delete()
    return redirect('suketpindahnikah')

def suketrekkeltani(request):
    template_name = "backend/suketrekkeltani.html"
    
    suket = SuketRekKelTani.objects.all()
    
    if request.method == "POST":
        # Membuat objek SuketRekKelTani baru
        SuketRekKelTani.objects.create(
            penulis=request.user,
            nama=request.POST.get("inputNama"),
            jabatan=request.POST.get("inputJabatan"),
            sekretariat=request.POST.get("inputSekretariat"),
            tempat=request.POST.get("inputTempat"),
            bantuan=request.POST.get("inputBantuan"),
            tujuan=request.POST.get("inputTujuan")
        )
    
        return redirect('suketrekkeltani')
    
    context = {
        "suket": suket
    }
    
    return render(request, template_name, context)

# View untuk mengedit data Suket Rekomendasi Kelompok Tani
def edit_suketrekkeltani(request, id):
    template_name = "backend/suketrekkeltani.html"
    
    suket_id = SuketRekKelTani.objects.get(id=id)
    
    if request.method == "POST":
        # Mengambil input data dari form
        penulis = request.user
        nama = request.POST.get("inputNama")
        jabatan = request.POST.get("inputJabatan")
        sekretariat = request.POST.get("inputSekretariat")
        tempat = request.POST.get("inputTempat")
        bantuan = request.POST.get("inputBantuan")
        tujuan = request.POST.get("inputTujuan")
        
        # Update data di objek suket_id
        suket_id.penulis = penulis
        suket_id.nama = nama
        suket_id.jabatan = jabatan
        suket_id.sekretariat = sekretariat
        suket_id.tempat = tempat
        suket_id.bantuan = bantuan
        suket_id.tujuan = tujuan
        suket_id.date = timezone.now()

        suket_id.save()
        
        return redirect('suketrekkeltani')
    
    context = {
        "value": suket_id
    }
    
    return render(request, template_name, context)

# View untuk menghapus data Suket Rekomendasi Kelompok Tani
def delete_suketrekkeltani(request, id):
    SuketRekKelTani.objects.get(id=id).delete()
    return redirect('suketrekkeltani')