from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class SuketBelumMenikah(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)

class SuketTidakMampu(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)

class SKCK(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    nik = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    kawin = models.CharField(max_length=255)
    pendidikanterakhir = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    scanktp = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)
    
class SuketKTPBedaNama(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis, self.nik)
    
class SuketAhliWaris(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama1 = models.CharField(max_length=255)
    ttl1 = models.CharField(max_length=255)
    alamat1 = models.CharField(max_length=255)
    nama2 = models.CharField(max_length=255)
    ttl2 = models.CharField(max_length=255)
    alamat2 = models.CharField(max_length=255)
    nama3 = models.CharField(max_length=255)
    ttl3 = models.CharField(max_length=255)
    alamat3 = models.CharField(max_length=255)
    nama4 = models.CharField(max_length=255)
    ttl4 = models.CharField(max_length=255)
    alamat4 = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketMTQ(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    suku = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketKehilangan(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    barang1 = models.CharField(max_length=255)
    barang2 = models.CharField(max_length=255)
    barang3 = models.CharField(max_length=255)
    tempat1 = models.CharField(max_length=255)
    tempat2 = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketKelahiran(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    namab = models.CharField(max_length=255)
    jenis_kelaminb = models.CharField(max_length=255)
    tanggal_lahirb = models.CharField(max_length=255)
    tempat_lahirb = models.CharField(max_length=255)
    agamab = models.CharField(max_length=255)
    alamatb = models.CharField(max_length=255)
    anakke = models.CharField(max_length=255)
    namaa = models.CharField(max_length=255)
    umura = models.CharField(max_length=255)
    pekerjaana = models.CharField(max_length=255)
    alamata = models.CharField(max_length=255)
    namai = models.CharField(max_length=255)
    umuri = models.CharField(max_length=255)
    pekerjaani = models.CharField(max_length=255)
    alamati = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    kkb = models.URLField(blank=True, null=True)
    scanfcbnb = models.URLField(blank=True, null=True)
    scanfcktportub = models.URLField(blank=True, null=True)
    scanfcktpsaksib1 = models.URLField(blank=True, null=True)
    scanfcktpsaksib2 = models.URLField(blank=True, null=True)
    kkd = models.URLField(blank=True, null=True)
    kk_ktportud = models.URLField(blank=True, null=True)
    scanfcktpsaksid1 = models.URLField(blank=True, null=True)
    scanfcktpsaksid2 = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketKematian(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    nip = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    nokk = models.CharField(max_length=255)
    namaalm = models.CharField(max_length=255)
    nikalm = models.CharField(max_length=255)
    ttlalm = models.CharField(max_length=255)
    agamaalm = models.CharField(max_length=255)
    anakkealm = models.CharField(max_length=255)
    ibualm = models.CharField(max_length=255)
    ayahalm = models.CharField(max_length=255)
    pekerjaanalm = models.CharField(max_length=255)
    kewarganegaraanalm = models.CharField(max_length=255)
    alamatalm = models.CharField(max_length=255)
    tanggal_kematian = models.CharField(max_length=255)
    jam_kematian = models.CharField(max_length=255)
    tempat_kematian = models.CharField(max_length=255)
    penyebab_kematian = models.CharField(max_length=255)
    tmptmakam = models.CharField(max_length=255)
    tanggal_pmkn = models.CharField(max_length=255)
    jam_pmkn = models.CharField(max_length=255)
    pengantarrt = models.URLField(blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.nama)
    
class SuketPenghasilanTidakTetap(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    pengantarrt = models.URLField(blank=True, null=True)
    scankk = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketUsaha(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    umur = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    jenisusaha = models.CharField(max_length=255)
    tahunberdiri = models.CharField(max_length=255)
    jumlahmodal = models.CharField(max_length=255)
    alamatusaha = models.CharField(max_length=255)
    npnpwp = models.CharField(max_length=255)
    notelepon = models.CharField(max_length=255)
    jumlahkaryawan = models.CharField(max_length=255)
    keterangan = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    pengantarrt = models.URLField(blank=True, null=True)
    scanktp = models.URLField(blank=True, null=True)
    fotousaha = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)
    
class SuketVaksinNikah(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=255)
    ttl = models.CharField(max_length=255)
    agama = models.CharField(max_length=255)
    pekerjaan = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)

class SuketPindahNikah(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama1 = models.CharField(max_length=255)
    ttl1 = models.CharField(max_length=255)
    jenis_kelamin1 = models.CharField(max_length=255)
    agama1 = models.CharField(max_length=255)
    pekerjaan1 = models.CharField(max_length=255)
    alamat1 = models.CharField(max_length=255)
    nama2 = models.CharField(max_length=255)
    ttl2 = models.CharField(max_length=255)
    jenis_kelamin2 = models.CharField(max_length=255)
    agama2 = models.CharField(max_length=255)
    pekerjaan2 = models.CharField(max_length=255)
    alamat2 = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)

class SuketRekKelTani(models.Model):
    penulis = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    sekretariat = models.CharField(max_length=255)
    tempat = models.CharField(max_length=255)
    bantuan = models.CharField(max_length=255)
    tujuan = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    status = models.BooleanField(null=True, blank=True)
    
    def __str__(self):
        return "{} - {}".format(self.penulis)