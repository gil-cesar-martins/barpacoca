from django.db import models

from stdimage.models import StdImageField

import uuid

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    
    class Meta:
        abstract = True

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo
    
class Chef(Base):
    nome = models.CharField('Name', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':600, 'height':600, 'crop':'True'}})
    twitter = models.CharField('Twitter', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    
    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural= 'Chefs'
    
    def __str__(self):
        return self.nome
  
    
