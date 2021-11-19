from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tipo_Negocio(models.Model):
    tipo = models.CharField(max_length=255)
    criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tipo

class Negocio(models.Model):
    nome_fantasia = models.CharField(max_length=255)
    endereco = models.TextField()
    tipo = models.ForeignKey(Tipo_Negocio, on_delete=models.DO_NOTHING)
    telefone = models.CharField(max_length=14)
    celular = models.CharField(max_length=14)
    instagram = models.URLField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_liberacao = models.DateTimeField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_fantasia

class Evento(models.Model):
    descricao = models.CharField(max_length=255)
    local = models.CharField(max_length=255)
    data_evento = models.DateTimeField()
    hora = models.TimeField()
    criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao

class SiteAreas(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    url = models.SlugField(max_length=255, unique=True)
    foto_capa = models.ImageField()
    ativo = models.BooleanField()
    criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class Atracoe(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    foto_capa = models.ImageField()
    foto1_atracao = models.ImageField()
    foto2_atracao = models.ImageField()
    foto3_atracao = models.ImageField()
    foto4_atracao = models.ImageField()
    foto5_atracao = models.ImageField()
    ativo = models.BooleanField()
    criado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo