from django.db import models

class person(models.Model):
    name = models.CharField(max_length=30,verbose_name='name')
    email = models.EmailField(verbose_name='email')
    phone = models.CharField(max_length=15, verbose_name='phone')

class product(models.Model):
    name = models.CharField(max_length=40, verbose_name='name')
    ref = models.CharField(max_length=40, verbose_name='reference')